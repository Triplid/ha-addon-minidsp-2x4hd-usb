# HA Add-on: MiniDSP 2x4 HD USB

## Installation
1. Add repo to HA: Settings > Add-ons > Store > Repositories > https://github.com/ТВОЙ_ЛОГИН/ha-addon-minidsp-2x4hd
2. Install "MiniDSP 2x4 HD USB (Presets & Source)".
3. Start add-on.

## configuration.yaml
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
