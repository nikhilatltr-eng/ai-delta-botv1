# orderflow/cvd.py

import orderflow.orderflow_store as store

def get_cvd():

    return round(
        store.cvd_value,
        2
    )