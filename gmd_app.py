import sys
import importlib
import FreeCAD as App  # type: ignore

BASE = r"C:\IamandiS\GMD"
if BASE not in sys.path:
    sys.path.insert(0, BASE)

import config
importlib.reload(config)

from gates.sliding_gate import SlidingGate
from gates.swing_double_gate import SwingDoubleGate


def run():
    doc = App.ActiveDocument
    if doc is None:
        doc = App.newDocument("GMD_Gate")

    for obj in list(doc.Objects):
        doc.removeObject(obj.Name)

    if config.GATE_TYPE == "sliding":
        gate = SlidingGate(doc, config)

    elif config.GATE_TYPE == "swing_double":
        gate = SwingDoubleGate(doc, config)

    else:
        raise ValueError(f"Tip poartă necunoscut: {config.GATE_TYPE}")

    gate.build()
    doc.recompute()

    App.Console.PrintMessage("✔ Poartă generată din config.py\n")
