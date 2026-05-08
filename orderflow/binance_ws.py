# orderflow/binance_ws.py

import json
import threading
import websocket

import orderflow.orderflow_store as store

SYMBOL = "ethusdt"

DEPTH_WS = (
    f"wss://fstream.binance.com/ws/"
    f"{SYMBOL}@depth20@100ms"
)

TRADE_WS = (
    f"wss://fstream.binance.com/ws/"
    f"{SYMBOL}@trade"
)
# =========================
# DEPTH STREAM
# =========================

def on_depth_message(ws, message):

    try:

        data = json.loads(message)

        bids = data.get("b", [])
        asks = data.get("a", [])

        if not bids or not asks:
            return

        bid_volume = sum(
            float(b[1]) for b in bids[:10]
        )

        ask_volume = sum(
            float(a[1]) for a in asks[:10]
        )

        if ask_volume == 0:
            return

        store.imbalance_value = round(
            bid_volume / ask_volume,
            2
        )

    except Exception as e:

        print("DEPTH ERROR:", e)

# =========================
# TRADE STREAM
# =========================

def on_trade_message(ws, message):

    try:

        data = json.loads(message)

        qty = float(data["q"])

        is_sell = data["m"]

        # SELL MARKET ORDER
        if is_sell:

            store.volume_delta_value -= qty
            store.cvd_value -= qty

        # BUY MARKET ORDER
        else:

            store.volume_delta_value += qty
            store.cvd_value += qty

    except Exception as e:

        print("TRADE ERROR:", e)

# =========================
# START DEPTH SOCKET
# =========================

def run_depth():

    ws = websocket.WebSocketApp(
        DEPTH_WS,
        on_message=on_depth_message
    )

    ws.run_forever()

# =========================
# START TRADE SOCKET
# =========================

def run_trade():

    ws = websocket.WebSocketApp(
        TRADE_WS,
        on_message=on_trade_message
    )

    ws.run_forever()

# =========================
# START ENGINE
# =========================

def start_orderflow():

    depth_thread = threading.Thread(
        target=run_depth,
        daemon=True
    )

    trade_thread = threading.Thread(
        target=run_trade,
        daemon=True
    )

    depth_thread.start()
    trade_thread.start()

    print("ORDERFLOW ENGINE STARTED")