# MiniDSP 2x4 HD USB Add-on for Home Assistant

This add-on allows USB control of miniDSP 2x4 HD presets and source selection in Home Assistant.

## Features
- Read current preset (1-4) and source (analog/digital) status
- Automatic status updates to shared file
- USB HID communication with miniDSP

## Installation
1. Add this repository in Home Assistant: 
   `https://github.com/Triplid/ha-addon-minidsp-2x4hd-usb`
2. Install the "MiniDSP 2x4 HD USB" add-on
3. Configure update interval if needed (default: 10 seconds)
4. Start the add-on

## Usage
The add-on writes status to `/share/minidsp_status.json` with format:
```json
{
  "preset": 1,
  "source": "analog",
  "error": null
}
