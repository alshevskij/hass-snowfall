# ❄️ Snowfall for Home Assistant

Bring a winter atmosphere to your Home Assistant dashboard!

Snowfall is a custom integration that adds an animated snowfall effect directly to the Home Assistant frontend. Customize the effect, control it manually, or let Home Assistant automations decide when the snow should appear.

<p align="center">
  <a href="README.md">🇷🇺 Русский</a> · <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.10.1-blue" alt="Version">
  <img src="https://img.shields.io/badge/HACS-Custom%20Repository-41BDF5" alt="HACS">
  <img src="https://img.shields.io/github/license/alshevskij/hass-snowfall" alt="License">
  <img src="https://img.shields.io/github/stars/alshevskij/hass-snowfall?style=flat" alt="GitHub Stars">
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=alshevskij&repository=hass-snowfall&category=integration">
    <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Add Snowfall to Home Assistant via HACS">
  </a>
</p>

> **IMPORTANT!:** This integration was put together quite informally for my own personal use. It’s based on a simple script I had saved alongside my Home Assistant setup, which was previously controlled by a basic on/off toggle. I decided to take it a step further by building a proper environment around the script and adding more flexible visual settings—going well beyond just a simple on/off switch. Please note that this integration hasn’t undergone full-scale testing; as a result, you might encounter issues with how the snow is rendered, the performance or battery life of the devices running the animation, or other unforeseen glitches. Rest assured, any bugs or issues that arise will be addressed as needed.

> I plan to actively develop this integration further—moving beyond just snow animations to include other features, such as customizable colors and much more!✨

---

## Features

- Animated snowfall directly in the Home Assistant frontend.
- Manual control through a dedicated switch.
- Three operating modes: Always, Winter, and Custom.
- Adjustable snowflake count, speed, size, and opacity.
- Exclude specific dashboard pages from the effect.
- Configure the integration through the Home Assistant UI.
- Use native Home Assistant automations to control the snowfall schedule.

## Installation

### Via HACS

1. Make sure HACS is installed in Home Assistant.
2. Click the blue **Add to Home Assistant** button above.
3. Your Home Assistant instance will open the Snowfall repository in HACS.
4. Confirm adding the custom repository if prompted.
5. Find Snowfall in HACS and install the integration.
6. Restart Home Assistant.

If the button does not work, add the repository manually:

`https://github.com/alshevskij/hass-snowfall`

Select **Integration** as the category in HACS.

### Manual installation

1. Download this repository.
2. Copy the `custom_components/snowfall` directory into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

## Configuration

After restarting Home Assistant:

1. Go to **Settings → Devices & services**.
2. Click **Add integration**.
3. Search for **Snowfall for Home Assistant**.
4. Complete the setup.

Additional options are available in the integration settings.

### Snowfall settings

| Setting | Description |
|---|---|
| Operating mode | Always, Winter, or Custom |
| Active months | Select months for Custom mode |
| Snowflake count | 10–300 |
| Speed | 25–200 |
| Size | 25–200 |
| Opacity | 10–100 |
| Excluded paths | Pages where snowfall is hidden |

Enter excluded paths one per line.

## Operating modes

- **Always** — snowfall is allowed throughout the year.
- **Winter** — snowfall is allowed from December through February.
- **Custom** — snowfall is allowed only during selected months.

## Home Assistant control

The integration creates a switch entity:

`switch.snowfall`

Use it to enable or disable snowfall manually, add it to your dashboard, or control it through scripts and automations.

### You don't have to use Snowfall's seasonal scheduling

You can skip the built-in monthly and winter scheduling entirely.

Simply select **Always** and let Home Assistant handle the schedule through its native automations.

Automate `switch.snowfall` to:

- Enable snowfall on a specific date.
- Disable it when winter ends.
- Start snowfall at sunset.
- Show snow only when someone is at home.
- Use any other conditions and scenarios.

Snowfall handles the visual effect, while Home Assistant controls when it runs.

Documentation: [Home Assistant Automations](https://www.home-assistant.io/docs/automation/).

## Support

Found a bug or have a feature request?

[Open a GitHub Issue](https://github.com/alshevskij/hass-snowfall/issues).

## License

See the [LICENSE](LICENSE) file.
