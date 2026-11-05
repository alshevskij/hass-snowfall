"""Snowfall integration for Home Assistant."""

from __future__ import annotations

from pathlib import Path

from homeassistant.components.frontend import add_extra_js_url, remove_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import (
    DEFAULTS,
    DOMAIN,
    FRONTEND_URL,
    JS_URL,
    PROFILE_SETTING_KEYS,
)
from .const import DEVICE_MODE_SHARED, CONF_DEVICE_MODE

PLATFORMS = [
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.TEXT,
]

FRONTEND_DIR = Path(__file__).parent / "frontend"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the integration."""
    return True


def _migrate_profile_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Move legacy visual options into the desktop profile and initialize mobile."""
    options = dict(entry.options)
    changed = False

    if CONF_DEVICE_MODE not in options:
        options[CONF_DEVICE_MODE] = DEVICE_MODE_SHARED
        changed = True

    for key in PROFILE_SETTING_KEYS:
        desktop_key = f"desktop_{key}"
        mobile_key = f"mobile_{key}"

        if desktop_key not in options:
            options[desktop_key] = options.get(key, DEFAULTS[key])
            changed = True
        if mobile_key not in options:
            options[mobile_key] = DEFAULTS[key]
            changed = True

    if changed:
        hass.config_entries.async_update_entry(entry, options=options)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Snowfall from a config entry."""
    _migrate_profile_options(hass, entry)

    if not hass.data.setdefault(DOMAIN, {}).get("static_registered"):
        await hass.http.async_register_static_paths(
            [
                StaticPathConfig(
                    url_path=FRONTEND_URL,
                    path=str(FRONTEND_DIR),
                    cache_headers=True,
                )
            ]
        )
        hass.data[DOMAIN]["static_registered"] = True

    add_extra_js_url(hass, JS_URL)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Snowfall."""
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, PLATFORMS
    )
    if unload_ok:
        remove_extra_js_url(hass, JS_URL)
    return unload_ok
