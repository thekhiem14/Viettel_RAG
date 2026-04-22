import re
from typing import Optional


_PATTERN = re.compile(r'\bPublic_(\d{3})\b', re.IGNORECASE)


def extract_doc_id(text: str) -> Optional[str]:
    """
    Tìm 'Public_XXX' trong text (question hoặc note).
    Trả về chuỗi chuẩn hoá 'Public_001', hoặc None nếu không tìm thấy.
    """
    m = _PATTERN.search(text)
    if m:
        return f"Public_{m.group(1).zfill(3)}"
    return None


def extract_doc_id_from_row(question: str, note: Optional[str] = None) -> Optional[str]:
    """
    Ưu tiên note (nếu có), sau đó fallback sang question text.
    note chỉ được dùng sau khi đã classify thành call_document.
    """
    if note:
        doc_id = extract_doc_id(note)
        if doc_id:
            return doc_id
    return extract_doc_id(question)
