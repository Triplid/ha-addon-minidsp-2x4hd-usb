# Home Assistant Add-on: miniDSP 2x4 HD USB Control

## Installation
1. Add this repo to HA Add-on Store: Settings > Add-ons > Add-on Store > Three dots > Repositories > Add `https://github.com/ТВОЙ_ЛОГИН/ha-addon-minidsp-2x4hd-usb`
2. Install and start the add-on.
3. Add sensors to `configuration.yaml` (see below).

## Usage
- Creates `/share/minidsp_status.json` with `{"preset": 2, "source": "analog"}`
- Sensors: `sensor.minidsp_preset` and `sensor.minidsp_source`

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
          {% set s = states('sensor.minidsp_preset') %}
          {% if s != 'error' %}{{ state_attr('sensor.minidsp_preset', 'source') }}{% else %}error{% endif %}
        icon_template: >-
          {% if state == 'analog' %}mdi:analog{% elif 'tos' in state %}mdi:swap-horizontal-variant{% else %}mdi:usb{% endif %}
