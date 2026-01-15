import FreeCAD as App # type: ignore

def new_doc(name="Model"):
    """
    Creeaza sau returneaza documentul activ FreeCAD
    """
    doc = App.ActiveDocument
    if doc is None:
        doc = App.newDocument(name)
    return doc

def clear_document(doc):
    for obj in list(doc.Objects):
        doc.removeObject(obj.Name)
