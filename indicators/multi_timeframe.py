# indicators/multi_timeframe.py

from market.candle_fetcher import (
    get_candles
)

from indicators.indicators import (
    add_indicators
)

def get_multi_timeframe_trend():

    try:

        score = 0

        timeframes = [
            "1m",
            "5m",
            "15m"
        ]

        for tf in timeframes:

            df = get_candles(tf)

            if df is None:
                continue

            if len(df) < 60:
                continue

            df = add_indicators(df)

            latest = df.iloc[-1]

            if latest["ema20"] > latest["ema50"]:
                score += 1

            else:
                score -= 1

        return score

    except Exception as e:

        print("MTF ERROR:", e)

        return 0