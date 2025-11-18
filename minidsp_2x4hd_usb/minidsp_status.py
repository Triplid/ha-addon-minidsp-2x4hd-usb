#!/usr/bin/env python3
import hid
import json
import time
import os
import sys
from threading import Thread

VID = 0x2752
PID = 0x0011
STATUS_FILE = "/share/minidsp_status.json"
COMMAND_FILE = "/share/minidsp_command.json"

def find_device():
    for d in hid.enumerate():
        if d['vendor_id'] == VID and d['product_id'] == PID:
            return d['path']
    return None

def send_command(report_id, data):
    try:
        h = hid.device()
        h.open_path(find_device())
        h.send_feature_report(bytes([report_id] + data))
        h.close()
        return True
    except Exception as e:
        print(f"Command error: {e}", file=sys.stderr)
        return False

def get_status():
    try:
        h = hid.device()
        h.open_path(find_device())

        # Master status — текущий пресет в байте 3 (0..3 → 1..4)
        master = h.get_feature_report(0x81, 8)
        preset = master[3] + 1 if len(master) >= 4 else 0

        # Input source — байт 1: 0=Analog, 1=Toslink, 2=USB
        source_rep = h.get_feature_report(0x82, 8)
        src = source_rep[1] if len(source_rep) >= 2 else 0
        source_map = {0: "analog", 1: "toslink", 2: "usb"}
        source = source_map.get(src, "unknown")

        h.close()
        return {"preset": preset, "source": source, "available": True}
    except Exception as e:
        print(f"Read error: {e}", file=sys.stderr)
        return {"preset": 0, "source": "error", "available": False}

def process_commands():
    while True:
        if os.path.exists(COMMAND_FILE):
            try:
                with open(COMMAND_FILE, 'r') as f:
                    cmd = json.load(f)
                os.remove(COMMAND_FILE)

                if "preset" in cmd and 1 <= cmd["preset"] <= 4:
                    send_command(0x0B, [cmd["preset"] - 1])
                    time.sleep(0.3)
                if "source" in cmd:
                    src_map = {"analog": 0, "toslink": 1, "usb": 2}
                    if cmd["source"] in src_map:
                        send_command(0x10, [src_map[cmd["source"]]])
                        time.sleep(0.3)
            except Exception as e:
                print(f"Command process error: {e}", file=sys.stderr)
        time.sleep(1)

def main_loop():
    # Запускаем обработчик команд в фоне
    Thread(target=process_commands, daemon=True).start()

    while True:
        status = get_status()
        with open(STATUS_FILE, 'w') as f:
            json.dump(status, f, indent=2)
        print(f"→ {status}")
        time.sleep(8)

if __name__ == "__main__":
    if find_device() is None:
        print("miniDSP 2x4 HD не найден по USB!", file=sys.stderr)
        sys.exit(1)
    main_loop()
