@@ -0,0 +1,26 @@
import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    """Load the JSON object the agent must write to /app/report.json."""
    assert REPORT.exists(), "no /app/report.json found"
    with REPORT.open() as f:
        return json.load(f)


def test_total_requests():
    """Criterion 1: 'total_requests' == number of non-empty lines in the log (6)."""
    assert _load()["total_requests"] == 6


def test_unique_ips():
    """Criterion 2: 'unique_ips' == number of distinct client IPs (3)."""
    assert _load()["unique_ips"] == 3


def test_top_path():
    """Criterion 3: 'top_path' == the most-requested path (/index.html)."""
    assert _load()["top_path"] == "/index.html"
