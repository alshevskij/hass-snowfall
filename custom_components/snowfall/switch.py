"""Snowfall switch entities."""

from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from .const import (
    CONF_EXCLUDED_PATHS,
    CONF_INCLUDED_PATHS,
    CONF_MODE,
    CONF_MONTHS,
    CONF_DEVICE_MODE,
    DEFAULTS,
    MONTHS,
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
    """Set up the global Snowfall switches."""
    entities = [SnowfallSwitch(entry)]
    entities.extend(SnowfallMonthSwitch(entry, month) for month in MONTHS)
    async_add_entities(entities)


class SnowfallSwitch(SnowfallEntityMixin, RestoreEntity, SwitchEntity):
    """Main switch that controls the global snowfall effect."""

    _attr_has_entity_name = True
    _attr_translation_key = "snowfall"
    _attr_icon = "mdi:snowflake"

    def __init__(self, entry: ConfigEntry) -> None:
        self._init_snowfall(entry, "enabled")
        self._attr_is_on = False

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        if (last_state := await self.async_get_last_state()) is not None:
            self._attr_is_on = last_state.state == "on"

    @property
    def extra_state_attributes(self) -> dict:
        """Expose global scheduling and page rules to the frontend."""
        options = {**DEFAULTS, **self._entry.options}
        return {
            CONF_MODE: options[CONF_MODE],
            CONF_MONTHS: options[CONF_MONTHS],
            CONF_EXCLUDED_PATHS: options[CONF_EXCLUDED_PATHS],
            CONF_INCLUDED_PATHS: options[CONF_INCLUDED_PATHS],
            CONF_DEVICE_MODE: options[CONF_DEVICE_MODE],
        }

    async def async_turn_on(self, **kwargs) -> None:
        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        self._attr_is_on = False
        self.async_write_ha_state()


class SnowfallMonthSwitch(SnowfallEntityMixin, SwitchEntity):
    """Switch for an individual active month."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:calendar-month"
    _attr_entity_registry_visible_default = False

    def __init__(self, entry: ConfigEntry, month: int) -> None:
        self._month = month
        self._attr_translation_key = f"month_{month}"
        self._init_snowfall(entry, f"month_{month}")

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        update_month_entities_visibility(self.hass, self._entry)

    @property
    def is_on(self) -> bool:
        months = self._options.get(CONF_MONTHS, DEFAULTS[CONF_MONTHS])
        return self._month in {int(month) for month in months}

    async def async_turn_on(self, **kwargs) -> None:
        months = {
            int(month)
            for month in self._options.get(CONF_MONTHS, DEFAULTS[CONF_MONTHS])
        }
        months.add(self._month)
        await update_options(self.hass, self._entry, {CONF_MONTHS: sorted(months)})

    async def async_turn_off(self, **kwargs) -> None:
        months = {
            int(month)
            for month in self._options.get(CONF_MONTHS, DEFAULTS[CONF_MONTHS])
        }
        months.discard(self._month)
        await update_options(self.hass, self._entry, {CONF_MONTHS: sorted(months)})
