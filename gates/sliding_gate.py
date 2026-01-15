import FreeCAD as App # type: ignore
from profiles.rectangular import rectangular_tube


class SlidingGate:
    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        W = self.cfg.GATE_WIDTH
        H = self.cfg.GATE_HEIGHT
        P = self.cfg.PROFILE_SIZE
        T = self.cfg.PROFILE_THICKNESS

        # STÂNGA (vertical)
        rectangular_tube(
            name="Left",
            width=P,
            height=P,
            thickness=T,
            length=H,
            placement=App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation()
            )
        )

        # DREAPTA (vertical)
        rectangular_tube(
            name="Right",
            width=P,
            height=P,
            thickness=T,
            length=H,
            placement=App.Placement(
                App.Vector(W - P, 0, 0),
                App.Rotation()
            )
        )

        # JOS (orizontal)
        rectangular_tube(
            name="Bottom",
            width=P,
            height=P,
            thickness=T,
            length=W,
            placement=App.Placement(
                App.Vector(0, 0, P),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )

        # SUS (orizontal)
        rectangular_tube(
            name="Top",
            width=P,
            height=P,
            thickness=T,
            length=W,
            placement=App.Placement(
                App.Vector(0, 0, H),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )
