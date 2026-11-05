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
    FLAKE_STYLE_CRYSTALS,
    FLAKE_STYLE_DOTS,
    FLAKE_STYLE_MIXED,
    FLAKE_STYLE_SNOWFLAKES,
    FPS_30,
    FPS_60,
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
    """Set up Snowfall select entities."""
    async_add_entities(
        [
            SnowfallModeSelect(entry),
            SnowfallFpsSelect(entry),
            SnowfallFlakeStyleSelect(entry),
            SnowfallPresetSelect(entry),
            SnowfallWindDirectionSelect(entry),
        ]
    )


class SnowfallSelectBase(SnowfallEntityMixin, SelectEntity):
    """Base class for Snowfall selectors."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, entry: ConfigEntry, key: str) -> None:
        """Initialize a selector."""
        self._init_snowfall(entry, key)

    def _current(self, key: str) -> str:
        """Return a valid saved option or its default."""
        value = str(self._options.get(key, DEFAULTS[key]))
        return value if value in self.options else str(DEFAULTS[key])

    async def _select(self, key: str, option: str) -> None:
        """Persist a selected option."""
        await update_options(self.hass, self._entry, {key: option})


class SnowfallModeSelect(SnowfallSelectBase):
    """Select the snowfall schedule."""

    _attr_translation_key = "mode"
    _attr_icon = "mdi:calendar-sync"
    _attr_options = [MODE_WINTER, MODE_ALWAYS, MODE_CUSTOM]

    def __init__(self, entry: ConfigEntry) -> None:
        super().__init__(entry, CONF_MODE)

    @property
    def current_option(self) -> str:
        return self._current(CONF_MODE)

    async def async_select_option(self, option: str) -> None:
        await self._select(CONF_MODE, option)
        update_month_entities_visibility(self.hass, self._entry)


class SnowfallFpsSelect(SnowfallSelectBase):
    """Select the animation frame rate."""

    _attr_translation_key = "fps"
    _attr_icon = "mdi:motion-play"
    _attr_options = [FPS_30, FPS_60]

    def __init__(self, entry: ConfigEntry) -> None:
        super().__init__(entry, CONF_FPS)

    @property
    def current_option(self) -> str:
        return self._current(CONF_FPS)

    async def async_select_option(self, option: str) -> None:
        await self._select(CONF_FPS, option)


class SnowfallFlakeStyleSelect(SnowfallSelectBase):
    """Select the snowflake drawing style."""

    _attr_translation_key = "flake_style"
    _attr_icon = "mdi:snowflake"
    _attr_options = [
        FLAKE_STYLE_DOTS,
        FLAKE_STYLE_SNOWFLAKES,
        FLAKE_STYLE_CRYSTALS,
        FLAKE_STYLE_MIXED,
    ]

    def __init__(self, entry: ConfigEntry) -> None:
        super().__init__(entry, CONF_FLAKE_STYLE)

    @property
    def current_option(self) -> str:
        return self._current(CONF_FLAKE_STYLE)

    async def async_select_option(self, option: str) -> None:
        await self._select(CONF_FLAKE_STYLE, option)


class SnowfallPresetSelect(SnowfallSelectBase):
    """Select a snowfall intensity preset."""

    _attr_translation_key = "preset"
    _attr_icon = "mdi:weather-snowy"
    _attr_options = [
        PRESET_LIGHT,
        PRESET_NORMAL,
        PRESET_HEAVY,
        PRESET_BLIZZARD,
    ]

    def __init__(self, entry: ConfigEntry) -> None:
        super().__init__(entry, CONF_PRESET)

    @property
    def current_option(self) -> str:
        return self._current(CONF_PRESET)

    async def async_select_option(self, option: str) -> None:
        await self._select(CONF_PRESET, option)


class SnowfallWindDirectionSelect(SnowfallSelectBase):
    """Select the direction of horizontal wind."""

    _attr_translation_key = "wind_direction"
    _attr_icon = "mdi:weather-windy"
    _attr_options = [WIND_LEFT, WIND_RIGHT, WIND_VARIABLE]

    def __init__(self, entry: ConfigEntry) -> None:
        super().__init__(entry, CONF_WIND_DIRECTION)

    @property
    def current_option(self) -> str:
        return self._current(CONF_WIND_DIRECTION)

    async def async_select_option(self, option: str) -> None:
        await self._select(CONF_WIND_DIRECTION, option)
