from __future__ import annotations

import time
from contextlib import contextmanager
from typing import Generator


class Timer:
    """Context manager đo wall-clock time. Kết quả lưu trong .elapsed (seconds)."""

    def __init__(self) -> None:
        self.elapsed: float = 0.0
        self._start: float = 0.0

    def __enter__(self) -> "Timer":
        self._start = time.perf_counter()
        return self

    def __exit__(self, *_) -> None:
        self.elapsed = time.perf_counter() - self._start


@contextmanager
def timed(label: str = "") -> Generator[Timer, None, None]:
    """Context manager tiện lợi khi không cần giữ object Timer."""
    t = Timer()
    with t:
        yield t
    if label:
        try:
            import config
            disable_console = getattr(config, "DISABLE_CONSOLE_LOG", False)
        except (ImportError, AttributeError):
            disable_console = False
        if not disable_console:
            print(f"[timer] {label}: {t.elapsed:.3f}s")
