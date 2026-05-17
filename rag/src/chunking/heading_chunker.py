from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import config
from shared.types import Chunk

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)
_HEADING_FORMAT_RE = re.compile(r"[\*\_`]+")
# H1 dùng làm doc separator trong file tổng hợp: "# Public_001"
_DOC_SEPARATOR_RE = re.compile(r"^# (Public_\d+)\s*$", re.MULTILINE)


def _clean_raw(raw: str) -> str:
    """Collapse 3+ blank lines thành 2."""
    return re.sub(r"\n{3,}", "\n\n", raw).strip()


def _clean_heading_title(title: str) -> str:
    return _HEADING_FORMAT_RE.sub("", title).strip()


def _split_long_text(text: str, chunk_id_base: str, heading_path: str, level: int) -> list[Chunk]:
    """Chia đoạn > CHUNK_MAX_CHARS thành sub-chunks có overlap."""
    max_c = config.CHUNK_MAX_CHARS
    overlap = config.CHUNK_OVERLAP
    chunks: list[Chunk] = []
    start = 0
    idx = 0

    min_cut = int(max_c * 0.8)  # chỉ cắt sớm nếu đoạn đã đủ 80% window

    while start < len(text):
        end = start + max_c
        if end < len(text):
            # Ưu tiên 1: cắt tại newline cuối trong 20% cuối của window
            newline = text.rfind("\n", start + min_cut, end)
            if newline > start + min_cut:
                end = newline
            else:
                # Ưu tiên 2: cắt tại word boundary (space/newline) gần end nhất,
                # nhưng vẫn phải sau min_cut
                space = max(
                    text.rfind(" ", start + min_cut, end),
                    text.rfind("\n", start + min_cut, end),
                )
                if space > start + min_cut:
                    end = space
        seg = text[start:end].strip()
        if seg:
            doc_id = "_".join(chunk_id_base.split("_")[:2])
            chunks.append(Chunk(
                chunk_id=f"{chunk_id_base}_{idx:02d}",
                doc_id=doc_id,
                heading_path=heading_path,
                level=level,
                char_count=len(seg),
                text=seg,
            ))
            idx += 1
        next_start = end - overlap if end < len(text) else len(text)
        # Đảm bảo tiến tối thiểu 1 ký tự
        start = max(next_start, start + 1)

    return chunks


def _parse_doc_block(doc_id: str, block: str) -> list[Chunk]:
    """Parse 1 block text của 1 document → list[Chunk].

    Block là phần text sau '# Public_XXX' đến '# Public_YYY' tiếp theo,
    không bao gồm dòng H1 separator.
    """
    raw = _clean_raw(block)
    if not raw:
        return []

    chunks: list[Chunk] = []
    chunk_counter = 0

    # --- Intro paragraph: text trước heading đầu tiên ---
    first_heading = _HEADING_RE.search(raw)
    if first_heading and first_heading.start() > 0:
        intro = raw[: first_heading.start()].strip()
        if len(intro) >= config.CHUNK_MIN_CHARS:
            prefix = f"[{doc_id}]\n\n"
            text_with_prefix = prefix + intro
            if len(text_with_prefix) <= config.CHUNK_MAX_CHARS:
                chunks.append(Chunk(
                    chunk_id=f"{doc_id}_{chunk_counter:03d}",
                    doc_id=doc_id,
                    heading_path=doc_id,
                    level=0,
                    char_count=len(text_with_prefix),
                    text=text_with_prefix,
                ))
                chunk_counter += 1
            else:
                sub = _split_long_text(text_with_prefix, f"{doc_id}_{chunk_counter:03d}", doc_id, 0)
                chunks.extend(sub)
                chunk_counter += 1

    # --- Heading-based sections (H2–H5, bỏ qua H1 vì là separator) ---
    matches = [m for m in _HEADING_RE.finditer(raw) if len(m.group(1)) > 1]

    sections: list[tuple[int, str, str]] = []
    for i, m in enumerate(matches):
        level = len(m.group(1))
        title = _clean_heading_title(m.group(2))
        if not title:
            continue
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        body = raw[body_start:body_end].strip()
        sections.append((level, title, body))

    breadcrumb: list[str] = []
    for level, title, body in sections:
        breadcrumb = breadcrumb[: level - 2]  # H2=level2 → breadcrumb depth 0
        breadcrumb.append(title)

        heading_path = " > ".join(breadcrumb)
        prefix = f"[{doc_id} > {heading_path}]\n\n"
        text_with_prefix = (prefix + body) if body else prefix.strip()
        char_count = len(text_with_prefix)
        chunk_id_base = f"{doc_id}_{chunk_counter:03d}"

        if char_count < config.CHUNK_MIN_CHARS:
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
            sub = _split_long_text(text_with_prefix, chunk_id_base, heading_path, level)
            chunks.extend(sub)
            chunk_counter += 1

    return chunks


def chunk_combined_document(md_path: Path) -> list[Chunk]:
    """Parse file tổng hợp chứa 380 docs phân tách bằng '# Public_XXX'.

    Args:
        md_path: đường dẫn tới chroma_documents.md
    """
    raw = md_path.read_text(encoding="utf-8")

    # Tìm tất cả doc separator và split
    separators = list(_DOC_SEPARATOR_RE.finditer(raw))
    if not separators:
        raise ValueError(f"Không tìm thấy doc separator '# Public_XXX' trong {md_path}")

    all_chunks: list[Chunk] = []
    for i, sep in enumerate(separators):
        doc_id = sep.group(1)
        block_start = sep.end()
        block_end = separators[i + 1].start() if i + 1 < len(separators) else len(raw)
        block = raw[block_start:block_end]
        try:
            all_chunks.extend(_parse_doc_block(doc_id, block))
        except Exception as e:
            print(f"[chunker] skip {doc_id}: {e}")

    return all_chunks


def chunk_document(md_path: Path, doc_id: str) -> list[Chunk]:
    """Parse 1 file Public_XXX.md riêng lẻ → list[Chunk].

    Args:
        md_path: đường dẫn tới Public_XXX.md
        doc_id:  "Public_001"
    """
    raw = md_path.read_text(encoding="utf-8")
    return _parse_doc_block(doc_id, raw)


def chunk_all_documents(doc_md_dir: Path | None = None) -> list[Chunk]:
    """Chunk toàn bộ: ưu tiên file tổng hợp nếu tồn tại, fallback sang từng Public_XXX.md.

    Args:
        doc_md_dir: override path, mặc định dùng config.DOC_MD_DIR
    """
    # Ưu tiên file tổng hợp từ chroma_db
    combined = config.DATA_DIR / "chroma_db" / "chroma_documents.md"
    if combined.exists():
        print(f"[chunker] using combined file: {combined}")
        return chunk_combined_document(combined)

    # Fallback: từng file riêng lẻ
    base_dir = doc_md_dir or config.DOC_MD_DIR
    all_chunks: list[Chunk] = []
    md_files = sorted(base_dir.glob("Public_*.md"))
    for md_path in md_files:
        doc_id = md_path.stem
        try:
            all_chunks.extend(chunk_document(md_path, doc_id))
        except Exception as e:
            print(f"[chunker] skip {doc_id}: {e}")
    return all_chunks
