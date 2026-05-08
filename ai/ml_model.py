# ai/ml_model.py

import joblib
import numpy as np

class AIModel:

    def __init__(self):

        self.model = joblib.load(
            "models/xgb_model.pkl"
        )

    def predict(
        self,
        rsi,
        macd,
        ema20,
        ema50,
        atr,
        volume
    ):

        try:

            features = np.array([
                [
                    rsi,
                    macd,
                    ema20,
                    ema50,
                    atr,
                    volume
                ]
            ])

            prediction = (
                self.model.predict_proba(features)[0][1]
            )

            return float(prediction)

        except Exception as e:

            print("ML ERROR:", e)

            return 0.5