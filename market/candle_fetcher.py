# market/candle_fetcher.py

import requests
import pandas as pd
import time

from config.settings import (
    BASE_URL,
    SYMBOL
)


def get_candles(resolution="1m"):

    try:

        url = f"{BASE_URL}/v2/history/candles"

        end_time = int(time.time())

        # =========================
        # FETCH MORE HISTORY
        # =========================

        start_time = end_time - 7200

        params = {

            "symbol": SYMBOL,

            "resolution": resolution,

            "start": start_time,

            "end": end_time

        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        # =========================
        # VALIDATION
        # =========================

        if "result" not in data:

            print("INVALID RESPONSE")

            return None

        candles = data["result"]

        if len(candles) == 0:

            print("NO DATA FOUND")

            return None

        # =========================
        # DATAFRAME
        # =========================

        df = pd.DataFrame(candles)

        # =========================
        # SORT DATA
        # =========================

        df = df.sort_values(
            by="time"
        )

        df = df.reset_index(
            drop=True
        )

        # =========================
        # NUMERIC CONVERSION
        # =========================

        numeric_cols = [

            "open",

            "high",

            "low",

            "close",

            "volume"

        ]

        for col in numeric_cols:

            df[col] = (
                df[col]
                .astype(float)
            )

        return df

    except Exception as e:

        print("CANDLE ERROR:", e)

        return None