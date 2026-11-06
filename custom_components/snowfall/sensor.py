"""Snowfall profile data sensors."""

from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DEFAULTS,
    DEVICE_DESKTOP,
    DEVICE_MOBILE,
    DEVICE_MODE_SEPARATE,
    CONF_DEVICE_MODE,
    PROFILE_SETTING_KEYS,
)
from .entity import SnowfallEntityMixin


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up hidden profile data sensors consumed by the frontend."""
    async_add_entities(
        [
            SnowfallProfileSensor(entry, DEVICE_DESKTOP),
            SnowfallProfileSensor(entry, DEVICE_MOBILE),
        ]
    )


class SnowfallProfileSensor(SnowfallEntityMixin, SensorEntity):
    """Expose one visual profile as attributes for the frontend renderer."""

    _attr_has_entity_name = False
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_entity_registry_visible_default = False

    def __init__(self, entry: ConfigEntry, device_role: str) -> None:
        self._device_role = device_role
        self._attr_translation_key = f"{device_role}_profile"
        self._init_snowfall(entry, f"{device_role}_profile", device_role)

    @property
    def native_value(self) -> str:
        if self._device_role == DEVICE_DESKTOP:
            return "active"
        return (
            "active"
            if self._options.get(CONF_DEVICE_MODE, DEFAULTS[CONF_DEVICE_MODE])
            == DEVICE_MODE_SEPARATE
            else "inactive"
        )

    @property
    def extra_state_attributes(self) -> dict:
        """Expose a stable profile marker and the profile settings."""
        return {
            "snowfall_profile": self._device_role,
            **{
                key: self._options.get(
                    f"{self._device_role}_{key}", DEFAULTS[key]
                )
                for key in PROFILE_SETTING_KEYS
            },
        }
