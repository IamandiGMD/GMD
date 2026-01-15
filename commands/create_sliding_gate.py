import FreeCADGui as Gui
import FreeCAD as App
from GMD.gates.sliding_gate import create_sliding_gate


class GMDCreateSlidingGate:
    def GetResources(self):
        return {
            "MenuText": "Create Sliding Gate",
            "ToolTip": "Create parametric sliding gate",
        }

    def Activated(self):
        create_sliding_gate()
        App.Console.PrintMessage("Poarta culisanta generata\n")

    def IsActive(self):
        return True


Gui.addCommand("GMD_CreateSlidingGate", GMDCreateSlidingGate())
