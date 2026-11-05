"""Shared entity helpers for Snowfall."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.dispatcher import (
    async_dispatcher_connect,
    async_dispatcher_send,
)
from homeassistant.helpers.entity_registry import RegistryEntryHider

from .const import DEFAULTS, DOMAIN, MODE_CUSTOM, MONTHS

SIGNAL_SETTINGS_UPDATED = f"{DOMAIN}_settings_updated"


async def update_options(
    hass: HomeAssistant,
    entry: ConfigEntry,
    changes: Mapping[str, Any],
) -> None:
    """Persist settings and notify all Snowfall entities."""
    options = {**entry.options, **changes}
    hass.config_entries.async_update_entry(entry, options=options)
    async_dispatcher_send(
        hass,
        f"{SIGNAL_SETTINGS_UPDATED}_{entry.entry_id}",
    )


@callback
def update_month_entities_visibility(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> None:
    """Show month switches only while custom scheduling is selected."""
    registry = er.async_get(hass)
    visible = entry.options.get("mode", DEFAULTS["mode"]) == MODE_CUSTOM

    for month in MONTHS:
        unique_id = f"{entry.entry_id}_month_{month}"
        entity_id = registry.async_get_entity_id("switch", DOMAIN, unique_id)
        if entity_id is None:
            continue

        registry_entry = registry.async_get(entity_id)
        if registry_entry is None:
            continue

        # Respect an explicit visibility choice made by the user.
        if registry_entry.hidden_by == RegistryEntryHider.USER:
            continue

        hidden_by = None if visible else RegistryEntryHider.INTEGRATION
        if registry_entry.hidden_by != hidden_by:
            registry.async_update_entity(entity_id, hidden_by=hidden_by)


class SnowfallEntityMixin:
    """Mixin with shared config-entry and device support."""

    _entry: ConfigEntry

    def _init_snowfall(self, entry: ConfigEntry, unique_id_suffix: str) -> None:
        """Initialize common entity properties."""
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_{unique_id_suffix}"

    @property
    def device_info(self) -> DeviceInfo:
        """Group every Snowfall entity under one Home Assistant device."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry.entry_id)},
            name="Snowfall",
            manufacturer="ALSHEVSKIJ",
            model="Home Assistant FX",
            sw_version="2026.11.3",
        )

    @property
    def _options(self) -> dict[str, Any]:
        """Return current options, including defaults for older entries."""
        return {**DEFAULTS, **self._entry.options}

    async def async_added_to_hass(self) -> None:
        """Subscribe to changes made by sibling entities."""
        await super().async_added_to_hass()
        self._subscribe_to_updates()

    @callback
    def _subscribe_to_updates(self) -> None:
        """Subscribe to settings changes."""
        self.async_on_remove(
            async_dispatcher_connect(
                self.hass,
                f"{SIGNAL_SETTINGS_UPDATED}_{self._entry.entry_id}",
                self._handle_settings_update,
            )
        )

    @callback
    def _handle_settings_update(self) -> None:
        """Refresh the entity after settings change."""
        self.async_write_ha_state()
