#!/usr/bin/env python3
import hid
import json
import time
import sys
import os
import argparse

VID = 0x2752  # miniDSP
PID = 0x0011  # 2x4 HD

def get_status():
    try:
        with hid.Device(VID, PID) as h:
            # Report 0x81: Master status (preset в байте 3: 0-3 -> 1-4)
            master_report = h.get_feature_report(0x81, 8)
            preset = int(master_report[3]) + 1 if len(master_report) > 3 else 0

            # Report 0x82: Input source (байт 1: 0=analog, 1=digital)
            source_report = h.get_feature_report(0x82, 8)
            source_num = int(source_report[1]) if len(source_report) > 1 else 0
            source = "analog" if source_num == 0 else "digital"

        return {"preset": preset, "source": source, "error": None}
    except Exception as e:
        error_msg = f"Error: {e}"
        print(error_msg, file=sys.stderr)
        return {"preset": 0, "source": "error", "error": error_msg}

def main():
    parser = argparse.ArgumentParser(description='MiniDSP Status Monitor')
    parser.add_argument('--interval', type=int, default=10, help='Update interval in seconds')
    args = parser.parse_args()
    
    # Создаем папку share если её нет
    share_dir = '/share'
    if not os.path.exists(share_dir):
        os.makedirs(share_dir)
    
    print(f"Starting MiniDSP 2x4 HD USB monitor (update interval: {args.interval}s)")
    
    while True:
        status = get_status()
        try:
            with open('/share/minidsp_status.json', 'w') as f:
                json.dump(status, f, indent=2)
            # Также пишем в stdout для логов HA
            print(f"Status updated: {status}")
        except Exception as e:
            print(f"Cannot write to /share: {e}", file=sys.stderr)
        
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
