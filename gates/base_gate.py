import FreeCAD as App  # type: ignore
from profiles.rectangular import rectangular_tube


class BaseGate:
    def __init__(self, doc, cfg):
        self.doc = doc
        self.cfg = cfg

    # =========================
    # creare profil tubular
    # =========================
    def profile(self, *, name, length, placement):
        """
        Creează o țeavă rectangulară standard
        """
        return rectangular_tube(
            name=name,
            width=self.cfg.PROFILE_SIZE,
            height=self.cfg.PROFILE_SIZE,
            thickness=self.cfg.PROFILE_THICKNESS,
            length=length,
            placement=placement,
        )
