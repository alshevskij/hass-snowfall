"""Snowfall number entities."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.number import NumberEntity, NumberMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    CONF_FLAKE_COUNT,
    CONF_OPACITY,
    CONF_SIZE,
    CONF_SPEED,
    CONF_WIND_GUSTS,
    CONF_WIND_STRENGTH,
    DEFAULTS,
)
from .entity import SnowfallEntityMixin, update_options


@dataclass(frozen=True, slots=True)
class NumberSetting:
    """Description of a numeric Snowfall setting."""

    key: str
    suffix: str
    minimum: int
    maximum: int
    step: int
    icon: str


SETTINGS = (
    NumberSetting(
        CONF_FLAKE_COUNT, "flake_count", 10, 300, 10, "mdi:snowflake"
    ),
    NumberSetting(CONF_SPEED, "speed", 25, 200, 5, "mdi:speedometer"),
    NumberSetting(CONF_SIZE, "size", 25, 200, 5, "mdi:arrow-expand"),
    NumberSetting(CONF_OPACITY, "opacity", 10, 100, 5, "mdi:opacity"),
    NumberSetting(
        CONF_WIND_STRENGTH, "wind_strength", 0, 100, 5, "mdi:weather-windy"
    ),
    NumberSetting(
        CONF_WIND_GUSTS, "wind_gusts", 0, 100, 5, "mdi:weather-windy-variant"
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Snowfall number entities."""
    async_add_entities(SnowfallNumber(entry, setting) for setting in SETTINGS)


class SnowfallNumber(SnowfallEntityMixin, NumberEntity):
    """A numeric Snowfall setting."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG
    _attr_mode = NumberMode.SLIDER

    def __init__(self, entry: ConfigEntry, setting: NumberSetting) -> None:
        """Initialize a numeric setting."""
        self._setting = setting
        self._attr_translation_key = setting.suffix
        self._attr_icon = setting.icon
        self._attr_native_min_value = setting.minimum
        self._attr_native_max_value = setting.maximum
        self._attr_native_step = setting.step
        self._init_snowfall(entry, setting.suffix)

    @property
    def native_value(self) -> float:
        """Return the current setting."""
        value = self._options.get(self._setting.key, DEFAULTS[self._setting.key])
        return float(value)

    async def async_set_native_value(self, value: float) -> None:
        """Persist a new numeric setting."""
        await update_options(
            self.hass,
            self._entry,
            {self._setting.key: int(value)},
        )
