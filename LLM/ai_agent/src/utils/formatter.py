import json
import re
from typing import Optional


_VALID_ANSWERS = {'A', 'B', 'C', 'D'}


def _clean_document_answer(raw: str) -> str:
    """
    Trích đáp án A/B/C/D từ raw LLM output.
    Ví dụ: "Đáp án là A và B" → "AB", "A" → "A", "The answer is C." → "C"
    """
    # Tìm tất cả ký tự A/B/C/D đứng độc lập
    found = re.findall(r'\b([ABCD])\b', raw.upper())
    unique = []
    seen = set()
    for ch in found:
        if ch not in seen:
            seen.add(ch)
            unique.append(ch)

    if unique:
        return ''.join(sorted(unique, key=lambda x: 'ABCD'.index(x)))

    # Fallback: lấy ký tự đầu tiên nếu không parse được
    upper = raw.strip().upper()
    for ch in upper:
        if ch in _VALID_ANSWERS:
            return ch

    return raw.strip()


def format_output(
    row_id: str,
    function_code: str,
    raw_answer: str,
    time_response: float,
) -> dict:
    """
    Tạo output dict theo format đề bài.
    function_code: 'call_document' | 'call_api'
    """
    if function_code == 'call_document':
        function_result = _clean_document_answer(raw_answer)
    else:
        # call_api: giữ nguyên raw response từ model
        function_result = raw_answer.strip()

    return {
        'id': row_id,
        'function_code': function_code,
        'function_result': function_result,
        'time_response': round(time_response, 3),
    }


def write_results(results: list[dict], output_path: str):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Đã ghi {len(results)} kết quả → {output_path}")
