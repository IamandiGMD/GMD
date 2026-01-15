import FreeCAD as App  # type: ignore
from gates.base_gate import BaseGate


class SlidingGate(BaseGate):

    def build(self):
        cfg = self.cfg

        w = cfg.GATE_WIDTH
        h = cfg.GATE_HEIGHT
        p = cfg.PROFILE_SIZE

        # =========================
        # vertical stânga
        # =========================
        self.profile(
            name="Left",
            length=h,
            placement=App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation()
            )
        )

        # =========================
        # vertical dreapta
        # =========================
        self.profile(
            name="Right",
            length=h,
            placement=App.Placement(
                App.Vector(w - p, 0, 0),
                App.Rotation()
            )
        )

        # =========================
        # jos (ridicată cu grosimea profilului)
        # =========================
        self.profile(
            name="Bottom",
            length=w,
            placement=App.Placement(
                App.Vector(0, 0, p),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )

        # =========================
        # sus (coborâtă cu grosimea profilului)
        # =========================
        self.profile(
            name="Top",
            length=w,
            placement=App.Placement(
                App.Vector(0, 0, h - p),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )
