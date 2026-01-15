# Copilot / AI Agent Instructions for GMD

This repository contains small FreeCAD Python scripts for creating and manipulating simple geometry. The guidance below helps an AI coding agent be immediately productive in this codebase.

**What this project is**
- **Purpose:** simple FreeCAD scripts that create geometry (cube generator, profile factory).
- **Key files:** [main.py](main.py#L1-L22) — entry script that uses FreeCAD GUI; [profiles.py](profiles.py#L1-L20) — geometry factory functions; [utils.py](utils.py#L1-L20) — helper to create/return documents.

**How to run (interactive, expected environment)**
- This code imports `FreeCAD` and `FreeCADGui` and therefore is intended to run inside the FreeCAD Python environment (FreeCAD GUI). Example in FreeCAD's Python console:

```
import sys
sys.path.append(r'C:\IamandiS\GMD')
import main
main.run()
```

If you must run parts headless, avoid or conditionally guard any `Gui` calls (e.g., `Gui.activeDocument()`) — the repository currently does not include a headless mode.

**Patterns & conventions specific to this repo**
- Code uses FreeCAD API objects (`App`, `Gui`, `Part`). Preserve these API calls when editing.
- `profiles.py` functions (e.g., `teava_patrata(lungime, latura, grosime)`) return `Part.Shape` results (they construct shapes using `Part.makeBox`, `cut`, `translate`). Avoid changing them to directly add GUI objects — prefer returning shapes.
- `main.py` shows the pattern of creating/adding objects to the document (it uses `doc.addObject("Part::Box", "Cube_Test")`) and then calling `doc.recompute()` and GUI view commands. Follow this separation: factories return shapes; top-level scripts add/show shapes.
- Naming and messages are in Romanian (e.g., `teava_patrata`, console message). Preserve locale strings unless instructed otherwise.

**Editing guidance for AI**
- When adding geometry helpers, return Part shapes (like `profiles.py`) rather than mutating the document — this keeps functions testable and consistent.
- If you add new scripts that should run headless, detect `Gui` availability first: `if 'Gui' in globals(): ...` or wrap GUI calls in try/except.
- Keep public API minimal: utility functions in `utils.py` should be small helpers (e.g., `new_doc()`), and scripts that create complex scenes should be under `main.py` or new similarly-named entry scripts.

**Dependencies & integration points**
- Runtime dependency: FreeCAD (with `Part` and GUI modules). There is no pip/requirements file — this is a FreeCAD macro/script repository.
- No CI/tests present; there are no build scripts. Changes affecting geometry should be validated manually inside FreeCAD.

**Examples (quick snippets)**
- Create the cube (inside FreeCAD GUI console):

```
import sys
sys.path.append(r'C:\IamandiS\GMD')
import main
main.run()
```

- Use the profile factory interactively:

```
import sys, profiles, utils, Part
sys.path.append(r'C:\IamandiS\GMD')
doc = utils.new_doc('Test')
shape = profiles.teava_patrata(100, 20, 2)
Part.show(shape)
doc.recompute()
```

**Where to look when editing**
- Entry / GUI actions: [main.py](main.py#L1-L22)
- Geometry factories: [profiles.py](profiles.py#L1-L20)
- Document helpers: [utils.py](utils.py#L1-L20)

If anything here is unclear or you'd like broader changes (headless mode, tests, or a packaging script), tell me which direction you prefer and I will update this file.
