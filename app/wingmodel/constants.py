import os
import math

## Physical constants

AIR_DENSITY = 1.225 #[kg/m^3]
AIR_KINEMATIC_VISCOSITY = 1.516*1e-5 # [m^/s], at 20 degrees C


DELTA_MAX = 0.1 ## relative wing tip displacement
G = 9.81 ## [m/s**2]
LOAD_FACTOR = 1.0


## Geometry

CHORD_MIN = 50
CHORD_MAX = 1000
CHORD_DEFAULT = 260

SPAN_MIN = 50
SPAN_MAX = 5000
SPAN_DEFAULT = 900

## App settings

STL_MODELS_DIR = os.path.join("app", "static")
CACHE_DIR = os.path.join("app", "cache")

MODEL_COLORS = {
    "box" : "#FFFF00",
    "foam": "#A9A9A9",
    "shell": "#A4D3EE"
}

USE_CACHED_RESULTS = False
# CACHE_LIFETIME_SECONDS = 6 * 3600
CACHE_LIFETIME_SECONDS = 60