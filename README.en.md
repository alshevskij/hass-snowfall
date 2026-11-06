# ❄️ Snowfall for Home Assistant

Add a winter atmosphere to your Home Assistant control panel!✨

Snowfall is a custom integration that adds an animated falling snow effect directly to the Home Assistant interface. Control the snowfall and all its parameters via the standard Home Assistant entities — no YAML and no separate integration settings window.

<p align="center">
 <a href="README.md">🇷🇺 Russian</a> · <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.11.4-blue" alt="Version">
  <img src="https://img.shields.io/badge/HACS-Custom%20Repository-41BDF5" alt="HACS">
  <img src="https://img.shields.io/github/license/alshevskij/hass-snowfall" alt="License">
  <img src="https://img.shields.io/github/stars/alshevskij/hass-snowfall?style=flat" alt="GitHub Stars">
</p>

## Current integration capabilities:

- Animated snow directly in the Home Assistant interface (on absolutely any page).
- A switch to turn snowfall on and off.
- Three built‑in operating modes: **New Year’s** (snow falls only from December to February), **Year‑round** and **Month selection**.
- 12 separate switches for each month of the year, numbered from 1 to 12. They are active and used only in the **Month selection** mode.
- Setting the number, speed, size, transparency and appearance of snowflakes.
- Four snowfall presets: light, normal, heavy and blizzard. Presets adjust overall intensity without overwriting manual slider values.
- Four snowflake styles: dots, six-armed snowflakes, crystals and mixed.
- Customizable wind: strength, direction and gusts; wind affects each snowflake's horizontal trajectory.
- Limiting the rendering frequency: 30, 60, 90 or 120 frames per second.
- A **whitelist** of pages where snowfall is allowed.
- **Blacklist** of pages where snowfall is prohibited.

## Integration installation:

### Via HACS / Marketplace (recommended)

1. Make sure HACS is installed in Home Assistant.
2. Click the button below <p>
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=alshevskij&repository=hass-snowfall&category=integration">
    <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Add Snowfall to Home Assistant via HACS">
  </a>
</p>

3. Confirm the addition of the custom repository.
4. Find Snowfall and install the integration.
5. Restart Home Assistant.

If the button didn’t work, add the repository manually using the link:

`https://github.com/alshevskij/hass-snowfall`

In HACS, select the **Integration** category.

### Manual installation

1. Download the repository.
2. Copy the `custom_components/snowfall` folder to the `custom_components` directory of your Home Assistant.
3. Restart Home Assistant.

## Devices and settings profiles

The integration creates three logical Home Assistant devices:

- **Snowfall** — global controls: enable/disable the effect, snowfall schedule, device settings mode, and page allow/block lists.
- **Snowfall Desktop** — visual settings for computers: flake count, speed, size and opacity, appearance, intensity preset, wind, and FPS.
- **Snowfall Mobile** — an independent set of the same visual settings for phones and tablets.

The **Separate device settings** switch controls the profile mode:

- **Off** — every browser uses the Snowfall Desktop profile. Snowfall Mobile controls are automatically hidden, while their saved values are preserved.
- **On** — computers use Snowfall Desktop, while phones and tablets use Snowfall Mobile. The client type is detected in the browser.

During the update, existing visual settings are migrated to the Desktop profile. Existing entity IDs are preserved, so previously configured cards and automations should not need to be rebuilt. A separate Mobile profile is initialized with default values.

Desktop and Mobile profile diagnostic sensors are visible in the standard entity list and expose the configuration attributes consumed by the integration's JavaScript renderer.

## Configuration and integration entities:

The main snowfall switch, added in version 2026.10.1, retains the previous ID `switch.snowfall`.
Starting with version 2026.11.3, standard entities for managing the integration are created automatically. Version 2026.11.4 adds separate Desktop and Mobile profiles and improves the visibility and ordering of diagnostic sensors and month switches.

| Entity | Purpose |
|---|---|
| `switch.snowfall` | Turning snowfall on and off |
| Mode switch | New Year’s, year‑round, or month selection |
| 12 month switches | Selection of active months (active only in month selection mode) |
| Numerical quantity setting | Number of snowflakes: 10–300 |
| Numerical speed setting | Falling speed: 25–200 |
| Numerical size setting | Snowflake size: 25–200 |
| Numerical transparency setting | Transparency: 10–100 |
| Frame rate selection | 30, 60, 90 or 120 FPS |
| Snowflake appearance | Dots, six-armed snowflakes, crystals or mixed |
| Snowfall preset | Light, normal, heavy or blizzard |
| Wind strength | 0–100 |
| Wind direction | Left, right or variable |
| Wind gusts | 0–100 |
| Blacklist text entity | Pages where snowfall is prohibited |
| Whitelist text entity | Pages where snowfall is allowed |

### What has changed:

In version 2026.11.4:
- Independent visual settings profiles for Desktop and Mobile have been added. When separate mode is off, all clients use the Desktop profile; when enabled, computers use Desktop while phones and tablets use Mobile.
- Existing visual settings are automatically migrated to the Desktop profile during the update. Mobile values are preserved when separate mode is disabled.
- Desktop and Mobile profile diagnostic sensors are visible in the standard entity list and expose profile attributes to the frontend.
- Month switches now include ordinal numbers for consistent ordering: 1. January through 12. December.

In version 2026.11.3, snowfall control has been moved to a full set of Home Assistant entities (the original control was implemented via integration settings, which turned out to be very inconvenient)

- Separate entities have been added for the operating mode and frame rate.
- Numerical settings for the number, speed, size, and transparency of snowflakes have been added.
- Switches have been added for each of the 12 months. They are automatically hidden (become inactive) in the **New Year** and **Year‑round** modes, and become available in the **Month Selection** mode. The selected months are saved when changing the mode.
- A whitelist of pages has been added in addition to the already existing blacklist.
- Added snowflake appearance styles: dots, six-armed snowflakes, crystals and mixed.
- Added snowfall intensity presets. They scale particle density and animation speed without overwriting manual slider values.
- Added wind physics: direction, strength and gusts affect the horizontal movement of each snowflake.
- A rendering frequency limit of 30/60/90/120 FPS has been added to control rendering performance and power consumption on devices displaying the snowfall.
- Previously saved parameters from Options Flow are transferred to new entities during an update, so your existing settings should not be reset.

## White and black lists of pages:

In text entities, specify page paths separated by a semicolon or a comma. For example:

`/lovelace/home; /lovelace/lights; /config/dashboard`

You can also use commas:

`/lovelace/home, /lovelace/lights`

Specify a path starting with `/`, without a domain, query parameters, or URL fragment.

- **The whitelist is empty** — snowfall is allowed on all pages except those listed in the blacklist.
- **The whitelist is full** — snowfall is allowed only on matching pages.
- **The blacklist** excludes the specified pages from the effect.
- If the path matches both lists, the blacklist always takes priority: snowfall is not displayed on this page.
- The matching takes into account nested pages: the rule `/lovelace` also applies to `/lovelace/room`.

Each Home Assistant text entity is limited to 255 characters. If the list is large, use shorter paths.

## Control via automations:

All integration entities, of course, can be added to your panels and used to create convenient cards for managing parameters, for example:

<img width="495" height="632" alt="3" src="https://github.com/user-attachments/assets/3dd15153-081a-4f83-a2a4-ae4844330372" />

You can also use it in automations; for example, you can enable `switch.snowfall` on a schedule, change the mode depending on the season, or switch animation parameters. If you want to fully manage the snowfall schedule using Home Assistant, select the **Year‑Round** mode, and let the automations handle turning the effect on and off.

Documentation: [Home Assistant Automations](https://www.home-assistant.io/docs/automation/).

## Support

Found an error or want to suggest a new feature?

[Create an Issue on GitHub](https://github.com/alshevskij/hass-snowfall/issues).

## License

The project is distributed under the license specified in the [LICENSE](LICENSE) file.
