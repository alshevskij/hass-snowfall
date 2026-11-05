# ❄️ Snowfall for Home Assistant

Bring a winter atmosphere to your Home Assistant dashboard!

Snowfall is a custom integration that adds an animated snowfall effect directly to the Home Assistant frontend. Control the effect and all its settings through native Home Assistant entities — no YAML and no separate Options Flow required.

<p align="center">
  <a href="README.md">🇷🇺 Русский</a> · <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.11.2-blue" alt="Version">
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
- Three operating modes: **Winter season** (December–February), **All year**, and **Custom months**.
- 12 individual month switches, shown only in **Custom months** mode.
- Adjustable snowflake count, fall speed, size, and opacity.
- Rendering frame-rate limit: 30 or 60 FPS.
- An **allowlist** of pages where snowfall is permitted.
- A **blocklist** of pages where snowfall is disabled.
- All settings are exposed as native Home Assistant entities and can be used on dashboards, in scripts, and in automations.
- All entities are grouped under a single **Snowfall** device.
- Settings are available directly in the integration device. No YAML or legacy Options Flow is needed to adjust them.

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

After adding the integration, open **Settings → Devices & services → Snowfall → Device**. The device contains the main snowfall switch and all integration settings.

The main switch keeps its existing entity ID, `switch.snowfall`. The remaining entities are created automatically:

| Entity | Purpose |
|---|---|
| `switch.snowfall` | Enable or disable snowfall |
| Mode selector | Winter season, All year, or Custom months |
| 12 month switches | Select active months; visible only in Custom months mode |
| Snowflake count control | Snowflake count: 10–300 |
| Speed control | Fall speed: 25–200 |
| Size control | Snowflake size: 25–200 |
| Opacity control | Opacity: 10–100 |
| Frame-rate selector | 30 or 60 FPS |
| Blocklist text entity | Pages where snowfall is disabled |
| Allowlist text entity | Pages where snowfall is permitted |

Entity names follow your Home Assistant language. All entities are grouped under one **Snowfall** device, whose model is **Home Assistant FX**.

### What's new

This version replaces the old integration options screen with a complete set of native Home Assistant entities:

- Integration settings are now adjusted using switches, selectors, number controls, and text entities directly in the Snowfall device.
- Added dedicated entities for the operating mode and frame rate.
- Added number controls for snowflake count, speed, size, and opacity.
- Added individual switches for all 12 months. They are automatically hidden in **Winter season** and **All year** modes and become available in **Custom months** mode. Selected months are preserved when changing modes.
- Added a page allowlist alongside the existing blocklist.
- Added a 30/60 FPS rendering limit.
- Grouped all entities under one device and updated its model name to **Home Assistant FX**.
- Previously saved Options Flow values are migrated to initialize the new entities, so existing settings should be preserved when upgrading.

## Operating modes

- **Winter season** — snowfall is allowed from December through February.
- **All year** — snowfall is allowed throughout the year.
- **Custom months** — snowfall is allowed only in months whose switches are enabled.

Month switches are automatically hidden in **Winter season** and **All year** modes, and shown when **Custom months** is selected. Saved month settings are preserved when switching modes.

## Page allowlist and blocklist

Enter page paths in the text entities, separated by semicolons or commas. For example:

`/lovelace/home; /lovelace/lights; /config/dashboard`

Commas are also supported:

`/lovelace/home, /lovelace/lights`

Use paths beginning with `/`; do not include the domain, query parameters, or URL fragment.

- **Empty allowlist** — snowfall is allowed on every page except those in the blocklist.
- **Non-empty allowlist** — snowfall is allowed only on matching pages.
- The **blocklist** always excludes matching pages from the effect.
- If a path matches both lists, the blocklist takes priority and snowfall is hidden on that page.
- Matching includes nested pages: the rule `/lovelace` also matches `/lovelace/room`.

Each Home Assistant text entity is limited to 255 characters. Use concise paths for longer lists.

## Automations

All entities can be added to dashboards and used in scripts and automations. For example, schedule `switch.snowfall`, change the operating mode by season, or adjust animation settings automatically.

To manage the schedule entirely through Home Assistant, select **All year** mode and let automations turn the effect on and off.

Documentation: [Home Assistant Automations](https://www.home-assistant.io/docs/automation/).

## Support

Found a bug or have a feature request?

[Open a GitHub Issue](https://github.com/alshevskij/hass-snowfall/issues).

## License

See the [LICENSE](LICENSE) file.
