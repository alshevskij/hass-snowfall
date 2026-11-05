"""Shared entity helpers for Snowfall."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import (
    async_dispatcher_connect,
    async_dispatcher_send,
)

from .const import DEFAULTS, DOMAIN

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


class SnowfallEntityMixin:
    """Mixin with shared config-entry settings support."""

    _entry: ConfigEntry

    def _init_snowfall(self, entry: ConfigEntry, unique_id_suffix: str) -> None:
        """Initialize common entity properties."""
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_{unique_id_suffix}"

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
        """Write state when shared settings change."""
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
