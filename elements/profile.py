import Part
import FreeCAD as App


def rectangle_wire(width, height):
    return Part.makePolygon([
        App.Vector(0, 0, 0),
        App.Vector(width, 0, 0),
        App.Vector(width, height, 0),
        App.Vector(0, height, 0),
        App.Vector(0, 0, 0)
    ])


def square_tube(length, profile):
    w = profile["width"]
    h = profile["height"]
    t = profile["thickness"]

    outer = rectangle_wire(w, h)
    inner = rectangle_wire(w - 2*t, h - 2*t)
    inner.translate(App.Vector(t, t, 0))

    outer_face = Part.Face(outer)
    inner_face = Part.Face(inner)

    section = outer_face.cut(inner_face)

    # 🔑 EXTRUDARE PE Z
    solid = section.extrude(App.Vector(0, 0, length))
    return solid
