"""Snowfall select entities."""

from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    CONF_FLAKE_STYLE,
    CONF_FPS,
    CONF_MODE,
    CONF_PRESET,
    CONF_WIND_DIRECTION,
    DEFAULTS,
    DEVICE_DESKTOP,
    DEVICE_MOBILE,
    FLAKE_STYLE_CRYSTALS,
    FLAKE_STYLE_DOTS,
    FLAKE_STYLE_MIXED,
    FLAKE_STYLE_SNOWFLAKES,
    FPS_30,
    FPS_60,
    FPS_90,
    FPS_120,
    MODE_ALWAYS,
    MODE_CUSTOM,
    MODE_WINTER,
    PRESET_BLIZZARD,
    PRESET_HEAVY,
    PRESET_LIGHT,
    PRESET_NORMAL,
    WIND_LEFT,
    WIND_RIGHT,
    WIND_VARIABLE,
)
from .entity import (
    SnowfallEntityMixin,
    update_month_entities_visibility,
    update_options,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up global and profile-specific selectors."""
    async_add_entities(
        [
            SnowfallModeSelect(entry),
            ProfileSelect(entry, CONF_FPS, "fps", [FPS_30, FPS_60, FPS_90, FPS_120], DEVICE_DESKTOP),
            ProfileSelect(entry, CONF_FLAKE_STYLE, "flake_style", [FLAKE_STYLE_DOTS, FLAKE_STYLE_SNOWFLAKES, FLAKE_STYLE_CRYSTALS, FLAKE_STYLE_MIXED], DEVICE_DESKTOP),
            ProfileSelect(entry, CONF_PRESET, "preset", [PRESET_LIGHT, PRESET_NORMAL, PRESET_HEAVY, PRESET_BLIZZARD], DEVICE_DESKTOP),
            ProfileSelect(entry, CONF_WIND_DIRECTION, "wind_direction", [WIND_LEFT, WIND_RIGHT, WIND_VARIABLE], DEVICE_DESKTOP),
            ProfileSelect(entry, CONF_FPS, "fps", [FPS_30, FPS_60, FPS_90, FPS_120], DEVICE_MOBILE),
            ProfileSelect(entry, CONF_FLAKE_STYLE, "flake_style", [FLAKE_STYLE_DOTS, FLAKE_STYLE_SNOWFLAKES, FLAKE_STYLE_CRYSTALS, FLAKE_STYLE_MIXED], DEVICE_MOBILE),
            ProfileSelect(entry, CONF_PRESET, "preset", [PRESET_LIGHT, PRESET_NORMAL, PRESET_HEAVY, PRESET_BLIZZARD], DEVICE_MOBILE),
            ProfileSelect(entry, CONF_WIND_DIRECTION, "wind_direction", [WIND_LEFT, WIND_RIGHT, WIND_VARIABLE], DEVICE_MOBILE),
        ]
    )


class SnowfallSelectBase(SnowfallEntityMixin, SelectEntity):
    """Base class for Snowfall selectors."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, entry: ConfigEntry, key: str, suffix: str) -> None:
        self._option_key = key
        self._attr_translation_key = suffix
        self._init_snowfall(entry, suffix)

    @property
    def current_option(self) -> str:
        value = str(self._options.get(self._option_key, DEFAULTS[self._option_key]))
        return value if value in self.options else str(DEFAULTS[self._option_key])

    async def async_select_option(self, option: str) -> None:
        await update_options(self.hass, self._entry, {self._option_key: option})


class SnowfallModeSelect(SnowfallSelectBase):
    """Select the global snowfall schedule."""

    _attr_icon = "mdi:calendar-sync"
    _attr_options = [MODE_WINTER, MODE_ALWAYS, MODE_CUSTOM]

    def __init__(self, entry: ConfigEntry) -> None:
        super().__init__(entry, CONF_MODE, "mode")

    async def async_select_option(self, option: str) -> None:
        await super().async_select_option(option)
        update_month_entities_visibility(self.hass, self._entry)


class ProfileSelect(SnowfallEntityMixin, SelectEntity):
    """A selector belonging to a device-specific visual profile."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(
        self,
        entry: ConfigEntry,
        key: str,
        suffix: str,
        options: list[str],
        device_role: str,
    ) -> None:
        self._option_key = f"{device_role}_{key}"
        self._attr_translation_key = suffix
        self._attr_icon = {
            "fps": "mdi:motion-play",
            "flake_style": "mdi:snowflake",
            "preset": "mdi:weather-snowy",
            "wind_direction": "mdi:weather-windy",
        }[suffix]
        self._attr_options = options
        unique_suffix = suffix if device_role == DEVICE_DESKTOP else f"mobile_{suffix}"
        self._init_snowfall(entry, unique_suffix, device_role)

    @property
    def current_option(self) -> str:
        value = str(self._options.get(self._option_key, DEFAULTS[self._option_key.removeprefix("desktop_").removeprefix("mobile_")]))
        return value if value in self.options else str(self.options[0])

    async def async_select_option(self, option: str) -> None:
        await update_options(self.hass, self._entry, {self._option_key: option})
