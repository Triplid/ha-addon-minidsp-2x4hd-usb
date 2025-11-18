#!/usr/bin/env python3
import hid
import json
import time
import sys

VID = 0x2752  # miniDSP
PID = 0x0011  # 2x4 HD

def get_status():
    try:
        h = hid.device()
        h.open(VID, PID)
        
        # Report 0x81: Master status (preset в байте 3: 0-3 -> 1-4)
        master_report = h.get_feature_report(0x81, 8)
        preset = int(master_report[3]) + 1 if len(master_report) > 3 else 0
        
        # Report 0x82: Input source (байт 1: 0=analog, 1=digital)
        source_report = h.get_feature_report(0x82, 8)
        source_num = int(source_report[1]) if len(source_report) > 1 else 0
        source = "analog" if source_num == 0 else "digital"
        
        h.close()
        return {"preset": preset, "source": source}
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return {"preset": 0, "source": "error"}

while True:
    status = get_status()
    with open('/share/minidsp_status.json', 'w') as f:
        json.dump(status, f, indent=2)
    print(f"Status: {status}")
    time.sleep(10)
