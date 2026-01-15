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

    def _build_leaf(self, name, x, w, h, p):

        self.profile(
            name=f"{name}_V1",
            length=h,
            placement=App.Placement(
                App.Vector(x, 0, 0),
                App.Rotation()
            )
        )

        self.profile(
            name=f"{name}_V2",
            length=h,
            placement=App.Placement(
                App.Vector(x + w - p, 0, 0),
                App.Rotation()
            )
        )

        self.profile(
            name=f"{name}_Bottom",
            length=w,
            placement=App.Placement(
                App.Vector(x, 0, p),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )

        self.profile(
            name=f"{name}_Top",
            length=w,
            placement=App.Placement(
                App.Vector(x, 0, h),
                App.Rotation(App.Vector(0, 1, 0), 90)
            )
        )
