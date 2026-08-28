import os
import joblib
import pandas as pd
import gzip
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

health_model = joblib.load(
    os.path.join(BASE_DIR, "models", "health_model.pkl")
)

health_features = joblib.load(
    os.path.join(BASE_DIR, "models", "health_features.pkl")
)

with gzip.open(
    os.path.join(BASE_DIR, "models", "failure_model.pkl.gz"),
    "rb"
) as f:
    failure_model = joblib.load(f)

failure_features = joblib.load(
    os.path.join(BASE_DIR, "models", "failure_features.pkl")
)

failure_type_model = joblib.load(
    os.path.join(BASE_DIR, "models", "failure_type_model.pkl")
)

failure_type_features = joblib.load(
    os.path.join(BASE_DIR, "models", "failure_type_features.pkl")
)

def get_health_status(health_score):

    if health_score >= 80:
        return "Healthy"

    elif health_score >= 60:
        return "Moderate"

    elif health_score >= 40:
        return "Degraded"

    else:
        return "Critical"


def maintenance_schedule(
    failure_status,
    failure_probability,
    health_score
):

    if failure_status == "YES":
        return "Immediate maintenance required"

    elif failure_probability >= 90:
        return "Maintenance required within 2 days"

    elif failure_probability >= 75:
        return "Maintenance required within 3 days"

    elif health_score >= 80:
        return "No maintenance required"

    elif health_score > 50:
        return "Maintenance required within 7 days"

    elif health_score > 20:
        return "Maintenance required within 3 days"

    else:
        return "Immediate maintenance required"



def predict_machine(
    machine_id,
    production_line,
    machine_type,
    temperature,
    vibration,
    rpm,
    current,
    voltage,
    torque,
    pressure,
    flow_rate,
    load_percentage,
    frequency,
    power_factor,
    cycle_time,
    operating_hours,
    maintenance_count
):

    machine = pd.DataFrame([{
        "machine_id": machine_id,
        "production_line": production_line,
        "machine_type": machine_type,
        "temperature": temperature,
        "vibration": vibration,
        "rpm": rpm,
        "current": current,
        "voltage": voltage,
        "torque": torque,
        "pressure": pressure,
        "flow_rate": flow_rate,
        "load_percentage": load_percentage,
        "frequency": frequency,
        "power_factor": power_factor,
        "cycle_time": cycle_time,
        "operating_hours": operating_hours,
        "maintenance_count": maintenance_count
    }])



    failure_input = pd.get_dummies(
        machine,
        columns=[
            "machine_id",
            "production_line",
            "machine_type"
        ]
    )

    failure_input = failure_input.reindex(
        columns=failure_features,
        fill_value=0
    )

    failure_input = failure_input.fillna(
        failure_input.median(numeric_only=True)
    )


    failure_prediction = failure_model.predict(
        failure_input
    )[0]


    failure_probability = (
        failure_model.predict_proba(failure_input)[0][1] * 100
    )


    failure_status = (
        "YES"
        if failure_prediction == 1
        else "NO"
    )


    failure_type_prediction = None
    failure_type_probabilities = {}


    if failure_status == "YES":

        failure_type_input = machine.drop(
            columns=["machine_id"]
        )


        failure_type_input = pd.get_dummies(
            failure_type_input,
            columns=[
                "production_line",
                "machine_type"
            ]
        )


        failure_type_input = failure_type_input.reindex(
            columns=failure_type_features,
            fill_value=0
        )


        failure_type_input = failure_type_input.fillna(
            failure_type_input.median(numeric_only=True)
        )


        failure_type_prediction = failure_type_model.predict(
            failure_type_input
        )[0]


        probabilities = failure_type_model.predict_proba(
            failure_type_input
        )[0]


        for failure_type, probability in zip(
            failure_type_model.classes_,
            probabilities
        ):

            failure_type_probabilities[failure_type] = round(
                probability * 100,
                2
            )


   
    health_input = machine[health_features].copy()


    health_input = health_input.fillna(
        health_input.median(numeric_only=True)
    )


    health_score = health_model.predict(
        health_input
    )[0]


    health_score = max(
        0,
        min(100, health_score)
    )


    health_status = get_health_status(
        health_score
    )


    maintenance = maintenance_schedule(
        failure_status,
        failure_probability,
        health_score
    )


 
    return {
        "machine_id": machine_id,
        "failure": failure_status,
        "failure_probability": round(
            failure_probability,
            2
        ),
        "failure_type": failure_type_prediction,
        "failure_type_probabilities": failure_type_probabilities,
        "health_score": round(
            health_score,
            2
        ),
        "health_status": health_status,
        "maintenance": maintenance
    }



result = predict_machine(
    "AIRCOMP_U_001",
    "Utilities",
    "Compressor",
    69.64,
    4.30,
    1500,
    12.5,
    220,
    45,
    5.2,
    10.5,
    75.86,
    50,
    0.92,
    12.5,
    4501,
    3
)

print(result)
