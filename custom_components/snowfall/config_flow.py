
"""Config flow for Snowfall."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import (
    CONF_EXCLUDED_PATHS,
    CONF_FLAKE_COUNT,
    CONF_MODE,
    CONF_MONTHS,
    CONF_OPACITY,
    CONF_SIZE,
    CONF_SPEED,
    DEFAULTS,
    DOMAIN,
    MODE_ALWAYS,
    MODE_CUSTOM,
    MODE_WINTER,
)


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

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return the options flow."""
        return SnowfallOptionsFlow()


class SnowfallOptionsFlow(config_entries.OptionsFlow):
    """Handle Snowfall options."""

    async def async_step_init(self, user_input=None):
        """Select the snowfall mode."""

        current = {**DEFAULTS, **self.config_entry.options}

        if user_input is not None:
            self._selected_mode = user_input[CONF_MODE]
            return await self.async_step_settings()

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_MODE,
                    default=current[CONF_MODE],
                ): selector.SelectSelector(
                    selector.SelectSelectorConfig(
                        options=[
                            MODE_WINTER,
                            MODE_CUSTOM,
                            MODE_ALWAYS,
                        ],
                        translation_key="mode",
                        mode=selector.SelectSelectorMode.DROPDOWN,
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=schema,
        )

    async def async_step_settings(self, user_input=None):
        """Configure snowfall appearance and behavior."""

        current = {**DEFAULTS, **self.config_entry.options}

        if user_input is not None:
            # Normalize excluded paths.
            paths = user_input.get(CONF_EXCLUDED_PATHS) or ""

            if isinstance(paths, str):
                excluded_paths = [
                    line.strip()
                    for line in paths.splitlines()
                    if line.strip()
                ]
            else:
                excluded_paths = []

            # Normalize selected months.
            if self._selected_mode == MODE_CUSTOM:
                months = [
                    int(month)
                    for month in user_input.get(CONF_MONTHS, [])
                ]
            else:
                months = current[CONF_MONTHS]

            # Save all options.
            options = {
                **user_input,
                CONF_MODE: self._selected_mode,
                CONF_MONTHS: months,
                CONF_EXCLUDED_PATHS: excluded_paths,
            }

            return self.async_create_entry(data=options)

        schema_dict = {}

        # Show month selection only in custom mode.
        if self._selected_mode == MODE_CUSTOM:
            schema_dict[
                vol.Optional(
                    CONF_MONTHS,
                    default=[
                        str(month)
                        for month in current[CONF_MONTHS]
                    ],
                )
            ] = selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[
                        str(month)
                        for month in range(1, 13)
                    ],
                    translation_key="months",
                    multiple=True,
                    mode=selector.SelectSelectorMode.DROPDOWN,
                )
            )

        schema_dict.update(
            {
                vol.Optional(
                    CONF_EXCLUDED_PATHS,
                    description={
                        "suggested_value": "\n".join(
                            current[CONF_EXCLUDED_PATHS]
                        )
                    },
                ): selector.TextSelector(
                    selector.TextSelectorConfig(multiline=True)
                ),

                vol.Required(
                    CONF_FLAKE_COUNT,
                    default=current[CONF_FLAKE_COUNT],
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=10,
                        max=300,
                        step=10,
                        mode=selector.NumberSelectorMode.SLIDER,
                    )
                ),

                vol.Required(
                    CONF_SPEED,
                    default=current[CONF_SPEED],
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=25,
                        max=200,
                        step=5,
                        mode=selector.NumberSelectorMode.SLIDER,
                    )
                ),

                vol.Required(
                    CONF_SIZE,
                    default=current[CONF_SIZE],
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=25,
                        max=200,
                        step=5,
                        mode=selector.NumberSelectorMode.SLIDER,
                    )
                ),

                vol.Required(
                    CONF_OPACITY,
                    default=current[CONF_OPACITY],
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=10,
                        max=100,
                        step=5,
                        mode=selector.NumberSelectorMode.SLIDER,
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="settings",
            data_schema=vol.Schema(schema_dict),
        )
