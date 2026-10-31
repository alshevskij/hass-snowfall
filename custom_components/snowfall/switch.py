
"""Snowfall switch entity."""

from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from .const import (
    CONF_EXCLUDED_PATHS,
    CONF_FLAKE_COUNT,
    CONF_MODE,
    CONF_MONTHS,
    CONF_OPACITY,
    CONF_SIZE,
    CONF_SPEED,
    DEFAULTS,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Snowfall switch."""

    async_add_entities([SnowfallSwitch(entry)])


class SnowfallSwitch(RestoreEntity, SwitchEntity):
    """A switch that controls the global snowfall effect."""

    _attr_has_entity_name = True
    _attr_translation_key = "snowfall"
    _attr_icon = "mdi:snowflake"
    _attr_is_on = False

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the Snowfall switch."""

        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_enabled"

    async def async_added_to_hass(self) -> None:
        """Restore the previous switch state."""

        await super().async_added_to_hass()

        if (last_state := await self.async_get_last_state()) is not None:
            self._attr_is_on = last_state.state == "on"

    @property
    def extra_state_attributes(self) -> dict:
        """Expose current animation options to the browser module."""

        options = {**DEFAULTS, **self._entry.options}

        return {
            CONF_MODE: options[CONF_MODE],
            CONF_MONTHS: options[CONF_MONTHS],
            CONF_EXCLUDED_PATHS: options[CONF_EXCLUDED_PATHS],
            CONF_FLAKE_COUNT: options[CONF_FLAKE_COUNT],
            CONF_SPEED: options[CONF_SPEED],
            CONF_SIZE: options[CONF_SIZE],
            CONF_OPACITY: options[CONF_OPACITY],
        }

    async def async_turn_on(self, **kwargs) -> None:
        """Enable snowfall."""

        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        """Disable snowfall."""

        self._attr_is_on = False
        self.async_write_ha_state()
