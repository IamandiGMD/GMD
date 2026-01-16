import FreeCAD as App  # type: ignore
from gates.base_gate import BaseGate


class SwingDoubleGate(BaseGate):

    # =========================
    # PROFILE CADRU (DOAR AICI)
    # =========================
    FRAME_VERTICAL_OUTER = "60x60x2"
    FRAME_VERTICAL_INNER = "60x60x2"
    FRAME_HORIZONTAL_TOP = "60x60x2"
    FRAME_HORIZONTAL_BOTTOM = "60x60x2"

    # =========================
    # PROFILE UMPLERE
    # =========================
    FILL_VERTICAL = "60x60x2"
    FILL_HORIZONTAL = "40x25x2"

    # =========================
    # BUILD
    # =========================
    def __init__(self, doc, cfg):
        super().__init__(doc)
        self.cfg = cfg

    def build(self):
        cfg = self.cfg

        total_w = cfg.GATE_WIDTH
        h = cfg.GATE_HEIGHT
        gap = cfg.GAP

        leaf_w = (total_w - gap) / 2

        self._build_leaf("Left", 0, leaf_w, h, cfg, outer_left=True)
        self._build_leaf("Right", leaf_w + gap, leaf_w, h, cfg, outer_left=False)

    def _build_leaf(self, name, x0, w, h, cfg, outer_left):

        # -------------------------
        # RAMĂ
        # -------------------------
        # vertical exterior
        self.profile(
            name=f"{name}_V_Outer",
            profile=self.FRAME_VERTICAL_OUTER,
            length=h,
            placement=App.Placement(
                App.Vector(x0 if outer_left else x0 + w - 60, 0, 0 - 60),
                App.Rotation()
            )
        )

        # vertical interior
        self.profile(
            name=f"{name}_V_Inner",
            profile=self.FRAME_VERTICAL_INNER,
            length=h,
            placement=App.Placement(
                App.Vector(x0 + w - 60 if outer_left else x0, 0, 0 - 60),
                App.Rotation()
            )
        )

        # jos
        self.profile(
            name=f"{name}_Bottom",
            profile=self.FRAME_HORIZONTAL_BOTTOM,
            length=w,
            placement=App.Placement(
                App.Vector(x0, 0, 0),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )

        # sus
        self.profile(
            name=f"{name}_Top",
            profile=self.FRAME_HORIZONTAL_TOP,
            length=w,
            placement=App.Placement(
                App.Vector(x0, 0, h - 60),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )

        # -------------------------
        # UMPLERE VERTICALĂ
        # -------------------------
        count = cfg.VERTICAL_COUNT
        if count > 2:
            step = w / (count - 1)

            for i in range(1, count - 1):
                x = x0 + i * step - 20

                self.profile(
                    name=f"{name}_Fill_V_{i}",
                    profile=self.FILL_VERTICAL,
                    length=h - 120,
                    placement=App.Placement(
                        App.Vector(x, 0, 0),
                        App.Rotation()
                    )
                )

        # -------------------------
        # UMPLERE ORIZONTALĂ
        # -------------------------
        if cfg.HORIZONTAL_COUNT > 0:
            z = h / 2 - 15

            self.profile(
                name=f"{name}_Fill_H",
                profile=self.FILL_HORIZONTAL,
                length=w,
                placement=App.Placement(
                    App.Vector(x0, 0, z),
                    App.Rotation(App.Vector(0, 1, 0), 90)
                )
            )
