import pymupdf4llm
import re
from pathlib import Path

# ============================================================
# ✏️ SỬA 2 ĐƯỜNG DẪN NÀY
PDF_DIR    = Path(r"C:\Users\Lenovo\Documents\Viettel_RAG\data\raw_data")   # thư mục chứa 675 PDF
OUTPUT_DIR = Path(r"C:\Users\Lenovo\Documents\Viettel_RAG\data\parsed_docs") # output markdown
# ============================================================

OUTPUT_DIR.mkdir(exist_ok=True)

def clean_markdown(text: str) -> str:
    text = re.sub(r'\n\s*[-–]\s*\d+\s*[-–]\s*\n', '\n', text)
    text = re.sub(r'(Trang|Page)\s+\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    lines = text.split('\n')
    lines = [l for l in lines if len(l.strip()) == 0 or len(l.strip()) >= 8]
    text = re.sub(r'\n{3,}', '\n\n', '\n'.join(lines))
    return text.strip()

def parse_pdf(pdf_path: Path) -> str:
    try:
        md = pymupdf4llm.to_markdown(str(pdf_path))
        return clean_markdown(md)
    except Exception as e:
        print(f"  ⚠️  Lỗi: {pdf_path.name}: {e}")
        return ""

pdf_files = list(PDF_DIR.glob("*.pdf"))
print(f"📁 Tìm thấy {len(pdf_files)} PDF")

done = 0
failed = []

for i, pdf_file in enumerate(pdf_files):
    out_file = OUTPUT_DIR / f"{pdf_file.stem}.md"
    
    # Skip nếu đã parse rồi → resume được nếu bị lỗi giữa chừng
    if out_file.exists() and out_file.stat().st_size > 0:
        print(f"  ⏭️  [{i+1}/{len(pdf_files)}] Skip: {pdf_file.name}")
        done += 1
        continue
    
    text = parse_pdf(pdf_file)
    if text:
        out_file.write_text(text, encoding="utf-8")
        print(f"  ✅ [{i+1}/{len(pdf_files)}] {pdf_file.name} → {len(text):,} chars")
        done += 1
    else:
        failed.append(pdf_file.name)
        print(f"  ❌ [{i+1}/{len(pdf_files)}] {pdf_file.name}")

print(f"\n✅ Xong: {done}/{len(pdf_files)} file")
if failed:
    print(f"❌ Lỗi {len(failed)} file: {failed}")