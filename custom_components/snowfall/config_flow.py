"""Config flow for Snowfall."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class SnowfallConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Snowfall."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Create the integration entry."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is not None:
            return self.async_create_entry(
                title="Snowfall",
                data={},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
