import sys
import FreeCAD as App # type: ignore

BASE = r"C:\IamandiS\GMD"
if BASE not in sys.path:
    sys.path.insert(0, BASE)

import config
from gates.sliding_gate import SlidingGate


def run():
    doc = App.ActiveDocument
    if doc is None:
        doc = App.newDocument("GMD_Gate")

    for obj in list(doc.Objects):
        doc.removeObject(obj.Name)

    gate = SlidingGate(config)
    gate.build()

    doc.recompute()
    App.Console.PrintMessage("✔ Poartă generată din config.py\n")
