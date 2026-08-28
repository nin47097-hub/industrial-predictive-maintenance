import { predictmachine } from "../services/predictionApi";
import { useState } from "react";

function PredictionForm() {

    const [machinedata, set_machinedata] = useState({
        machine_id: "",
        production_line: "",
        machine_type: "",
        temperature: "",
        vibration: "",
        rpm: "",
        current: "",
        voltage: "",
        torque: "",
        pressure: "",
        flow_rate: "",
        load_percentage: "",
        frequency: "",
        power_factor: "",
        cycle_time: "",
        operating_hours: "",
        maintenance_count: ""
    });

    const [prediction, set_prediction] = useState(null);

    const handle_change = (event) => {
        const { name, value } = event.target;

        set_machinedata({
            ...machinedata,
            [name]: value
        });
    };

    const handle_submit = async (event) => {
        event.preventDefault();

        const result = await predictmachine(machinedata);

        set_prediction(result);
    };

    return (
        <div>

            <h1>Machine Prediction</h1>

            <form onSubmit={handle_submit}>

                <label>Machine ID</label>
                <input
                    type="text"
                    name="machine_id"
                    value={machinedata.machine_id}
                    onChange={handle_change}
                />

                <label>Production Line</label>
                <input
                    type="text"
                    name="production_line"
                    value={machinedata.production_line}
                    onChange={handle_change}
                />

                <label>Machine Type</label>
                <input
                    type="text"
                    name="machine_type"
                    value={machinedata.machine_type}
                    onChange={handle_change}
                />

                <label>Temperature</label>
                <input
                    type="text"
                    name="temperature"
                    value={machinedata.temperature}
                    onChange={handle_change}
                />

                <label>Vibration</label>
                <input
                    type="text"
                    name="vibration"
                    value={machinedata.vibration}
                    onChange={handle_change}
                />

                <label>RPM</label>
                <input
                    type="text"
                    name="rpm"
                    value={machinedata.rpm}
                    onChange={handle_change}
                />

                <label>Current</label>
                <input
                    type="text"
                    name="current"
                    value={machinedata.current}
                    onChange={handle_change}
                />

                <label>Voltage</label>
                <input
                    type="text"
                    name="voltage"
                    value={machinedata.voltage}
                    onChange={handle_change}
                />

                <label>Torque</label>
                <input
                    type="text"
                    name="torque"
                    value={machinedata.torque}
                    onChange={handle_change}
                />

                <label>Pressure</label>
                <input
                    type="text"
                    name="pressure"
                    value={machinedata.pressure}
                    onChange={handle_change}
                />

                <label>Flow Rate</label>
                <input
                    type="text"
                    name="flow_rate"
                    value={machinedata.flow_rate}
                    onChange={handle_change}
                />

                <label>Load Percentage</label>
                <input
                    type="text"
                    name="load_percentage"
                    value={machinedata.load_percentage}
                    onChange={handle_change}
                />

                <label>Frequency</label>
                <input
                    type="text"
                    name="frequency"
                    value={machinedata.frequency}
                    onChange={handle_change}
                />

                <label>Power Factor</label>
                <input
                    type="text"
                    name="power_factor"
                    value={machinedata.power_factor}
                    onChange={handle_change}
                />

                <label>Cycle Time</label>
                <input
                    type="text"
                    name="cycle_time"
                    value={machinedata.cycle_time}
                    onChange={handle_change}
                />

                <label>Operating Hours</label>
                <input
                    type="text"
                    name="operating_hours"
                    value={machinedata.operating_hours}
                    onChange={handle_change}
                />

                <label>Maintenance Count</label>
                <input
                    type="text"
                    name="maintenance_count"
                    value={machinedata.maintenance_count}
                    onChange={handle_change}
                />

                <button type="submit">
                    Predict
                </button>

            </form>

            {prediction && (
                <div>
                    <h2>Prediction Results</h2>

                    <p>
                        Failure: {prediction.failure}
                    </p>

                    <p>
                        Failure Probability: {prediction.failure_probability}%
                    </p>
                </div>
            )}

        </div>
    );
}

export default PredictionForm;