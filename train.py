import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

from data_preprocessing import prepare_data


SEC_IN_HOUR = 3600
TARGET_COL = "delta_time"
FEATURE_COLS = [
    'estimated_delta', 
    'route_distance_km', 
    'running_hour', 
    'estimated_distance_km', 
    'distance_error_sqr'
]


def rmse(y_true, y_pred):
    from sklearn.metrics import mean_squared_error

    return np.sqrt(mean_squared_error(y_true, y_pred))



def train_model(orders, train_size=0.8, final=False, random_state=43, save_dir="models"):

    if final:
        # Train on all data
        x_train, y_train = orders[FEATURE_COLS], orders[TARGET_COL]

    else:
        train_orders, val_orders  = train_test_split(orders, train_size=train_size, random_state=random_state)

        x_train, y_train = train_orders[FEATURE_COLS], train_orders[TARGET_COL]
        x_val, y_val = val_orders[FEATURE_COLS], val_orders[TARGET_COL]

    reg = GradientBoostingRegressor()
    reg.fit(x_train, y_train)

    if final:
        model_name = type(reg).__name__
        save_path = os.path.join(save_dir, f"{model_name}.pkl")

        joblib.dump(reg, save_path)
    
    else:
        y_pred = reg.predict(x_val)
        rmse_score = rmse(y_val, y_pred)
        print("RMSE:", rmse_score)


if __name__ == "__main__":
    orders_path = "data/orders.csv"
    nodes_path = "data/nodes.csv"
    median_speed = 30.0
    save_model = True

    print("Loading data...")
    orders = pd.read_csv(orders_path)
    nodes = nodes = pd.read_csv(nodes_path)

    print("Preparing data...")
    orders = prepare_data(orders, nodes)
    
    print("Training model...")
    train_model(orders, final=save_model)

    print("DONE")
