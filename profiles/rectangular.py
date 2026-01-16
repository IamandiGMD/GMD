# profiles/rectangular.py

import FreeCAD as App  # type: ignore
import Part  # type: ignore

from profiles.steel_profiles import get_profile


def rectangular_tube(
    doc,
    profile: str,
    length: float,
    name: str,
    placement: App.Placement,
):
    """
    Creează o țeavă rectangulară REALĂ (profil gol)
    """

    data = get_profile(profile)

    w = data["width"]
    h = data["height"]
    t = data["thickness"]

    if t * 2 >= min(w, h):
        raise ValueError(f"Grosime invalidă pentru profil {profile}")

    # solid exterior
    outer = Part.makeBox(w, h, length)

    # solid interior
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
