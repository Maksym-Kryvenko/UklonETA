import joblib
import pandas as pd


from data_preprocessing import prepare_data
from train import FEATURE_COLS


def make_predictions(reg, orders):
    x_test = orders[FEATURE_COLS]
    y_pred = reg.predict(x_test)
    return y_pred


def save_predictions(orders, y_pred, save_path):
    predictions = pd.DataFrame({
        "Id": orders.index,
        "Predicted": y_pred
    })
    predictions.to_csv(save_path, index=False)


if __name__ == "__main__":

    model_name = "GradientBoostingRegressor"
    model_path = f"models/{model_name}.pkl"
    prediction_path = f"results/{model_name}_predictions_final.csv"
    orders_path = "data/final_test.csv"
    nodes_path = "data/nodes_test.csv"

    print("Loading data...")
    orders = pd.read_csv(orders_path)
    nodes = nodes = pd.read_csv(nodes_path)

    print("Loading model...")
    reg = joblib.load(model_path)

    print("Preparing data...")
    orders = prepare_data(orders, nodes)

    print("Making predictions...")
    y_pred = make_predictions(reg, orders)

    print("Saving predictions...")
    save_predictions(orders, y_pred, save_path=prediction_path)
    print("DONE")
