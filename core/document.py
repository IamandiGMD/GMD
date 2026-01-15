import FreeCAD as App

def get_doc(name="GMD"):
    """
    Returnează documentul activ sau creează unul nou.
    """
    doc = App.ActiveDocument
    if doc is None or doc.Name != name:
        doc = App.newDocument(name)
    return doc
