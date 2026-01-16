# profiles/rectangular.py

import FreeCAD as App  # type: ignore
import Part

from profiles.steel_profiles import get_profile


def rectangular_tube(
    doc,
    profile_name: str,
    length: float,
    name: str,
    placement: App.Placement,
):
    """
    Creează o țeavă rectangulară pe baza unui profil din steel_profiles.py
    """

    p = get_profile(profile_name)

    w = p["width"]
    h = p["height"]
    t = p["thickness"]

    if t * 2 >= min(w, h):
        raise ValueError(f"Grosime invalidă pentru profil {profile_name}")

    # solid exterior
    outer = Part.makeBox(w, h, length)

    # gol interior
    inner = Part.makeBox(
        w - 2 * t,
        h - 2 * t,
        length
    )
    inner.translate(App.Vector(t, t, 0))

    shape = outer.cut(inner)

    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape
    obj.Placement = placement

    return obj
