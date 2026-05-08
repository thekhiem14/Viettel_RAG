import os
from pathlib import Path

# from dotenv import load_dotenv

# load_dotenv()

ROOT = Path(__file__).parent  # Viettel_RAG/

# --- Raw data (KHÔNG SỬA) ---
DATA_DIR       = Path(os.getenv("DATA_DIR",       str(ROOT / "data")))
DOC_MD_DIR     = Path(os.getenv("DOC_MD_DIR",     str(ROOT / "data" / "document")))
MINERU_OUT_DIR = Path(os.getenv("MINERU_OUT_DIR", str(ROOT / "training_data_update" / "output")))

API_CSV       = DATA_DIR / "Tài_liệu_config_API_Doc_api_for_contest.csv"
API_ALIAS_CSV = DATA_DIR / "Tài_liệu_config_API_Doc_alias_for_contest.csv"
EXAMPLE_CSV        = DATA_DIR / "example_data_example_question.csv"
EXAMPLE_RESULT_CSV = DATA_DIR / "example_data_example_result.csv"
TEST_CSV           = DATA_DIR / "Test_data.csv"

# --- Artifacts (BUILT) ---
ARTIFACTS_DIR = Path(os.getenv("ARTIFACTS_DIR", str(ROOT / "artifacts")))
SYNTHETIC_DIR = Path(os.getenv("SYNTHETIC_DIR", str(ROOT / "synthetic")))
OUTPUTS_DIR   = Path(os.getenv("OUTPUTS_DIR",   str(ROOT / "outputs")))
LOGS_DIR      = Path(os.getenv("LOGS_DIR",      str(ROOT / "logs")))

API_ALIASES = ARTIFACTS_DIR / "api" / "aliases.json"
DOC_CHUNKS  = ARTIFACTS_DIR / "docs" / "chunks.jsonl"
DOC_FAISS   = ARTIFACTS_DIR / "docs" / "faiss.index"
DOC_BM25    = ARTIFACTS_DIR / "docs" / "bm25.pkl"
API_SCHEMAS = ARTIFACTS_DIR / "api" / "schemas.json"
API_FAISS   = ARTIFACTS_DIR / "api" / "faiss.index"
API_BM25    = ARTIFACTS_DIR / "api" / "bm25.pkl"
API_FUZZY   = ARTIFACTS_DIR / "api" / "fuzzy_targets.json"
CLASSIFIER  = ARTIFACTS_DIR / "classifier" / "intent.pkl"

# --- Models ---
EMBED_MODEL      = "BAAI/bge-m3"
RERANK_MODEL     = "BAAI/bge-reranker-v2-m3"
LLM_MODEL        = "Qwen/Qwen3-4B"
LLM_QUANTIZATION = "4bit"

# --- Chunking ---
CHUNK_MIN_CHARS = 80
CHUNK_MAX_CHARS = 600
CHUNK_OVERLAP   = 80

# --- Retrieval ---
BM25_TOP_K         = 20
FAISS_TOP_K        = 20
RRF_K              = 60
RERANK_TOP_K       = 5
API_RETRIEVE_TOP_K = 5   # TODO: test top_k=10 — nếu latency cho phép thì tăng

# --- Intent (cosine vs API embeddings) ---
INTENT_COSINE_THRESHOLD = 0.55  # TODO: tune trên example_data 100 câu

# --- LLM ---
LLM_MAX_NEW_TOKENS = 512
LLM_THINKING_MODE  = False
LLM_TEMPERATURE    = 0.0

# --- Gemini ---
GEMINI_API_KEY     = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL       = "gemini-1.5-flash"
GEMINI_SLEEP       = 4.0
GEMINI_MAX_RETRIES = 3

# --- Eval ---
EVAL_ACCURACY_THRESHOLD = 0.70
TIME_RESPONSE_TARGET    = 15.0


def ensure_dirs() -> None:
    """Tạo các output directories nếu chưa tồn tại. Gọi 1 lần khi bắt đầu script."""
    for d in [ARTIFACTS_DIR / "docs", ARTIFACTS_DIR / "api", ARTIFACTS_DIR / "classifier",
              SYNTHETIC_DIR, OUTPUTS_DIR / "eval", OUTPUTS_DIR / "submission", LOGS_DIR]:
        d.mkdir(parents=True, exist_ok=True)
