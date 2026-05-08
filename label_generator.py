import pandas as pd

df = pd.read_csv(
    "featured_eth.csv"
)

future_close = df["close"].shift(-5)

df["target"] = (
    future_close > df["close"]
).astype(int)

df.dropna(inplace=True)

df.to_csv(
    "training_data.csv",
    index=False
)

print("TRAINING DATA CREATED")