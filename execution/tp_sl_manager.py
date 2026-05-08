# execution/tp_sl_manager.py

def calculate_tp_sl(
    entry,
    atr,
    side
):

    if side == "BUY":

        sl = entry - atr * 1.5

        tp = entry + atr * 3

    else:

        sl = entry + atr * 1.5

        tp = entry - atr * 3

    return sl, tp