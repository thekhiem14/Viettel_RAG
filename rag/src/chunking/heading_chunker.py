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

# Sentence splitter cho tiếng Việt:
#   - Tách tại dấu kết thúc câu (.?!) theo sau bởi khoảng trắng hoặc xuống dòng
#   - KHÔNG tách tại số thứ tự (1.1.2.), IP (192.168.1.0), viết tắt (TP.)
#   - Tách tại dòng trống (paragraph boundary)
_SENT_SPLIT_RE = re.compile(
    r"(?<="           # lookbehind — kí tự trước vị trí cắt
    r"(?<!\d)"        # KHÔNG phải số (tránh "1." "2.")
    r"(?<!\b[A-Z])"   # KHÔNG phải viết tắt 1 chữ hoa (tránh "TP." "Q.")
    r"[.?!]"          # dấu kết thúc câu
    r")"
    r"\s+"            # 1+ khoảng trắng/xuống dòng
    r"|"              # HOẶC
    r"\n{2,}"         # dòng trống (paragraph boundary)
)


def _clean_raw(raw: str) -> str:
    """Collapse 3+ blank lines thành 2."""
    return re.sub(r"\n{3,}", "\n\n", raw).strip()


def _clean_heading_title(title: str) -> str:
    return _HEADING_FORMAT_RE.sub("", title).strip()


def _split_sentences(text: str) -> list[str]:
    """Tách text thành danh sách câu, giữ nguyên dấu câu.

    Dùng regex split thông minh để tránh cắt sai tại số thứ tự,
    IP address, viết tắt.
    """
    # Loại bỏ markdown separator (---) trước khi split
    cleaned = re.sub(r"\n---+\s*$", "", text.strip())
    cleaned = re.sub(r"^---+\s*\n", "", cleaned)
    sentences = _SENT_SPLIT_RE.split(cleaned.strip())
    # Filter câu rỗng và câu chỉ chứa dấu ---
    result = []
    for s in sentences:
        s = s.strip().rstrip("-").strip()
        if s and len(s) > 2:
            result.append(s)
    return result


def _chunk_by_sentences(
    body: str,
    prefix: str,
    chunk_id_base: str,
    doc_id: str,
    heading_path: str,
    level: int,
) -> list[Chunk]:
    """Chia body text thành chunks theo sentence-aware strategy.

    Logic:
      1. Split body thành list câu
      2. Gom câu cho đến khi đạt TARGET_CHARS (hoặc vượt MAX_CHARS → dừng)
      3. Slide window: overlap CHUNK_OVERLAP_SENTENCES câu với chunk trước
      4. Nếu body ngắn → trả 1 chunk duy nhất
      5. Guard: nếu 1 câu đơn lẻ > MAX_CHARS → cắt theo từ (word fallback)
    """
    target = config.CHUNK_TARGET_CHARS
    max_chars = config.CHUNK_MAX_CHARS
    overlap_s = config.CHUNK_OVERLAP_SENTENCES

    sentences = _split_sentences(body)
    if not sentences:
        return []

    # Nếu toàn bộ body + prefix đủ nhỏ → 1 chunk
    full_text = prefix + body
    if len(full_text) <= max_chars:
        return [Chunk(
            chunk_id=f"{chunk_id_base}_00",
            doc_id=doc_id,
            heading_path=heading_path,
            level=level,
            char_count=len(full_text),
            text=full_text,
        )]

    chunks: list[Chunk] = []
    idx = 0
    start = 0  # index câu bắt đầu window hiện tại

    while start < len(sentences):
        # Gom câu cho đến khi đạt target hoặc hết câu
        window: list[str] = []
        window_chars = len(prefix)  # prefix luôn được thêm vào

        end = start
        while end < len(sentences):
            sent = sentences[end]
            new_chars = window_chars + len(sent) + (1 if window else 0)  # +1 cho khoảng trắng

            # Nếu thêm câu này sẽ vượt MAX_CHARS và đã có ít nhất 1 câu → dừng
            if new_chars > max_chars and window:
                break

            window.append(sent)
            window_chars = new_chars
            end += 1

            # Nếu đã đạt target và có đủ câu → có thể dừng
            if window_chars >= target:
                break

        if not window:
            break

        # Tạo chunk text
        chunk_body = " ".join(window)
        chunk_text = prefix + chunk_body
        chunks.append(Chunk(
            chunk_id=f"{chunk_id_base}_{idx:02d}",
            doc_id=doc_id,
            heading_path=heading_path,
            level=level,
            char_count=len(chunk_text),
            text=chunk_text,
        ))
        idx += 1

        # Đã hết câu → thoát
        if end >= len(sentences):
            break

        # Slide: lùi lại overlap_s câu để giữ context
        next_start = max(end - overlap_s, start + 1)
        start = next_start

    return chunks


def _parse_doc_block(doc_id: str, block: str) -> list[Chunk]:
    """Parse 1 block text của 1 document → list[Chunk].

    Block là phần text sau '# Public_XXX' đến '# Public_YYY' tiếp theo,
    không bao gồm dòng H1 separator.

    Strategy (Heading-first + Sentence-aware split):
      - Giữ heading boundary — mỗi heading section xử lý riêng
      - Section ngắn (< MIN_CHARS) → bỏ
      - Section vừa (≤ MAX_CHARS) → 1 chunk
      - Section dài (> MAX_CHARS) → sentence-based split với overlap
    """
    raw = _clean_raw(block)
    if not raw:
        return []

    min_chars = config.CHUNK_MIN_CHARS

    chunks: list[Chunk] = []
    chunk_counter = 0

    # --- Intro paragraph: text trước heading đầu tiên ---
    first_heading = _HEADING_RE.search(raw)
    if first_heading and first_heading.start() > 0:
        intro = raw[: first_heading.start()].strip()
        if len(intro) >= min_chars:
            prefix = f"[{doc_id}]\n\n"
            sub = _chunk_by_sentences(
                body=intro,
                prefix=prefix,
                chunk_id_base=f"{doc_id}_{chunk_counter:03d}",
                doc_id=doc_id,
                heading_path=doc_id,
                level=0,
            )
            chunks.extend(sub)
            chunk_counter += 1
    elif not first_heading:
        # Không có heading nào → toàn bộ block là intro
        intro = raw.strip()
        if len(intro) >= min_chars:
            prefix = f"[{doc_id}]\n\n"
            sub = _chunk_by_sentences(
                body=intro,
                prefix=prefix,
                chunk_id_base=f"{doc_id}_{chunk_counter:03d}",
                doc_id=doc_id,
                heading_path=doc_id,
                level=0,
            )
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

        # Guard: quá ngắn → bỏ
        if len(text_with_prefix) < min_chars:
            continue

        chunk_id_base = f"{doc_id}_{chunk_counter:03d}"

        sub = _chunk_by_sentences(
            body=body if body else "",
            prefix=prefix,
            chunk_id_base=chunk_id_base,
            doc_id=doc_id,
            heading_path=heading_path,
            level=level,
        )
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
    combined = config.DATA_DIR / "chroma_db" / "maybe_best_data.md"
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
