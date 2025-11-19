#!/usr/bin/env python3
import hid
import sys
import json

VID = 0x2752
PID = 0x0011

def set_preset(preset_num):
    """Установить пресет (1-4)"""
    try:
        with hid.Device(VID, PID) as h:
            # Пресеты: 0-3 соответствуют 1-4
            preset_byte = max(0, min(3, preset_num - 1))
            report = bytes([0x01, 0x08, 0x00, preset_byte] + [0x00]*4)
            h.send_feature_report(report)
            print(f"Preset set to: {preset_num}")
            return True
    except Exception as e:
        print(f"Error setting preset: {e}", file=sys.stderr)
        return False

def set_source(source):
    """Установить источник: 'analog' или 'digital'"""
    try:
        with hid.Device(VID, PID) as h:
            source_byte = 0 if source == "analog" else 1
            report = bytes([0x02, 0x08, source_byte] + [0x00]*5)
            h.send_feature_report(report)
            print(f"Source set to: {source}")
            return True
    except Exception as e:
        print(f"Error setting source: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "preset" and len(sys.argv) > 2:
            success = set_preset(int(sys.argv[2]))
            sys.exit(0 if success else 1)
            
        elif command == "source" and len(sys.argv) > 2:
            success = set_source(sys.argv[2])
            sys.exit(0 if success else 1)
            
        elif command == "status":
            # Простой статус для проверки
            try:
                with hid.Device(VID, PID) as h:
                    print("MiniDSP connected successfully")
                    sys.exit(0)
            except Exception as e:
                print(f"MiniDSP connection failed: {e}")
                sys.exit(1)
                
        else:
            print("Usage:")
            print("  minidsp_control.py preset <1-4>")
            print("  minidsp_control.py source <analog|digital>")
            print("  minidsp_control.py status")
            sys.exit(1)
