class BaseGate:
    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        self.build_frame()
        self.build_fill()
        self.build_accessories()

    def build_frame(self):
        pass

    def build_fill(self):
        pass

    def build_accessories(self):
        pass
