# config/settings.py

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("DELTA_API_KEY")
API_SECRET = os.getenv("DELTA_API_SECRET")

BASE_URL = os.getenv("BASE_URL")
WS_URL = os.getenv("WS_URL")

SYMBOL = os.getenv("SYMBOL")

TELEGRAM_BOT_TOKEN = (
    os.getenv("TELEGRAM_BOT_TOKEN")
    or os.getenv("TELEGRAM_TOKEN")
)

TELEGRAM_CHAT_ID = (
    os.getenv("TELEGRAM_CHAT_ID")
    or os.getenv("CHAT_ID")
)

TELEGRAM_ENABLED = (
    os.getenv("TELEGRAM_ENABLED", "true")
    .strip()
    .lower()
    not in {"0", "false", "no", "off"}
)

RISK_PER_TRADE = 0.01

LEVERAGE = 3

MIN_AI_PROBABILITY = 0.20
