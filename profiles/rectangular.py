import FreeCAD as App # type: ignore
import Part


def rectangular_tube(
    width,
    height,
    thickness,
    length,
    name="RectangularTube",
    placement=None
):
    doc = App.ActiveDocument
    if doc is None:
        doc = App.newDocument("GMD")

    outer = Part.makeBox(width, height, length)

    inner = Part.makeBox(
        width - 2 * thickness,
        height - 2 * thickness,
        length
    )
    inner.translate(App.Vector(thickness, thickness, 0))

    shape = outer.cut(inner)

    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape

    if placement:
        obj.Placement = placement

    return obj
