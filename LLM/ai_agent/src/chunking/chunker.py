import re
import json
from pathlib import Path


MIN_CHARS = 80
MAX_CHARS = 600
OVERLAP_CHARS = 80


def _split_large_text(text: str, breadcrumb: str) -> list[dict]:
    """Split text > MAX_CHARS thành sub-chunks, giữ breadcrumb prefix."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + MAX_CHARS
        if end < len(text):
            # Tìm điểm cắt gần nhất (dấu chấm, xuống dòng)
            cut = text.rfind('\n', start, end)
            if cut == -1:
                cut = text.rfind('. ', start, end)
            if cut == -1:
                cut = end
            else:
                cut += 1
        else:
            cut = len(text)

        chunk_text = text[start:cut].strip()
        if chunk_text:
            chunks.append({
                "breadcrumb": breadcrumb,
                "content": chunk_text,
                "full_text": f"[{breadcrumb}]\n\n{chunk_text}",
            })
        start = max(cut - OVERLAP_CHARS, cut)  # no overlap khi đã đến cuối
        if cut == len(text):
            break
    return chunks


def _parse_headings(md_text: str) -> list[dict]:
    """
    Parse markdown thành list sections, mỗi section có:
      level, title, content (text dưới heading đó, không tính sub-headings)
    """
    lines = md_text.split('\n')
    sections = []
    current = None

    for line in lines:
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            if current is not None:
                current['content'] = '\n'.join(current['content']).strip()
                sections.append(current)
            current = {
                'level': len(m.group(1)),
                'title': m.group(2).strip(),
                'content': [],
            }
        else:
            if current is not None:
                current['content'].append(line)

    if current is not None:
        current['content'] = '\n'.join(current['content']).strip()
        sections.append(current)

    return sections


def _build_breadcrumb(sections: list[dict], idx: int) -> str:
    """Xây breadcrumb từ doc_id tới heading hiện tại."""
    target_level = sections[idx]['level']
    path = []

    # Tìm ancestor headings
    for i in range(idx + 1):
        s = sections[i]
        if s['level'] < target_level:
            # Giữ ancestor gần nhất ở mỗi level
            while path and path[-1][0] >= s['level']:
                path.pop()
            path.append((s['level'], s['title']))
        elif i == idx:
            while path and path[-1][0] >= s['level']:
                path.pop()
            path.append((s['level'], s['title']))

    return ' > '.join(title for _, title in path)


def chunk_markdown_file(filepath: str, doc_id: str) -> list[dict]:
    """
    Đọc 1 file main.md, trả về list chunks.
    Mỗi chunk: {doc_id, heading_path, level, chunk_id, char_count, full_text}
    """
    with open(filepath, encoding='utf-8') as f:
        md_text = f.read()

    sections = _parse_headings(md_text)
    raw_chunks = []  # list of {breadcrumb, content}

    # Gộp section nhỏ vào section trước đó cùng cấp hoặc parent
    merged_sections = []
    for i, sec in enumerate(sections):
        breadcrumb = _build_breadcrumb(sections, i)
        content = sec['content']

        if not content:
            continue

        if len(content) < MIN_CHARS and merged_sections:
            # Gộp vào section trước
            merged_sections[-1]['content'] += '\n' + content
            merged_sections[-1]['full_text'] = (
                f"[{merged_sections[-1]['breadcrumb']}]\n\n{merged_sections[-1]['content']}"
            )
        else:
            merged_sections.append({
                'breadcrumb': breadcrumb,
                'level': sec['level'],
                'content': content,
                'full_text': f"[{breadcrumb}]\n\n{content}",
            })

    # Split section lớn
    chunk_counter = 0
    result = []
    for sec in merged_sections:
        if len(sec['content']) > MAX_CHARS:
            sub_chunks = _split_large_text(sec['content'], sec['breadcrumb'])
        else:
            sub_chunks = [sec]

        for sub in sub_chunks:
            result.append({
                'doc_id': doc_id,
                'heading_path': sub['breadcrumb'],
                'level': sec.get('level', 1),
                'chunk_id': f"{doc_id}_{chunk_counter:04d}",
                'char_count': len(sub['content']),
                'full_text': sub['full_text'],
                'content': sub['content'],
            })
            chunk_counter += 1

    return result


def chunk_all_documents(output_dir: str, chunks_output_path: str) -> int:
    """
    Glob tất cả Public_*/main.md trong output_dir.
    Ghi toàn bộ chunks ra chunks_output_path (JSON).
    Trả về tổng số chunks.
    """
    output_path = Path(output_dir)
    all_chunks = []

    md_files = sorted(output_path.glob('Public_*/main.md'))
    print(f"Tìm thấy {len(md_files)} file main.md")

    for md_file in md_files:
        doc_id = md_file.parent.name
        try:
            chunks = chunk_markdown_file(str(md_file), doc_id)
            all_chunks.extend(chunks)
            print(f"  {doc_id}: {len(chunks)} chunks")
        except Exception as e:
            print(f"  LỖI {doc_id}: {e}")

    with open(chunks_output_path, 'w', encoding='utf-8') as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"\nTổng: {len(all_chunks)} chunks → {chunks_output_path}")
    return len(all_chunks)
