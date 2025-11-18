# HA Add-on: MiniDSP 2x4 HD USB

Custom add-on for controlling miniDSP 2x4 HD via USB (presets and source only).

## Installation
1. Add this repo to HA Add-on Store: Settings > Add-ons > Store > Repositories > https://github.com/Triplid/ha-addon-minidsp-2x4hd-usb
2. Install "MiniDSP 2x4 HD USB (Presets & Source)".
3. Start the add-on.

## Usage
- Outputs `/share/minidsp_status.json` with `{"preset": 2, "source": "analog"}` every 10s.
- Add sensors to `configuration.yaml` (see below).

## configuration.yaml example
```yaml
sensor:
  - platform: file
    name: "MiniDSP Preset"
    file_path: "/share/minidsp_status.json"
    value_template: "{{ value_json.preset | int(0) }}"
    icon: mdi:numeric-1-2-3

  - platform: template
    sensors:
      minidsp_source:
        friendly_name: "MiniDSP Source"
        value_template: >-
          {% set s = state_attr('sensor.minidsp_preset', 'source') %}
          {% if s == 'analog' %}Analog{% elif s == 'digital' %}Toslink/USB{% else %}Error{% endif %}
        icon_template: mdi:swap-horizontal
