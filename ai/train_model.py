# ai/train_model.py

import pandas as pd
import joblib

from xgboost import XGBClassifier

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    accuracy_score
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "training_data.csv"
)

# =========================
# FEATURES
# =========================

features = [

    "rsi",

    "macd",

    "ema20",

    "ema50",

    "atr",

    "volume"
]

X = df[features]

y = df["target"]

# =========================
# SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    shuffle=False
)

# =========================
# MODEL
# =========================

model = XGBClassifier(

    n_estimators=200,

    max_depth=5,

    learning_rate=0.05,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42
)

# =========================
# TRAIN
# =========================

model.fit(
    X_train,
    y_train
)

# =========================
# TEST
# =========================

preds = model.predict(X_test)

acc = accuracy_score(
    y_test,
    preds
)

print(f"Accuracy: {acc:.2f}")

# =========================
# SAVE
# =========================

joblib.dump(
    model,
    "models/xgb_model.pkl"
)

print("REAL AI MODEL TRAINED")