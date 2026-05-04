from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from shared.types import Chunk

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)


def _split_long_text(text: str, chunk_id_base: str, heading_path: str, level: int) -> list[Chunk]:
    """Chia đoạn text > CHUNK_MAX_CHARS thành các sub-chunk có overlap."""
    max_c = config.CHUNK_MAX_CHARS
    overlap = config.CHUNK_OVERLAP
    chunks: list[Chunk] = []
    start = 0
    idx = 0

    while start < len(text):
        end = start + max_c
        if end < len(text):
            # tìm điểm cắt tại dấu xuống dòng gần nhất
            newline = text.rfind("\n", start, end)
            if newline > start:
                end = newline
        segment = text[start:end].strip()
        if segment:
            chunks.append(Chunk(
                chunk_id=f"{chunk_id_base}_{idx:02d}",
                doc_id=chunk_id_base.split("_")[0] + "_" + chunk_id_base.split("_")[1],
                heading_path=heading_path,
                level=level,
                char_count=len(segment),
                text=segment,
            ))
            idx += 1
        start = end - overlap if end < len(text) else len(text)

    return chunks


def chunk_document(md_path: Path, doc_id: str) -> list[Chunk]:
    """Parse 1 file main.md → list[Chunk] theo heading-based + breadcrumb.

    Args:
        md_path: đường dẫn tới Public_XXX/main.md
        doc_id:  "Public_001"
    """
    raw = md_path.read_text(encoding="utf-8")

    # Tách markdown thành các section theo heading
    # Mỗi section = (heading_level, heading_text, body_text)
    sections: list[tuple[int, str, str]] = []
    matches = list(_HEADING_RE.finditer(raw))

    for i, m in enumerate(matches):
        level = len(m.group(1))
        title = m.group(2).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        body = raw[body_start:body_end].strip()
        sections.append((level, title, body))

    # Xây dựng breadcrumb stack và tạo chunks
    chunks: list[Chunk] = []
    breadcrumb: list[str] = []   # stack tiêu đề ancestor theo level
    chunk_counter = 0

    for level, title, body in sections:
        # Cập nhật breadcrumb: bỏ các heading cùng level hoặc sâu hơn
        breadcrumb = breadcrumb[: level - 1]
        breadcrumb.append(title)

        heading_path = " > ".join(breadcrumb)
        prefix = f"[{doc_id} > {heading_path}]\n\n"

        text_with_prefix = prefix + body if body else prefix.strip()
        char_count = len(text_with_prefix)

        chunk_id_base = f"{doc_id}_{chunk_counter:03d}"

        if char_count < config.CHUNK_MIN_CHARS:
            # Quá ngắn: bỏ qua (sẽ được cover bởi parent context qua breadcrumb)
            pass
        elif char_count <= config.CHUNK_MAX_CHARS:
            chunks.append(Chunk(
                chunk_id=chunk_id_base,
                doc_id=doc_id,
                heading_path=heading_path,
                level=level,
                char_count=char_count,
                text=text_with_prefix,
            ))
            chunk_counter += 1
        else:
            # Quá dài: split, mỗi sub-chunk giữ prefix breadcrumb
            sub_chunks = _split_long_text(
                text=text_with_prefix,
                chunk_id_base=chunk_id_base,
                heading_path=heading_path,
                level=level,
            )
            chunks.extend(sub_chunks)
            chunk_counter += 1

    return chunks


def chunk_all_documents(mineru_out_dir: Path | None = None) -> list[Chunk]:
    """Chunk toàn bộ documents trong MINERU_OUT_DIR.

    Args:
        mineru_out_dir: override path, mặc định dùng config.MINERU_OUT_DIR
    """
    base_dir = mineru_out_dir or config.MINERU_OUT_DIR
    all_chunks: list[Chunk] = []

    md_files = sorted(base_dir.glob("*/main.md"))
    for md_path in md_files:
        doc_id = md_path.parent.name   # "Public_001"
        try:
            chunks = chunk_document(md_path, doc_id)
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"[chunker] skip {doc_id}: {e}")

    return all_chunks
