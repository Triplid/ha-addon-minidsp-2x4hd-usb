#!/usr/bin/env python3
import hid
import json
import time
import sys
import os

# VID/PID для 2x4 HD
VID = 0x2752
PID = 0x0011

def get_status():
    try:
        h = hid.device()
        h.open(VID, PID)
        
        # Чтение пресета (report 0x81, байт 3: 0-3 -> 1-4)
        master_report = h.get_feature_report(0x81, 8)
        preset = (master_report[3] if len(master_report) > 3 else 0) + 1
        
        # Чтение источника (report 0x82, байт 1: 0=analog, 1=digital)
        source_report = h.get_feature_report(0x82, 8)
        source_num = source_report[1] if len(source_report) > 1 else 0
        source = "analog" if source_num == 0 else "digital"  # Toslink/USB
        
        h.close()
        
        return {"preset": preset, "source": source}
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return {"preset": 0, "source": "error"}

# Основной цикл: обновляем JSON каждые 10 сек
while True:
    status = get_status()
    with open('/share/minidsp_status.json', 'w') as f:
        json.dump(status, f)
    time.sleep(10)