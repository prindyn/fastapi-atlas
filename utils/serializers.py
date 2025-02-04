from bson import ObjectId
from typing import List, Dict, Any

def individual_serial(document: Dict[str, Any]) -> Dict[str, Any]:
    if not document:
        return None
    return {key: str(value) if isinstance(value, ObjectId) else value for key, value in document.items()}

def individual_serials(documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [individual_serial(doc) for doc in documents]