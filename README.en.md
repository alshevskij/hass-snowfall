# ❄️ Snowfall for Home Assistant

Bring a winter atmosphere to your Home Assistant dashboard!

Snowfall is a custom integration that adds an animated snowfall effect directly to the Home Assistant frontend. Control the effect through native Home Assistant entities, use automations, and adjust its appearance without YAML.

<p align="center">
  <a href="README.md">🇷🇺 Русский</a> · <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.11.1-blue" alt="Version">
  <img src="https://img.shields.io/badge/HACS-Custom%20Repository-41BDF5" alt="HACS">
  <img src="https://img.shields.io/github/license/alshevskij/hass-snowfall" alt="License">
  <img src="https://img.shields.io/github/stars/alshevskij/hass-snowfall?style=flat" alt="GitHub Stars">
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=alshevskij&repository=hass-snowfall&category=integration">
    <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Add Snowfall to Home Assistant via HACS">
  </a>
</p>

---

## Features

- Animated snowfall directly in the Home Assistant frontend.
- A dedicated switch to enable or disable the effect.
- Three modes: Winter season (December–February), All year, and Custom months.
- Individual switches for all 12 months.
- Adjustable snowflake count, speed, size, and opacity.
- Rendering frame-rate limit: 30 or 60 FPS.
- Allowlist of dashboard pages where snowfall is permitted.
- Blocklist of dashboard pages where snowfall is disabled.
- All settings are exposed as native Home Assistant entities and can be used in automations.

## Installation

### Via HACS

1. Make sure HACS is installed in Home Assistant.
2. Click the **Add to Home Assistant** button above.
3. Open the Snowfall repository in HACS and confirm adding the custom repository if prompted.
4. Find Snowfall and install the integration.
5. Restart Home Assistant.

If the button does not work, add the repository manually:

`https://github.com/alshevskij/hass-snowfall`

Select **Integration** as the category in HACS.

### Manual installation

1. Download this repository.
2. Copy `custom_components/snowfall` into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

## Configuration and entities

After adding the integration, open **Settings → Devices & services → Snowfall**. The integration creates these entities:

| Entity | Purpose |
|---|---|
| `switch.snowfall` | Enable or disable snowfall |
| `select.snowfall_mode` | Winter, All year, or Custom months |
| `switch.snowfall_january` … `switch.snowfall_december` | Select active months |
| `number.snowfall_flake_count` | Snowflake count: 10–300 |
| `number.snowfall_speed` | Speed: 25–200 |
| `number.snowfall_size` | Size: 25–200 |
| `number.snowfall_opacity` | Opacity: 10–100 |
| `select.snowfall_fps` | Rendering rate: 30 or 60 FPS |
| `text.snowfall_excluded_paths` | Blocklist of pages |
| `text.snowfall_included_paths` | Allowlist of pages |

### Operating modes

- **Winter season** — snowfall is active from December through February.
- **All year** — snowfall is allowed throughout the year.
- **Custom months** — snowfall is active only in months whose switches are enabled.

Month switches affect scheduling only in **Custom months** mode.

### Page allowlist and blocklist

Enter paths separated by semicolons, for example:

`/lovelace/home; /lovelace/lights`

- If the allowlist is empty, snowfall is allowed on every page except those in the blocklist.
- If the allowlist is not empty, snowfall is allowed only on matching pages.
- If a path matches both lists, the blocklist wins and snowfall is hidden.
- Matching includes nested pages: `/lovelace` also matches `/lovelace/room`.

Each Home Assistant text entity is limited to 255 characters. Keep paths concise for longer lists.

### Automations

All entities can be added to dashboards and used in scripts and automations. For example, schedule `switch.snowfall`, change the mode by season, or reduce FPS on less powerful devices.

Documentation: [Home Assistant Automations](https://www.home-assistant.io/docs/automation/).

## Support

Found a bug or have a feature request?

[Open a GitHub Issue](https://github.com/alshevskij/hass-snowfall/issues).

## License

See the [LICENSE](LICENSE) file.
