"""Snowfall switch entities."""

from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from .const import (
    CONF_EXCLUDED_PATHS,
    CONF_FLAKE_COUNT,
    CONF_FPS,
    CONF_INCLUDED_PATHS,
    CONF_MODE,
    CONF_MONTHS,
    CONF_OPACITY,
    CONF_SIZE,
    CONF_SPEED,
    DEFAULTS,
    MONTHS,
)
from .entity import SnowfallEntityMixin, update_options


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Snowfall switches."""
    entities = [SnowfallSwitch(entry)]
    entities.extend(SnowfallMonthSwitch(entry, month) for month in MONTHS)
    async_add_entities(entities)


class SnowfallSwitch(SnowfallEntityMixin, RestoreEntity, SwitchEntity):
    """Main switch that controls the global snowfall effect."""

    _attr_has_entity_name = True
    _attr_translation_key = "snowfall"
    _attr_icon = "mdi:snowflake"

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the main switch."""
        self._init_snowfall(entry, "enabled")
        self._attr_is_on = False

    async def async_added_to_hass(self) -> None:
        """Restore the previous switch state."""
        await super().async_added_to_hass()
        if (last_state := await self.async_get_last_state()) is not None:
            self._attr_is_on = last_state.state == "on"

    @property
    def extra_state_attributes(self) -> dict:
        """Expose current animation settings to the frontend module."""
        options = {**DEFAULTS, **self._entry.options}
        return {
            CONF_MODE: options[CONF_MODE],
            CONF_MONTHS: options[CONF_MONTHS],
            CONF_EXCLUDED_PATHS: options[CONF_EXCLUDED_PATHS],
            CONF_INCLUDED_PATHS: options[CONF_INCLUDED_PATHS],
            CONF_FLAKE_COUNT: options[CONF_FLAKE_COUNT],
            CONF_SPEED: options[CONF_SPEED],
            CONF_SIZE: options[CONF_SIZE],
            CONF_OPACITY: options[CONF_OPACITY],
            CONF_FPS: options[CONF_FPS],
        }

    async def async_turn_on(self, **kwargs) -> None:
        """Enable snowfall."""
        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        """Disable snowfall."""
        self._attr_is_on = False
        self.async_write_ha_state()


class SnowfallMonthSwitch(SnowfallEntityMixin, SwitchEntity):
    """Switch for an individual active month."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:calendar-month"

    def __init__(self, entry: ConfigEntry, month: int) -> None:
        """Initialize a month switch."""
        self._month = month
        self._attr_translation_key = f"month_{month}"
        self._init_snowfall(entry, f"month_{month}")

    @property
    def is_on(self) -> bool:
        """Return whether this month is enabled."""
        months = self._options.get(CONF_MONTHS, DEFAULTS[CONF_MONTHS])
        return self._month in {int(month) for month in months}

    async def async_turn_on(self, **kwargs) -> None:
        """Enable this month."""
        months = {
            int(month)
            for month in self._options.get(CONF_MONTHS, DEFAULTS[CONF_MONTHS])
        }
        months.add(self._month)
        await update_options(
            self.hass,
            self._entry,
            {CONF_MONTHS: sorted(months)},
        )

    async def async_turn_off(self, **kwargs) -> None:
        """Disable this month."""
        months = {
            int(month)
            for month in self._options.get(CONF_MONTHS, DEFAULTS[CONF_MONTHS])
        }
        months.discard(self._month)
        await update_options(
            self.hass,
            self._entry,
            {CONF_MONTHS: sorted(months)},
        )
