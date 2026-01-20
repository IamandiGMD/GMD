import FreeCAD as App  # type: ignore
import sys

BASE = r"C:\IamandiS\GMD"
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from gates.base_gate import BaseGate
from profiles.steel_profiles import get_profile


def profile_with_front(profile_name: str, front_size: int) -> str:
    w, h, t = profile_name.split("x")
    w = int(w)
    h = int(h)

    if front_size == w:
        return f"{w}x{h}x{t}"
    elif front_size == h:
        return f"{h}x{w}x{t}"
    else:
        raise ValueError(f"Front {front_size} invalid pentru {profile_name}")


class SwingDoubleGate(BaseGate):

    # =========================
    # PROFILE CADRU
    # =========================
    FRAME_VERTICAL_EXT = "60x60x2"
    FRAME_VERTICAL_EXT_FRONT = 60

    FRAME_VERTICAL_INT = "40x60x2"
    FRAME_VERTICAL_INT_FRONT = 40

    FRAME_BOTTOM = "60x40x2"
    FRAME_BOTTOM_FRONT = 40

    FRAME_TOP = "60x40x2"
    FRAME_TOP_FRONT = 40

    # =========================
    # UMPLERE
    # =========================
    FILL_VERTICAL = "40x20x2"
    FILL_VERTICAL_FRONT = 40

    # =========================
    def place_profile(self, profile, length, name, base, vertical=True):
        rot = App.Rotation()
        if not vertical:
            rot = App.Rotation(App.Vector(0, 1, 0), 90)

        self.profile(profile, length, name, App.Placement(base, rot))

    # =========================
    def build(self):
        cfg = self.cfg
        w = cfg.GATE_WIDTH
        h = cfg.GATE_HEIGHT
        gap = cfg.GAP

        leaf_w = (w - gap) / 2

        self._leaf("Left", 0, leaf_w, h, "left")
        self._leaf("Right", leaf_w + gap, leaf_w, h, "right")

    # =========================
    def _leaf(self, name, x0, w, h, hinge):
        cfg = self.cfg
        v_count = cfg.VERTICAL_COUNT

        # -------------------------------------------------
        # POZIȚII CORECTE
        # -------------------------------------------------
        z_start = 0
        vertical_len = h - self.FRAME_BOTTOM_FRONT - self.FRAME_TOP_FRONT
        z_top = h - self.FRAME_TOP_FRONT

        # -------------------------------------------------
        # PROFILE ORIENTATE
        # -------------------------------------------------
        bottom_prof = profile_with_front(self.FRAME_BOTTOM, self.FRAME_BOTTOM_FRONT)
        top_prof = profile_with_front(self.FRAME_TOP, self.FRAME_TOP_FRONT)

        if hinge == "left":
            left_prof = profile_with_front(self.FRAME_VERTICAL_EXT, self.FRAME_VERTICAL_EXT_FRONT)
            right_prof = profile_with_front(self.FRAME_VERTICAL_INT, self.FRAME_VERTICAL_INT_FRONT)
        else:
            left_prof = profile_with_front(self.FRAME_VERTICAL_INT, self.FRAME_VERTICAL_INT_FRONT)
            right_prof = profile_with_front(self.FRAME_VERTICAL_EXT, self.FRAME_VERTICAL_EXT_FRONT)

        left_w = get_profile(left_prof)["width"]
        right_w = get_profile(right_prof)["width"]

        # -------------------------------------------------
        # VERTICALE CADRU
        # -------------------------------------------------
        self.place_profile(
            left_prof,
            vertical_len,
            f"{name}_FrameLeft",
            App.Vector(x0, 0, z_start),
            vertical=True
        )

        self.place_profile(
            right_prof,
            vertical_len,
            f"{name}_FrameRight",
            App.Vector(x0 + w - right_w, 0, z_start),
            vertical=True
        )

        # -------------------------------------------------
        # UMPLERE
        # -------------------------------------------------
        fill_prof = profile_with_front(self.FILL_VERTICAL, self.FILL_VERTICAL_FRONT)
        fill_w = get_profile(fill_prof)["width"]

        inner_w = w - left_w - right_w
        fill_count = max(v_count - 2, 0)

        if fill_count > 0:
            spacing = (inner_w - fill_count * fill_w) / (fill_count + 1)

            for i in range(fill_count):
                x = spacing * (i + 1) + fill_w * i
                self.place_profile(
                    fill_prof,
                    vertical_len,
                    f"{name}_V{i}",
                    App.Vector(x0 + left_w + x, 0, z_start),
                    vertical=True
                )

        # -------------------------------------------------
        # ORIZONTALE
        # -------------------------------------------------
        self.place_profile(
            bottom_prof,
            w,
            f"{name}_FrameBottom",
            App.Vector(x0, 0, 0),
            vertical=False
        )

        self.place_profile(
            top_prof,
            w,
            f"{name}_FrameTop",
            App.Vector(x0, 0, z_top),
            vertical=False
        )
