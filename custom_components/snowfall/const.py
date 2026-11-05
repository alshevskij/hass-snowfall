"""Constants for Snowfall."""

DOMAIN = "snowfall"

FRONTEND_URL = "/snowfall"
JS_URL = f"{FRONTEND_URL}/snowfall.js?v=2026.11.3"

CONF_MODE = "mode"
CONF_MONTHS = "months"
CONF_EXCLUDED_PATHS = "excluded_paths"
CONF_INCLUDED_PATHS = "included_paths"
CONF_FLAKE_COUNT = "flake_count"
CONF_SPEED = "speed"
CONF_SIZE = "size"
CONF_OPACITY = "opacity"
CONF_FPS = "fps"

MODE_ALWAYS = "always"
MODE_WINTER = "winter"
MODE_CUSTOM = "custom"

FPS_30 = "30"
FPS_60 = "60"

MONTHS = tuple(range(1, 13))

DEFAULTS = {
    CONF_MODE: MODE_ALWAYS,
    CONF_MONTHS: [12, 1, 2],
    CONF_EXCLUDED_PATHS: [],
    CONF_INCLUDED_PATHS: [],
    CONF_FLAKE_COUNT: 120,
    CONF_SPEED: 100,
    CONF_SIZE: 100,
    CONF_OPACITY: 85,
    CONF_FPS: FPS_60,
}
