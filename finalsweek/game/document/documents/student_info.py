from game.document.documents.document_base import DocumentBase

class StudentInfo(DocumentBase):
    _field_definitions = {
        "id": str,
        "first_name": str,
        "last_name": str,
        "backstory": str,
        "perk_name": str,
        "perk_description": str,
        "fear_name": str,
        "fear_description": str
    }