import numpy as np
import pandas as pd


MEDIAN_SPEED = 30.0
SEC_IN_HOUR = 3600


def fix_dates(orders):
    orders["running_time"] = pd.to_datetime(orders.running_time)
    # orders["completed_time"] = pd.to_datetime(orders.completed_time)
    # orders["delta_time"] = orders.delta_time.astype(int)


def fill_na(nodes, speed_value):
    nodes["speed"] = nodes.speed.fillna(speed_value)
    return nodes


def generate_features(orders, nodes):
    orders = orders.set_index("Id")

    nodes["node_distance_km"] = nodes["distance"] / 1000
    orders["estimated_distance_km"] = nodes.groupby("Id")["node_distance_km"].sum()

    estimated_delta = nodes.groupby('Id').apply(lambda g: (g["node_distance_km"] / g["speed"]).sum() * SEC_IN_HOUR)
    orders["estimated_delta"] = estimated_delta

    orders["running_hour"] = orders.running_time.dt.hour

    orders["distance_error"] = orders["route_distance_km"] - orders["estimated_distance_km"]
    orders["distance_error_sqr"] = np.square(orders["distance_error"])

    return orders

def prepare_data(orders, nodes):

    fix_dates(orders)
    nodes = fill_na(nodes, speed_value=MEDIAN_SPEED)
    orders = generate_features(orders, nodes)

    return orders