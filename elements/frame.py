import Part
import FreeCAD as App
from elements.profile import square_tube


def rectangular_frame(width, height, profile):
    shapes = []

    w = profile["width"]
    h = profile["height"]

    # jos
    bottom = square_tube(width, profile, "X")
    shapes.append(bottom)

    # sus
    top = square_tube(width, profile, "X")
    top.translate(App.Vector(0, height - h, 0))
    shapes.append(top)

    # stanga
    left = square_tube(height, profile, "Y")
    shapes.append(left)

    # dreapta
    right = square_tube(height, profile, "Y")
    right.translate(App.Vector(width - w, 0, 0))
    shapes.append(right)

    return Part.makeCompound(shapes)
