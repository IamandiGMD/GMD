import FreeCAD as App  # type: ignore
import sys

BASE = r"C:\IamandiS\GMD"
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from gates.base_gate import BaseGate
from profiles.steel_profiles import get_profile


class SwingDoubleGate(BaseGate):
    """
    Poartă batantă dublă, fără stâlpi și balamale
    """

    # =========================
    # PROFILE CADRU
    # =========================
    FRAME_VERTICAL_EXT = "60x60x2"   # exterior (lângă balamale)
    FRAME_VERTICAL_INT = "60x40x2"   # interior (spre centru)
    FRAME_BOTTOM = "60x40x2"
    FRAME_TOP = "60x40x2"

    # =========================
    # PROFILE UMPLERE
    # =========================
    FILL_VERTICAL = "40x20x2"
    FILL_HORIZONTAL = "40x20x2"

    # =========================
    # ROTIRI CADRU (grade)
    # =========================
    ROT_FRAME_VERT_EXT = 0.0
    ROT_FRAME_VERT_INT = 90.0
    ROT_FRAME_BOTTOM = 90.0
    ROT_FRAME_TOP = 90.0

    # =========================
    # ROTIRE UMPLERE
    # =========================
    ROTATE_FILL = 0.0

    # =========================
    # BUILD
    # =========================
    def build(self):
        cfg = self.cfg

        total_w = cfg.GATE_WIDTH
        h = cfg.GATE_HEIGHT
        gap = cfg.GAP

        leaf_w = (total_w - gap) / 2.0

        self._build_leaf("Left", 0.0, leaf_w, h, hinge="left")
        self._build_leaf("Right", leaf_w + gap, leaf_w, h, hinge="right")

    # =========================
    # LEAF
    # =========================
    def _build_leaf(self, name, x0, w, h, hinge):
        cfg = self.cfg

        v_total = cfg.VERTICAL_COUNT

        frame_ext = get_profile(self.FRAME_VERTICAL_EXT)
        frame_int = get_profile(self.FRAME_VERTICAL_INT)
        frame_h = get_profile(self.FRAME_BOTTOM)
        fill_v = get_profile(self.FILL_VERTICAL)

        # alegere profile stânga / dreapta (oglindire corectă)
        if hinge == "left":
            left_prof = self.FRAME_VERTICAL_EXT
            right_prof = self.FRAME_VERTICAL_INT
            left_w = frame_ext["width"]
            right_w = frame_int["width"]
            rot_left = self.ROT_FRAME_VERT_EXT
            rot_right = self.ROT_FRAME_VERT_INT
        else:
            left_prof = self.FRAME_VERTICAL_INT
            right_prof = self.FRAME_VERTICAL_EXT
            left_w = frame_int["width"]
            right_w = frame_ext["width"]
            rot_left = self.ROT_FRAME_VERT_INT
            rot_right = self.ROT_FRAME_VERT_EXT

        bottom_h = frame_h["height"]
        top_h = frame_h["height"]

        # zona verticalelor (între cadru jos și sus)
        z0 = bottom_h
        vertical_len = h - bottom_h - top_h

        # =========================
        # CADRU VERTICAL
        # =========================
        self.profile(
            left_prof,
            vertical_len,
            f"{name}_FrameLeft",
            App.Placement(
                App.Vector(x0, 0, z0),
                App.Rotation(App.Vector(0, 0, 1), rot_left)
            )
        )

        self.profile(
            right_prof,
            vertical_len,
            f"{name}_FrameRight",
            App.Placement(
                App.Vector(x0 + w - right_w, 0, z0),
                App.Rotation(App.Vector(0, 0, 1), rot_right)
            )
        )

        # =========================
        # UMPLERE VERTICALĂ (CENTRATĂ PERFECT)
        # =========================
        fill_count = max(v_total - 2, 0)

        if fill_count > 0:
            inner_w = w - left_w - right_w
            bar_w = fill_v["width"]

            spacing = (inner_w - fill_count * bar_w) / (fill_count + 1)

            total_fill_width = fill_count * bar_w + (fill_count - 1) * spacing
            center_offset = (inner_w - total_fill_width) / 2.0

            for i in range(fill_count):
                x = center_offset + i * (bar_w + spacing)

                self.profile(
                    self.FILL_VERTICAL,
                    vertical_len,
                    f"{name}_V{i}",
                    App.Placement(
                        App.Vector(x0 + left_w + x, 0, z0),
                        App.Rotation(App.Vector(0, 0, 1), self.ROTATE_FILL)
                    )
                )

        # =========================
        # CADRU ORIZONTAL JOS
        # =========================
        self.profile(
            self.FRAME_BOTTOM,
            w,
            f"{name}_FrameBottom",
            App.Placement(
                App.Vector(x0, 0, 0),
                App.Rotation(App.Vector(0, 1, 0), 90)
                * App.Rotation(App.Vector(0, 0, 1), self.ROT_FRAME_BOTTOM)
            )
        )

        # =========================
        # CADRU ORIZONTAL SUS
        # =========================
        self.profile(
            self.FRAME_TOP,
            w,
            f"{name}_FrameTop",
            App.Placement(
                App.Vector(x0, 0, h - top_h),
                App.Rotation(App.Vector(0, 1, 0), 90)
                * App.Rotation(App.Vector(0, 0, 1), self.ROT_FRAME_TOP)
            )
        )
