import FreeCAD as App  # type: ignore
from gates.base_gate import BaseGate


class SwingDoubleGate(BaseGate):

    def build(self):
        cfg = self.cfg

        p = cfg.PROFILE_SIZE
        h = cfg.GATE_HEIGHT
        total_w = cfg.GATE_WIDTH
        gap = cfg.GAP

        leaf_w = (total_w - gap) / 2

        self._build_leaf("LeftLeaf", 0, leaf_w, h, p)
        self._build_leaf("RightLeaf", leaf_w + gap, leaf_w, h, p)

    # ==================================================
    # construcție foaie
    # ==================================================
    def _build_leaf(self, prefix, x0, width, height, p):
        cfg = self.cfg

        v_count = cfg.VERTICAL_COUNT
        h_count = cfg.HORIZONTAL_COUNT

        if v_count < 2:
            raise ValueError("VERTICAL_COUNT trebuie să fie >= 2")

        # =========================
        # BARE VERTICALE (incl. cadru)
        # =========================
        v_step = (width - p) / (v_count - 1)

        for i in range(v_count):
            x = x0 + i * v_step
            self.profile(
                name=f"{prefix}_V{i+1}",
                length=height,
                placement=App.Placement(
                    App.Vector(x, 0, 0 - p),
                    App.Rotation()
                )
            )

        # =========================
        # CADRU ORIZONTAL (jos)
        # =========================
        self.profile(
            name=f"{prefix}_Bottom",
            length=width,
            placement=App.Placement(
                App.Vector(x0, 0, 0),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )

        # =========================
        # BARE ORIZONTALE INTERIOARE
        # =========================
        if h_count > 0:
            h_step = (height - p) / (h_count + 1)

            for i in range(h_count):
                z = (i + 1) * h_step
                self.profile(
                    name=f"{prefix}_H{i+1}",
                    length=width,
                    placement=App.Placement(
                        App.Vector(x0, 0, z),
                        App.Rotation(App.Vector(0, 1, 0), 90)
                    )
                )

        # =========================
        # CADRU ORIZONTAL (sus)
        # =========================
        self.profile(
            name=f"{prefix}_Top",
            length=width,
            placement=App.Placement(
                App.Vector(x0, 0, height - p),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )
