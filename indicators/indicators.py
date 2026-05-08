# indicators/indicators.py

import ta

def add_indicators(df):

    df["ema20"] = ta.trend.ema_indicator(
        df["close"],
        20
    )

    df["ema50"] = ta.trend.ema_indicator(
        df["close"],
        50
    )

    df["rsi"] = ta.momentum.rsi(
        df["close"],
        14
    )

    macd = ta.trend.MACD(
        df["close"]
    )

    df["macd"] = macd.macd()

    df["macd_signal"] = macd.macd_signal()

    df["atr"] = ta.volatility.average_true_range(
        df["high"],
        df["low"],
        df["close"]
    )

    return df