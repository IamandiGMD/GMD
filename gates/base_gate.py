# gates/base_gate.py

from profiles.rectangular import rectangular_tube


class BaseGate:
    def __init__(self, doc, cfg):
        self.doc = doc
        self.cfg = cfg

    def profile(self, profile_name, length, name, placement):
        return rectangular_tube(
            doc=self.doc,
            profile_name=profile_name,
            length=length,
            name=name,
            placement=placement,
        )
