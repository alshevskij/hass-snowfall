"""Snowfall text entities."""

from __future__ import annotations

import re

from homeassistant.components.text import TextEntity, TextMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_EXCLUDED_PATHS, CONF_INCLUDED_PATHS
from .entity import SnowfallEntityMixin, update_options


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Snowfall text entities."""
    async_add_entities(
        [
            SnowfallPathsText(entry, CONF_EXCLUDED_PATHS, "excluded_paths"),
            SnowfallPathsText(entry, CONF_INCLUDED_PATHS, "included_paths"),
        ]
    )


def parse_paths(value: str) -> list[str]:
    """Parse a single-line list of paths."""
    return list(
        dict.fromkeys(
            path.strip()
            for path in re.split(r"[,;\\n]+", value)
            if path.strip()
        )
    )


class SnowfallPathsText(SnowfallEntityMixin, TextEntity):
    """Text entity for included or excluded dashboard paths."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG
    _attr_mode = TextMode.TEXT
    _attr_native_min = 0
    _attr_native_max = 255

    def __init__(self, entry: ConfigEntry, key: str, translation_key: str) -> None:
        """Initialize a path list."""
        self._key = key
        self._attr_translation_key = translation_key
        self._attr_icon = "mdi:format-list-bulleted"
        self._init_snowfall(entry, translation_key)

    @property
    def native_value(self) -> str:
        """Return paths separated by semicolons."""
        paths = self._options.get(self._key, [])
        if isinstance(paths, str):
            return paths[:255]
        return "; ".join(paths)[:255]

    async def async_set_value(self, value: str) -> None:
        """Persist the edited path list."""
        await update_options(
            self.hass,
            self._entry,
            {self._key: parse_paths(value)},
        )
