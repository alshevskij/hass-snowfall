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
CONF_FLAKE_STYLE = "flake_style"
CONF_PRESET = "preset"
CONF_WIND_STRENGTH = "wind_strength"
CONF_WIND_DIRECTION = "wind_direction"
CONF_WIND_GUSTS = "wind_gusts"

MODE_ALWAYS = "always"
MODE_WINTER = "winter"
MODE_CUSTOM = "custom"

FPS_30 = "30"
FPS_60 = "60"

FLAKE_STYLE_DOTS = "dots"
FLAKE_STYLE_SNOWFLAKES = "snowflakes"
FLAKE_STYLE_CRYSTALS = "crystals"
FLAKE_STYLE_MIXED = "mixed"

PRESET_LIGHT = "light"
PRESET_NORMAL = "normal"
PRESET_HEAVY = "heavy"
PRESET_BLIZZARD = "blizzard"

WIND_LEFT = "left"
WIND_RIGHT = "right"
WIND_VARIABLE = "variable"

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
    CONF_FLAKE_STYLE: FLAKE_STYLE_MIXED,
    CONF_PRESET: PRESET_NORMAL,
    CONF_WIND_STRENGTH: 0,
    CONF_WIND_DIRECTION: WIND_RIGHT,
    CONF_WIND_GUSTS: 20,
}
