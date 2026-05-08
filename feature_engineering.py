# feature_engineering.py

import pandas as pd
import ta

df = pd.read_csv("historical_eth.csv")

# =========================
# BASIC INDICATORS
# =========================

df["rsi"] = ta.momentum.RSIIndicator(
    df["close"]
).rsi()

df["macd"] = ta.trend.MACD(
    df["close"]
).macd()

df["ema20"] = ta.trend.EMAIndicator(
    df["close"],
    window=20
).ema_indicator()

df["ema50"] = ta.trend.EMAIndicator(
    df["close"],
    window=50
).ema_indicator()

df["atr"] = ta.volatility.AverageTrueRange(
    df["high"],
    df["low"],
    df["close"]
).average_true_range()

# =========================
# ADVANCED FEATURES
# =========================

df["returns"] = (
    df["close"].pct_change()
)

df["volatility"] = (
    df["returns"]
    .rolling(10)
    .std()
)

df["momentum"] = (
    df["close"]
    - df["close"].shift(5)
)

df["volume_ma"] = (
    df["volume"]
    .rolling(20)
    .mean()
)

df["volume_spike"] = (
    df["volume"]
    / df["volume_ma"]
)

# =========================
# CANDLE STRUCTURE
# =========================

df["body"] = (
    abs(df["close"] - df["open"])
)

df["upper_wick"] = (
    df["high"]
    - df[["close", "open"]].max(axis=1)
)

df["lower_wick"] = (
    df[["close", "open"]].min(axis=1)
    - df["low"]
)

# =========================
# CLEAN
# =========================

df = df.dropna()

# =========================
# SAVE
# =========================

df.to_csv(
    "featured_eth.csv",
    index=False
)

print("FEATURES CREATED")