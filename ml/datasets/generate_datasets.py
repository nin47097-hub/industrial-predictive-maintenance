import pandas as pd
import numpy as np
import os

np.random.seed(42)

OUTPUT_DIR = "ml/dataset"
os.makedirs(OUTPUT_DIR, exist_ok=True)

N = 10000

machines = [
    ("CNC_L1_001", "Metal Processing", "CNC Machine"),
    ("CNC_L1_002", "Metal Processing", "CNC Machine"),

    ("PRESS_L1_001", "Metal Processing", "Hydraulic Press"),
    ("PRESS_L1_002", "Metal Processing", "Hydraulic Press"),

    ("CONVEYOR_L1_001", "Metal Processing", "Conveyor System"),

    ("ROBOT_L2_001", "Component Assembly", "Robotic Arm"),
    ("ROBOT_L2_002", "Component Assembly", "Robotic Arm"),

    ("CONVEYOR_L2_001", "Component Assembly", "Conveyor System"),

    ("MOTOR_L2_001", "Component Assembly", "Industrial Motor"),
    ("MOTOR_L2_002", "Component Assembly", "Industrial Motor"),

    ("GRIND_L3_001", "Finishing", "Grinding Machine"),

    ("COMP_L3_001", "Finishing", "Compressor"),

    ("COOL_L3_001", "Finishing", "Cooling System"),

    ("AIRCOMP_U_001", "Utilities", "Air Compressor"),

    ("PUMP_U_001", "Utilities", "Water Pump"),

    ("POWER_U_001", "Utilities", "Power System")
]


def generate_data(machine_id, production_line, machine_type):

    timestamp = pd.date_range(
        start="2026-01-01 00:00:00",
        periods=N,
        freq="2h"
    )

    # ------------------------------------------------
    # Common values
    # ------------------------------------------------

    operating_hours = np.cumsum(
        np.random.uniform(0.5, 1.5, N)
    ) + 4500

    maintenance_count = np.random.poisson(
        3, N
    )

    # ------------------------------------------------
    # Default NaN values
    # ------------------------------------------------

    temperature = np.full(N, np.nan)
    vibration = np.full(N, np.nan)
    rpm = np.full(N, np.nan)
    current = np.full(N, np.nan)
    voltage = np.full(N, np.nan)
    torque = np.full(N, np.nan)
    pressure = np.full(N, np.nan)
    flow_rate = np.full(N, np.nan)
    load_percentage = np.full(N, np.nan)
    frequency = np.full(N, np.nan)
    power_factor = np.full(N, np.nan)
    cycle_time = np.full(N, np.nan)

    # ------------------------------------------------
    # CNC MACHINE
    # ------------------------------------------------

    if machine_type == "CNC Machine":

        temperature = np.random.normal(72, 8, N)

        vibration = np.random.normal(3.1, 1.0, N)

        rpm = np.random.normal(3200, 250, N)

        current = np.random.normal(8.4, 1.2, N)

        voltage = np.random.normal(415, 5, N)

        torque = np.random.normal(42.5, 5, N)

        load_percentage = np.random.normal(
            74, 10, N
        )

        cycle_time = np.random.normal(
            45, 5, N
        )

    # ------------------------------------------------
    # HYDRAULIC PRESS
    # ------------------------------------------------

    elif machine_type == "Hydraulic Press":

        temperature = np.random.normal(78, 9, N)

        vibration = np.random.normal(4.2, 1.2, N)

        current = np.random.normal(11, 1.5, N)

        voltage = np.random.normal(415, 5, N)

        pressure = np.random.normal(150, 20, N)

        load_percentage = np.random.normal(
            82, 8, N
        )

        cycle_time = np.random.normal(
            60, 7, N
        )

    # ------------------------------------------------
    # CONVEYOR
    # ------------------------------------------------

    elif machine_type == "Conveyor System":

        temperature = np.random.normal(58, 7, N)

        vibration = np.random.normal(2.5, 0.8, N)

        rpm = np.random.normal(1450, 100, N)

        current = np.random.normal(6, 1, N)

        voltage = np.random.normal(415, 5, N)

        load_percentage = np.random.normal(
            65, 12, N
        )

        cycle_time = np.random.normal(
            30, 4, N
        )

    # ------------------------------------------------
    # ROBOTIC ARM
    # ------------------------------------------------

    elif machine_type == "Robotic Arm":

        temperature = np.random.normal(55, 7, N)

        vibration = np.random.normal(2.2, 0.7, N)

        current = np.random.normal(5.5, 1, N)

        voltage = np.random.normal(415, 5, N)

        load_percentage = np.random.normal(
            68, 12, N
        )

        cycle_time = np.random.normal(
            12, 2, N
        )

    # ------------------------------------------------
    # INDUSTRIAL MOTOR
    # ------------------------------------------------

    elif machine_type == "Industrial Motor":

        temperature = np.random.normal(65, 8, N)

        vibration = np.random.normal(3.0, 1, N)

        rpm = np.random.normal(2900, 150, N)

        current = np.random.normal(7.5, 1.2, N)

        voltage = np.random.normal(415, 5, N)

        torque = np.random.normal(35, 5, N)

        load_percentage = np.random.normal(
            70, 12, N
        )

    # ------------------------------------------------
    # GRINDING MACHINE
    # ------------------------------------------------

    elif machine_type == "Grinding Machine":

        temperature = np.random.normal(75, 9, N)

        vibration = np.random.normal(4.5, 1.3, N)

        rpm = np.random.normal(3500, 250, N)

        current = np.random.normal(9, 1.5, N)

        voltage = np.random.normal(415, 5, N)

        load_percentage = np.random.normal(
            78, 10, N
        )

    # ------------------------------------------------
    # COMPRESSOR
    # ------------------------------------------------

    elif machine_type == "Compressor":

        temperature = np.random.normal(70, 8, N)

        vibration = np.random.normal(3.5, 1, N)

        rpm = np.random.normal(1750, 100, N)

        current = np.random.normal(8, 1.2, N)

        pressure = np.random.normal(
            7, 1, N
        )

        load_percentage = np.random.normal(
            75, 10, N
        )

    # ------------------------------------------------
    # COOLING SYSTEM
    # ------------------------------------------------

    elif machine_type == "Cooling System":

        temperature = np.random.normal(45, 6, N)

        vibration = np.random.normal(1.8, 0.5, N)

        current = np.random.normal(5, 0.8, N)

        voltage = np.random.normal(415, 5, N)

        pressure = np.random.normal(
            3.5, 0.5, N
        )

        flow_rate = np.random.normal(
            80, 10, N
        )

    # ------------------------------------------------
    # AIR COMPRESSOR
    # ------------------------------------------------

    elif machine_type == "Air Compressor":

        temperature = np.random.normal(75, 9, N)

        vibration = np.random.normal(3.8, 1.1, N)

        rpm = np.random.normal(1800, 120, N)

        current = np.random.normal(9, 1.3, N)

        pressure = np.random.normal(
            8, 1, N
        )

        load_percentage = np.random.normal(
            80, 10, N
        )

    # ------------------------------------------------
    # WATER PUMP
    # ------------------------------------------------

    elif machine_type == "Water Pump":

        temperature = np.random.normal(60, 7, N)

        vibration = np.random.normal(2.8, 0.8, N)

        current = np.random.normal(6, 1, N)

        voltage = np.random.normal(415, 5, N)

        pressure = np.random.normal(
            4, 0.7, N
        )

        flow_rate = np.random.normal(
            50, 8, N
        )

    # ------------------------------------------------
    # POWER SYSTEM
    # ------------------------------------------------

    elif machine_type == "Power System":

        temperature = np.random.normal(50, 6, N)

        vibration = np.random.normal(1.2, 0.4, N)

        current = np.random.normal(35, 5, N)

        voltage = np.random.normal(
            415, 8, N
        )

        frequency = np.random.normal(
            50, 0.2, N
        )

        power_factor = np.random.normal(
            0.95, 0.02, N
        )

    # ------------------------------------------------
    # LIMIT VALUES TO REALISTIC RANGES
    # ------------------------------------------------

    temperature = np.clip(
        temperature, 20, 120
    )

    vibration = np.clip(
        vibration, 0.1, 15
    )

    rpm = np.where(
        np.isnan(rpm),
        np.nan,
        np.clip(rpm, 500, 5000)
    )

    current = np.clip(
        current, 0.5, 30
    )

    voltage = np.where(
        np.isnan(voltage),
        np.nan,
        np.clip(voltage, 300, 450)
    )

    torque = np.where(
        np.isnan(torque),
        np.nan,
        np.clip(torque, 5, 100)
    )

    pressure = np.where(
        np.isnan(pressure),
        np.nan,
        np.clip(pressure, 0.5, 250)
    )

    flow_rate = np.where(
        np.isnan(flow_rate),
        np.nan,
        np.clip(flow_rate, 5, 150)
    )

    load_percentage = np.where(
        np.isnan(load_percentage),
        np.nan,
        np.clip(load_percentage, 10, 100)
    )

    frequency = np.where(
        np.isnan(frequency),
        np.nan,
        np.clip(frequency, 45, 55)
    )

    power_factor = np.where(
        np.isnan(power_factor),
        np.nan,
        np.clip(power_factor, 0.7, 1)
    )

    # ------------------------------------------------
    # FAILURE GENERATION
    # ------------------------------------------------
    # Failure becomes more likely when:
    # temperature, vibration, load and operating hours
    # become high.

    risk = np.zeros(N)

    risk += np.maximum(
        temperature - 80, 0
    ) * 0.025

    risk += np.maximum(
        vibration - 5, 0
    ) * 0.08

    risk += np.maximum(
        np.nan_to_num(load_percentage) - 85, 0
    ) * 0.015

    risk += np.maximum(
        operating_hours - 8000, 0
    ) / 10000

    risk += maintenance_count * 0.01

    # Convert risk to probability
    probability = np.clip(
        risk, 0, 0.8
    )

    failure = (
        np.random.random(N) < probability
    ).astype(int)

    # ------------------------------------------------
    # FAILURE TYPE
    # ------------------------------------------------

    failure_type = np.full(
        N,
        "None",
        dtype=object
    )

    for i in range(N):

        if failure[i] == 1:

            if temperature[i] > 90:

                failure_type[i] = "Overheating"

            elif vibration[i] > 7:

                failure_type[i] = "Bearing Failure"

            elif (
                not np.isnan(pressure[i])
                and pressure[i] > 180
            ):

                failure_type[i] = "Pressure Failure"

            elif (
                not np.isnan(current[i])
                and current[i] > 15
            ):

                failure_type[i] = "Electrical Failure"

            else:

                failure_type[i] = "Mechanical Failure"

    # ------------------------------------------------
    # CREATE DATAFRAME
    # ------------------------------------------------

    df = pd.DataFrame({

        "machine_id": machine_id,

        "production_line": production_line,

        "machine_type": machine_type,

        "timestamp": timestamp,

        "temperature": np.round(
            temperature, 2
        ),

        "vibration": np.round(
            vibration, 2
        ),

        "rpm": np.round(
            rpm, 2
        ),

        "current": np.round(
            current, 2
        ),

        "voltage": np.round(
            voltage, 2
        ),

        "torque": np.round(
            torque, 2
        ),

        "pressure": np.round(
            pressure, 2
        ),

        "flow_rate": np.round(
            flow_rate, 2
        ),

        "load_percentage": np.round(
            load_percentage, 2
        ),

        "frequency": np.round(
            frequency, 2
        ),

        "power_factor": np.round(
            power_factor, 3
        ),

        "cycle_time": np.round(
            cycle_time, 2
        ),

        "operating_hours": np.round(
            operating_hours, 1
        ),

        "maintenance_count":
            maintenance_count,

        "failure":
            failure,

        "failure_type":
            failure_type
    })

    return df


# ====================================================
# GENERATE ALL 16 FILES
# ====================================================

for machine_id, production_line, machine_type in machines:

    df = generate_data(
        machine_id,
        production_line,
        machine_type
    )

    file_path = os.path.join(
        OUTPUT_DIR,
        f"{machine_id}.csv"
    )

    df.to_csv(
        file_path,
        index=False
    )

    print(
        f"Created {file_path} -> "
        f"{len(df)} entries"
    )


print("\n===================================")
print("DATASET GENERATION COMPLETE")
print("===================================")
print(f"Files created: {len(machines)}")
print(f"Rows per file: {N}")
print(f"Total rows: {len(machines) * N}")