import FreeCAD as App  # type: ignore
from profiles.rectangular import rectangular_tube


class BaseGate:
    def __init__(self, doc):
        self.doc = doc

    def profile(self, name, profile, length, placement):
        rectangular_tube(
            self.doc,
            profile=profile,
            length=length,
            name=name,
            placement=placement
        )
