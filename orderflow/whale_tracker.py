# orderflow/whale_tracker.py

WHALE_SIZE = 100000

def detect_whale(trade):

    value = (
        trade["price"] *
        trade["size"]
    )

    return value > WHALE_SIZE