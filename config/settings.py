# config/settings.py

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("DELTA_API_KEY")
API_SECRET = os.getenv("DELTA_API_SECRET")

BASE_URL = os.getenv("BASE_URL")
WS_URL = os.getenv("WS_URL")

SYMBOL = os.getenv("SYMBOL")

RISK_PER_TRADE = 0.01

LEVERAGE = 3

MIN_AI_PROBABILITY = 0.20