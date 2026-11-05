"""Snowfall select entities."""

from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    CONF_FPS,
    CONF_MODE,
    DEFAULTS,
    FPS_30,
    FPS_60,
    MODE_ALWAYS,
    MODE_CUSTOM,
    MODE_WINTER,
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
    async_add_entities([SnowfallModeSelect(entry), SnowfallFpsSelect(entry)])


class SnowfallModeSelect(SnowfallEntityMixin, SelectEntity):
    """Select the snowfall schedule."""

    _attr_has_entity_name = True
    _attr_translation_key = "mode"
    _attr_entity_category = EntityCategory.CONFIG
    _attr_icon = "mdi:calendar-sync"
    _attr_options = [MODE_WINTER, MODE_ALWAYS, MODE_CUSTOM]

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the mode selector."""
        self._init_snowfall(entry, "mode")

    @property
    def current_option(self) -> str:
        """Return the selected mode."""
        return self._options[CONF_MODE]

    async def async_select_option(self, option: str) -> None:
        """Change the snowfall schedule."""
        await update_options(self.hass, self._entry, {CONF_MODE: option})
        update_month_entities_visibility(self.hass, self._entry)


class SnowfallFpsSelect(SnowfallEntityMixin, SelectEntity):
    """Select the animation frame rate."""

    _attr_has_entity_name = True
    _attr_translation_key = "fps"
    _attr_entity_category = EntityCategory.CONFIG
    _attr_icon = "mdi:motion-play"
    _attr_options = [FPS_30, FPS_60]

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the frame-rate selector."""
        self._init_snowfall(entry, "fps")

    @property
    def current_option(self) -> str:
        """Return the selected frame rate."""
        value = self._options.get(CONF_FPS, DEFAULTS[CONF_FPS])
        return str(value) if str(value) in self.options else FPS_60

    async def async_select_option(self, option: str) -> None:
        """Change the animation frame rate."""
        await update_options(self.hass, self._entry, {CONF_FPS: option})
