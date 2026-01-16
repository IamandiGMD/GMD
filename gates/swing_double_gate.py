import FreeCAD as App  # type: ignore

from gates.base_gate import BaseGate
from profiles.steel_profiles import get_profile


# =====================================================
# DISTRIBUIRE LINIARĂ – local (fără import extern)
# =====================================================
def distribute_linear(total_length: float, count: int, element_size: float):
    if count <= 0:
        return []

    if count == 1:
        return [(total_length - element_size) / 2.0]

    free_space = total_length - count * element_size
    if free_space < 0:
        raise ValueError("Nu este suficient spațiu pentru distribuție")

    step = free_space / (count + 1)
    return [
        step * (i + 1) + element_size * i
        for i in range(count)
    ]


class SwingDoubleGate(BaseGate):
    """
    Poartă batantă dublă, fără stâlpi și balamale
    Toți parametrii specifici acestui tip de poartă sunt definiți AICI
    """

    # =========================
    # PROFILE CADRU
    # =========================
    FRAME_VERTICAL_EXT = "60x60x2"
    FRAME_VERTICAL_INT = "60x40x2"
    FRAME_TOP = "60x40x2"
    FRAME_BOTTOM = "60x40x2"

    # =========================
    # PROFILE UMPLERE
    # =========================
    FILL_VERTICAL = "40x20x2"
    FILL_HORIZONTAL = "40x20x2"

    # =========================
    # BUILD
    # =========================
    def build(self):
        cfg = self.cfg

        total_w = cfg.GATE_WIDTH
        h = cfg.GATE_HEIGHT
        gap = cfg.GAP

        leaf_w = (total_w - gap) / 2.0

        self._build_leaf("Left", 0.0, leaf_w, h)
        self._build_leaf("Right", leaf_w + gap, leaf_w, h)

    # =========================
    # LEAF
    # =========================
    def _build_leaf(self, name: str, x0: float, w: float, h: float):
        cfg = self.cfg

        v_total = cfg.VERTICAL_COUNT
        h_count = cfg.HORIZONTAL_COUNT

        # =========================
        # PROFILE
        # =========================
        frame_v_ext = get_profile(self.FRAME_VERTICAL_EXT)
        frame_v_int = get_profile(self.FRAME_VERTICAL_INT)
        frame_bottom = get_profile(self.FRAME_BOTTOM)
        frame_top = get_profile(self.FRAME_TOP)

        fill_v = get_profile(self.FILL_VERTICAL)
        fill_h = get_profile(self.FILL_HORIZONTAL)

        frame_left_w = frame_v_ext["width"]
        frame_right_w = frame_v_int["width"]

        bottom_h = frame_bottom["height"]
        top_h = frame_top["height"]

        # =========================
        # GEOMETRIE CORECTĂ
        # =========================
        z_vertical = bottom_h
        vertical_len = h - bottom_h - top_h

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
            )
        )

        # =========================
        # CADRU VERTICAL
        # =========================
        self.profile(
            self.FRAME_VERTICAL_EXT,
            vertical_len,
            f"{name}_FrameLeft",
            App.Placement(
                App.Vector(x0, 0, z_vertical),
                App.Rotation()
            )
        )

        self.profile(
            self.FRAME_VERTICAL_INT,
            vertical_len,
            f"{name}_FrameRight",
            App.Placement(
                App.Vector(x0 + w - frame_right_w, 0, z_vertical),
                App.Rotation()
            )
        )

        # =========================
        # UMPLERE VERTICALĂ
        # =========================
        fill_count = max(v_total - 2, 0)
        if fill_count > 0:
            inner_w = w - frame_left_w - frame_right_w

            xs = distribute_linear(
                inner_w,
                fill_count,
                fill_v["width"]
            )

            for i, x in enumerate(xs):
                self.profile(
                    self.FILL_VERTICAL,
                    vertical_len,
                    f"{name}_V{i + 1}",
                    App.Placement(
                        App.Vector(
                            x0 + frame_left_w + x,
                            0,
                            z_vertical
                        ),
                        App.Rotation()
                    )
                )

        # =========================
        # UMPLERE ORIZONTALĂ
        # =========================
        if h_count > 0:
            inner_h = h - bottom_h - top_h

            zs = distribute_linear(
                inner_h,
                h_count,
                fill_h["height"]
            )

            for i, z in enumerate(zs):
                self.profile(
                    self.FILL_HORIZONTAL,
                    w,
                    f"{name}_H{i + 1}",
                    App.Placement(
                        App.Vector(
                            x0,
                            0,
                            bottom_h + z
                        ),
                        App.Rotation(App.Vector(0, 1, 0), 90)
                    )
                )
