# execution/trailing_manager.py

def trailing_stop(
    current,
    atr,
    side
):

    if side == "BUY":

        return current - atr

    return current + atr