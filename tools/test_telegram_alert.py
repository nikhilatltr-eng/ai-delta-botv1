import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from alerts.telegram_alerts import send_alert


if __name__ == "__main__":
    ok = send_alert("AI Delta Bot Telegram test alert")
    raise SystemExit(0 if ok else 1)
