# orderflow/imbalance.py

import orderflow.orderflow_store as store

def get_imbalance():

    return round(
        store.imbalance_value,
        2
    )