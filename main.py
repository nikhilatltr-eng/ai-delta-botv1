import time

from market.candle_fetcher import (
    get_candles
)

from indicators.indicators import (
    add_indicators
)

from indicators.multi_timeframe import (
    get_multi_timeframe_trend
)

from orderflow.imbalance import (
    get_imbalance
)

from orderflow.volume_delta import (
    get_volume_delta
)

from orderflow.cvd import (
    get_cvd
)

from ai.ml_model import AIModel

from strategy.strategy import (
    generate_signal
)

from orderflow.binance_ws import (
    start_orderflow
)

from alerts.telegram_alerts import (
    send_alert,
    validate_telegram_config
)

# =========================
# START SYSTEM
# =========================

ai = AIModel()

start_orderflow()

validate_telegram_config()

# =========================
# TELEGRAM CONTROL
# =========================

last_signal = None

# =========================
# MAIN LOOP
# =========================

while True:

    try:

        # =========================
        # FETCH CANDLES
        # =========================

        df = get_candles()

        if df is None:

            print("NO DATA")

            time.sleep(2)

            continue

        # =========================
        # SAFE MINIMUM CANDLES
        # =========================

        if len(df) < 60:

            print(
                "WAITING FOR MORE CANDLES..."
            )

            time.sleep(2)

            continue

        # =========================
        # ADD INDICATORS
        # =========================

        df = add_indicators(df)

        latest = df.iloc[-1]

        # =========================
        # ORDERFLOW
        # =========================

        imbalance = get_imbalance()

        volume_delta = get_volume_delta()

        cvd = get_cvd()

        # =========================
        # MULTI TIMEFRAME TREND
        # =========================

        trend_score = (
            get_multi_timeframe_trend()
        )

        # =========================
        # AI PREDICTION
        # =========================

        ai_prob = ai.predict(

            latest["rsi"],

            latest["macd"],

            latest["ema20"],

            latest["ema50"],

            latest["atr"],

            latest["volume"]
        )

        # =========================
        # STRATEGY
        # =========================

        signal = generate_signal(

            df,

            ai_prob,

            imbalance,

            volume_delta,

            cvd,

            trend_score
        )

        # =========================
        # TELEGRAM ALERTS
        # =========================

        if signal != last_signal:

            if signal != "HOLD":

                message = f"""

🚨 SIGNAL: {signal}

🤖 AI PROBABILITY: {ai_prob:.2f}

📊 IMBALANCE: {imbalance}

📈 VOLUME DELTA: {volume_delta}

💹 CVD: {cvd}

📡 TREND SCORE: {trend_score}

"""

                alert_sent = send_alert(message)

                if not alert_sent:
                    print("TELEGRAM ALERT FAILED")

            last_signal = signal

        # =========================
        # TERMINAL OUTPUT
        # =========================

        print("=" * 40)

        print(f"SIGNAL: {signal}")

        print(
            f"AI PROBABILITY: {ai_prob:.2f}"
        )

        print(
            f"IMBALANCE: {imbalance}"
        )

        print(
            f"VOLUME DELTA: {volume_delta}"
        )

        print(f"CVD: {cvd}")

        print(
            f"TREND SCORE: {trend_score}"
        )

        print("=" * 40)

        time.sleep(2)

    except Exception as e:

        print("ERROR:", e)

        time.sleep(2)
