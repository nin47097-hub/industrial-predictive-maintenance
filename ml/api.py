from flask import Flask, request, jsonify
from prediction.predict import predict_machine
import pandas as pd
import math

app = Flask(__name__)

machines = pd.read_csv("dataset/all_machines.csv")

print(machines["machine_id"].unique())


# -----------------------------
# Convert NaN to None
# -----------------------------

def clean_data(data):

    cleaned = {}

    for key, value in data.items():

        if pd.isna(value):
            cleaned[key] = None
        else:
            cleaned[key] = value

    return cleaned


# -----------------------------
# Get all machines
# -----------------------------

@app.route("/machines", methods=["GET"])
def get_machines():

    machine_list = []

    for machine_id in machines["machine_id"].unique():

        machine = machines[
            machines["machine_id"] == machine_id
        ]

        latest_machine = machine.iloc[-1].to_dict()

        latest_machine = clean_data(latest_machine)

        machine_list.append(latest_machine)

    return jsonify(machine_list)


# -----------------------------
# Get one machine
# -----------------------------

@app.route("/machines/<machine_id>", methods=["GET"])
def get_machine(machine_id):

    machine = machines[
        machines["machine_id"] == machine_id
    ]

    if machine.empty:

        return jsonify({
            "message": "Machine not found"
        }), 404

    machine = machine.iloc[-1].to_dict()

    machine = clean_data(machine)

    return jsonify(machine)


# -----------------------------
# ML Prediction
# -----------------------------

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    result = predict_machine(
        data["machine_id"],
        data["production_line"],
        data["machine_type"],
        data["temperature"],
        data["vibration"],
        data["rpm"],
        data["current"],
        data["voltage"],
        data["torque"],
        data["pressure"],
        data["flow_rate"],
        data["load_percentage"],
        data["frequency"],
        data["power_factor"],
        data["cycle_time"],
        data["operating_hours"],
        data["maintenance_count"]
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)