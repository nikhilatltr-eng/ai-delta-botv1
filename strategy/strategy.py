# strategy/strategy.py

def generate_signal(
    df,
    ai_prob,
    imbalance,
    volume_delta,
    cvd,
    trend_score
):

    latest = df.iloc[-1]

    ema20 = latest["ema20"]
    ema50 = latest["ema50"]

    bullish_trend = ema20 > ema50
    bearish_trend = ema20 < ema50

    buy_score = 0
    sell_score = 0

    # =========================
    # AI
    # =========================

    if ai_prob > 0.60:
        buy_score += 2

    if ai_prob < 0.40:
        sell_score += 2

    # =========================
    # TREND
    # =========================

    if bullish_trend:
        buy_score += 1

    if bearish_trend:
        sell_score += 1

    # =========================
    # IMBALANCE
    # =========================

    if imbalance > 1.2:
        buy_score += 1

    if imbalance < 0.8:
        sell_score += 1

    # =========================
    # VOLUME DELTA
    # =========================

    if volume_delta > 0:
        buy_score += 1

    if volume_delta < 0:
        sell_score += 1

    # =========================
    # CVD
    # =========================

    if cvd > 0:
        buy_score += 1

    if cvd < 0:
        sell_score += 1

    # =========================
    # TREND SCORE
    # =========================

    if trend_score > 0:
        buy_score += 1

    if trend_score < 0:
        sell_score += 1

    # =========================
    # FINAL DECISION
    # =========================

    print(f"BUY SCORE: {buy_score}")
    print(f"SELL SCORE: {sell_score}")

    if buy_score >= 5:
        return "STRONG BUY"

    if sell_score >= 5:
        return "STRONG SELL"

    if buy_score > sell_score:
        return "BUY"

    if sell_score > buy_score:
        return "SELL"

    return "HOLD"