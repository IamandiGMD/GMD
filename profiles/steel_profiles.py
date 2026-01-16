# profiles/steel_profiles.py

"""
Colecție standard de profile rectangulare
format cheie: "latime x inaltime x grosime" (mm)
"""

STEEL_PROFILES = {
    "60x60x2": {
        "width": 60.0,
        "height": 60.0,
        "thickness": 2.0,
    },
    "60x40x2": {
        "width": 60.0,
        "height": 40.0,
        "thickness": 2.0,
    },
    "50x50x2": {
        "width": 50.0,
        "height": 50.0,
        "thickness": 2.0,
    },
    "40x40x2": {
        "width": 40.0,
        "height": 40.0,
        "thickness": 2.0,
    },
        "40x20x2": {
        "width": 40.0,
        "height": 20.0,
        "thickness": 2.0,
    },
        "40x25x2": {
        "width": 40.0,
        "height": 25.0,
        "thickness": 2.0,
    },
    "30x30x2": {
        "width": 30.0,
        "height": 30.0,
        "thickness": 2.0,
    },
}


def get_profile(profile_name: str) -> dict:
    if profile_name not in STEEL_PROFILES:
        raise ValueError(f"Profil necunoscut: {profile_name}")
    return STEEL_PROFILES[profile_name]
