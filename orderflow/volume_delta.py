# orderflow/volume_delta.py

import orderflow.orderflow_store as store

def get_volume_delta():

    return round(
        store.volume_delta_value,
        2
    )