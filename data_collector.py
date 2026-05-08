import requests
import pandas as pd
import time

BASE_URL = "https://cdn-ind.testnet.deltaex.org"

SYMBOL = "ETHUSD"

all_data = []

end_time = int(time.time())

for i in range(200):

    start_time = end_time - 3600

    url = f"{BASE_URL}/v2/history/candles"

    params = {
        "symbol": SYMBOL,
        "resolution": "1m",
        "start": start_time,
        "end": end_time
    }

    response = requests.get(
        url,
        params=params
    ).json()

    if "result" not in response:

        print(response)

        break

    candles = response["result"]

    all_data.extend(candles)

    print(f"Collected {len(candles)} candles")

    end_time = start_time

    time.sleep(0.5)

df = pd.DataFrame(all_data)

df.to_csv(
    "historical_eth.csv",
    index=False
)

print("REAL DATA SAVED")