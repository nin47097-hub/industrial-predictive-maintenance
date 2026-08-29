import "./factory_dashboard.css";
import { useEffect, useState } from "react";
import axios from "axios";

function FactoryDashboard() {

    const [categoryFilter, setCategoryFilter] = useState("All");
    const [statusFilter, setStatusFilter] = useState("All");

    const [machines, setMachines] = useState([]);
    const [selectedMachine, setSelectedMachine] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [predictionLoading,setPredictionLoading]= useState(false)


    // ==========================================
    // GET MACHINES + RUN ML PREDICTION
    // ==========================================

    useEffect(() => {

        const getMachines = async () => {

            try {

                const response = await axios.get(
                    "https://industrial-predictive-maintenance-ml.onrender.com/machines"
                );

                console.log(
                    "Machines:",
                    response.data
                );

                if (!Array.isArray(response.data)) {

                    console.error(
                        "Machines response is not an array"
                    );

                    return;
                }

                // Run prediction for every machine
                const predictedMachines =
                    await Promise.all(

                        response.data.map(
                            async (machine) => {

                                try {

                                    const predictionResponse  = await axios.post(
                                        "https://industrial-predictive-maintenance-ml.onrender.com/predict",
                                            {
                                                machine_id:
                                                    machine.machine_id,

                                                production_line:
                                                    machine.production_line,

                                                machine_type:
                                                    machine.machine_type,

                                                temperature:
                                                    machine.temperature,

                                                vibration:
                                                    machine.vibration,

                                                rpm:
                                                    machine.rpm,

                                                current:
                                                    machine.current,

                                                voltage:
                                                    machine.voltage,

                                                torque:
                                                    machine.torque,

                                                pressure:
                                                    machine.pressure,

                                                flow_rate:
                                                    machine.flow_rate,

                                                load_percentage:
                                                    machine.load_percentage,

                                                frequency:
                                                    machine.frequency,

                                                power_factor:
                                                    machine.power_factor,

                                                cycle_time:
                                                    machine.cycle_time,

                                                operating_hours:
                                                    machine.operating_hours,

                                                maintenance_count:
                                                    machine.maintenance_count
                                            }
                                        );


                                    console.log(
                                        "Prediction:",
                                        machine.machine_id,
                                        predictionResponse.data
                                    );

                                    const prediction = predictionResponse.data;
                                    let dashboardStatus = prediction.health_status;
                                    if (dashboardStatus ==="Degraded"){
                                        dashboardStatus="At Risk"
                                    }
                                    return {

                                        ...machine,

                                        ...prediction,
                                        health_status: dashboardStatus

                                    };
                                } catch (error) {
                                    console.error(
                                        "Prediction failed for",
                                        machine.machine_id,
                                        error
                                    );

                                    // Keep machine even if
                                    // prediction fails
                                    return machine;

                                }

                            }
                        )
                    );


                console.log(
                    "Final machines:",
                    predictedMachines
                );
                console.log(
                    "Machine statuses:",
                    predictedMachines.map(machine => ({
                        id: machine.machine_id,
                        status: machine.health_status
                    }))
                );
               


                setMachines(
                    predictedMachines
                );


            } catch (error) {

                console.error(
                    "Failed to get machines:",
                    error
                );

            }

        };


        getMachines();

    }, []);


    // ==========================================
    // FILTER MACHINES
    // ==========================================

    const filteredMachines =
        machines.filter((machine) => {

            const categoryMatch =
                categoryFilter === "All" ||
                machine.machine_type
                    ?.toLowerCase()
                    .includes(
                        categoryFilter.toLowerCase()
                    );


            const statusMatch =
                statusFilter === "All" ||
                machine.health_status === statusFilter;


            return (
                categoryMatch &&
                statusMatch
            );

        });


    // ==========================================
    // STATUS COUNTS
    // ==========================================

    const healthyCount =
        machines.filter(
            machine =>
                machine.health_status === "Healthy"
        ).length;


    const moderateCount =
        machines.filter(
            machine =>
                machine.health_status === "Moderate"
        ).length;


    const atRiskCount =
        machines.filter(
            machine =>
                machine.health_status === "At Risk"
        ).length;


    const criticalCount =
        machines.filter(
            machine =>
                machine.health_status === "Critical"
        ).length;


    // ==========================================
    // COLORS
    // ==========================================

    const statusColor = (status) => {

        if (status === "Healthy")
            return "green";

        if (status === "Moderate")
            return "orange";

        if (status === "At Risk")
            return "maroon";

        if (status === "Critical")
            return "red";

        return "gray";

    };


    const riskColor = (risk) => {

        if (risk <= 30)
            return "green";

        if (risk <= 60)
            return "orange";

        return "red";

    };


    // ==========================================
    // SELECT MACHINE
    // ==========================================

    const handleMachineClick = async (machine) => {
        setSelectedMachine(machine);
        setPrediction(null);

        try {
            setPredictionLoading(true);

            const response = await axios.post(
                "https://industrial-predictive-maintenance-ml.onrender.com/predict",
                machine
            );

            console.log("ML Prediction:", response.data);

            setPrediction(response.data);

        } catch (error) {
            console.error("Prediction failed:", error);
        } finally {
            setPredictionLoading(false);
        }
    };


    // ==========================================
    // UI
    // ==========================================



    const predicMachine = async(machine)=>{
        try{
            setPredictionLoading(true);
            setPrediction(null);
            const response = await axios.post(
                "https://industrial-predictive-maintenance-ml.onrender.com/predict",
                machine
            )
            console.log("ML prediction",response.data);
            setPrediction(response.data);
        }  catch(error){
            console.log("prediction failed",error);

        }finally{
            setPredictionLoading(false);
        }
        


    };
    return (

        <div className="dashboard">

            <h1>
                Factory Dashboard
            </h1>

            <p className="dashboard-subtitle">
                Machine Monitoring & ML Prediction
            </p>


            {/* ================================= */}
            {/* FILTERS */}
            {/* ================================= */}

            <section className="filters-section">

                <h2>
                    Machine Category
                </h2>

                <div className="filter-buttons">

                    {[
                        "All",
                        "CNC",
                        "Hydraulic",
                        "Robotic",
                        "Compressor",
                        "Grinding",
                        "Motor",
                        "Conveyor",
                        "Pump",
                        "Power",
                        "Cooling"
                    ].map(
                        category => (

                            <button
                                key={category}
                                className={
                                    categoryFilter === category
                                        ? "filter-btn active"
                                        : "filter-btn"
                                }
                                onClick={() =>
                                    setCategoryFilter(
                                        category
                                    )
                                }
                            >
                                {category}
                            </button>

                        )
                    )}

                </div>


                <h2>
                    Machine Status
                </h2>

                <div className="filter-buttons">

                    {[
                        "All",
                        "Healthy",
                        "Moderate",
                        "At Risk",
                        "Critical"
                    ].map(
                        status => (

                            <button
                                key={status}
                                className={
                                    statusFilter === status
                                        ? "filter-btn active"
                                        : "filter-btn"
                                }
                                onClick={() =>
                                    setStatusFilter(
                                        status
                                    )
                                }
                            >
                                {status}
                            </button>

                        )
                    )}

                </div>

            </section>


            {/* ================================= */}
            {/* OVERVIEW */}
            {/* ================================= */}

            <section className="overview-section">

                <div className="overview-card">

                    <span>
                        Total Machines
                    </span>

                    <strong>
                        {machines.length}
                    </strong>

                </div>


                <div className="overview-card">

                    <span>
                        Healthy
                    </span>

                    <strong>
                        {healthyCount}
                    </strong>

                </div>


                <div className="overview-card">

                    <span>
                        Moderate
                    </span>

                    <strong>
                        {moderateCount}
                    </strong>

                </div>


                <div className="overview-card">

                    <span>
                        At Risk
                    </span>

                    <strong>
                        {atRiskCount}
                    </strong>

                </div>


                <div className="overview-card">

                    <span>
                        Critical
                    </span>

                    <strong>
                        {criticalCount}
                    </strong>

                </div>

            </section>


            {/* ================================= */}
            {/* MACHINES */}
            {/* ================================= */}

            <section className="machines-section">

                <h2>
                    Machines
                </h2>


                <div className="machine-container">

                    {machines.length === 0 ? (

                        <p>
                            Loading machines...
                        </p>

                    ) : filteredMachines.length === 0 ? (

                        <p>
                            No machines match the selected filters.
                        </p>

                    ) : (

                        filteredMachines.map(
                            machine => (

                                <div
                                    className="machine-card"
                                    key={
                                        machine.machine_id
                                    }
                                    onClick={() =>
                                        handleMachineClick(
                                            machine
                                        )
                                    }
                                >

                                    {/* HEADER */}

                                    <div className="machine-header">

                                        <h3>
                                            {
                                                machine.machine_id
                                            }
                                        </h3>


                                        <span
                                            className="status-badge"
                                            style={{
                                                backgroundColor:
                                                    statusColor(
                                                        machine.health_status
                                                    )
                                            }}
                                        >
                                            {
                                                machine.health_status
                                                    || "Analyzing"
                                            }
                                        </span>

                                    </div>


                                    <p className="machine-type">

                                        {
                                            machine.machine_type
                                        }

                                    </p>


                                    <p className="machine-line">

                                        {
                                            machine.production_line
                                        }

                                    </p>


                                    {/* HEALTH */}

                                    <div className="health-section">

                                        <div className="health-info">

                                            <span>
                                                Health
                                            </span>

                                            <strong>

                                                {
                                                    machine.health_score !== undefined
                                                        ? `${machine.health_score}%`
                                                        : "--"
                                                }

                                            </strong>

                                        </div>


                                        <div className="health-bar">

                                            <div
                                                className="health-fill"
                                                style={{
                                                    width:
                                                        machine.health_score !== undefined
                                                            ? `${machine.health_score}%`
                                                            : "0%",

                                                    backgroundColor:
                                                        statusColor(
                                                            machine.health_status
                                                        )
                                                }}
                                            />

                                        </div>

                                    </div>


                                    {/* FAILURE RISK */}

                                    <div className="risk-info">

                                        <span>
                                            Failure Risk
                                        </span>

                                        <strong>

                                            {
                                                machine.failure_probability !== undefined
                                                    ? `${machine.failure_probability}%`
                                                    : "--"
                                            }

                                        </strong>

                                    </div>


                                    <div className="risk-bar">

                                        <div
                                            className="risk-fill"
                                            style={{
                                                width:
                                                    machine.failure_probability !== undefined
                                                        ? `${machine.failure_probability}%`
                                                        : "0%",

                                                backgroundColor:
                                                    riskColor(
                                                        machine.failure_probability || 0
                                                    )
                                            }}
                                        />

                                    </div>


                                    {/* SENSOR DATA */}

                                    <div className="sensor-data">

                                        <p>
                                            <span>
                                                Temperature
                                            </span>

                                            <strong>
                                                {
                                                    machine.temperature ?? "--"
                                                } °C
                                            </strong>
                                        </p>


                                        <p>
                                            <span>
                                                Vibration
                                            </span>

                                            <strong>
                                                {
                                                    machine.vibration ?? "--"
                                                }
                                            </strong>
                                        </p>


                                        <p>
                                            <span>
                                                RPM
                                            </span>

                                            <strong>
                                                {
                                                    machine.rpm ?? "--"
                                                }
                                            </strong>
                                        </p>


                                        <p>
                                            <span>
                                                Current
                                            </span>

                                            <strong>
                                                {
                                                    machine.current ?? "--"
                                                } A
                                            </strong>
                                        </p>


                                        <p>
                                            <span>
                                                Load
                                            </span>

                                            <strong>
                                                {
                                                    machine.load_percentage ?? "--"
                                                } %
                                            </strong>
                                        </p>

                                    </div>

                                </div>

                            )
                        )

                    )}

                </div>

            </section>


            {/* ================================= */}
            {/* SELECTED MACHINE */}
            {/* ================================= */}

            {selectedMachine && (

                <section className="machine-details">

                    <h2>
                        Machine Details
                    </h2>


                    <div className="details-card">
                        <div className="selected-sensors">
                            <h4>sensor readings</h4>
                            <p>
                                temperature:
                                <strong>{selectedMachine.temperature ??"_ _"}</strong>

                            </p>
                            <p>
                                Vibrations:
                                <strong>{selectedMachine.vibration ??"_ _"}</strong>
                            </p>
                            <p>
                                RPM:
                                <strong>{selectedMachine.rpm ?? "--"}</strong>
                            </p>
                            <p>
                                Current:
                                <strong>{selectedMachine.current ?? "--"} A</strong>

                            </p>
                            <p>
                                Voltage:
                                <strong>{selectedMachine.voltage ?? "--"} V</strong>
                            </p>
                            <p>
                                Load:
                                <strong>{selectedMachine.load_percentage ?? "--"}%</strong>
                            </p>




                        </div>

                        <div className="machine-header">

                            <h3>
                                {
                                    selectedMachine.machine_id
                                }
                            </h3>


                            <span
                                className="status-badge"
                                style={{
                                    backgroundColor:
                                        statusColor(
                                            selectedMachine.health_status
                                        )
                                }}
                            >
                                {
                                    selectedMachine.health_status
                                        || "Analyzing"
                                }
                            </span>

                        </div>


                        <p>
                            {
                                selectedMachine.machine_type
                            }
                        </p>


                        <p>
                            {
                                selectedMachine.production_line
                            }
                        </p>

                        {predictionLoading &&(
                            <p>Analysing Machine</p>
                        )}
                        {prediction &&(
                            <div className="prediction-results">
                                <div className="prediction-metric">
                                    <div className="metric-header">
                                        <span>Heallth Score</span>
                                        <strong>{prediction.health_score}%</strong>
                                    </div>

                                    <div className="metric-bar">
                                        <div
                                        className="metric-fill health-fill"
                                        style={{
                                            width: `${prediction.health_score}%`

                                        }}>
                                           
                                        </div>

                                    </div>

                                </div>
                                <div className="prediction-metric">
                                    <div className="metric-header">
                                        <span>Failure Risk</span>
                                        <strong>{prediction.failure_probability}%</strong>
                                    </div>

                                    <div className="metric-bar">
                                        <div
                                            className="metric-fill risk-fill"
                                            style={{
                                                width: `${prediction.failure_probability}%`
                                            }}

                                        ></div>
                                    </div>
                                </div>

                                <p>
                                    Failure Type: {prediction.failure_type || "None"}
                                </p>

                                <p>
                                    Health Status: {prediction.health_status}
                                </p>

                                <div className="maintenance-recommendation">
                                    <span>Maintenance Recommendation</span>
                                    <strong>
                                        {prediction.maintenance || "No recommendation"}
                                    </strong>


                                </div>
                            </div>

                        )}


                        <hr />


                        <div className="details-row">

                            <span>
                                Health Score
                            </span>

                            <strong>
                                {
                                    selectedMachine.health_score ?? "--"
                                }%
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Failure Probability
                            </span>

                            <strong>
                                {
                                    selectedMachine.failure_probability ?? "--"
                                }%
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Failure Type
                            </span>

                            <strong>
                                {
                                    selectedMachine.failure_type
                                        || "No failure detected"
                                }
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Maintenance
                            </span>

                            <strong>
                                {
                                    selectedMachine.maintenance
                                        || "--"
                                }
                            </strong>

                        </div>


                        <hr />


                        <h3>
                            Sensor Data
                        </h3>


                        <div className="details-row">

                            <span>
                                Temperature
                            </span>

                            <strong>
                                {
                                    selectedMachine.temperature ?? "--"
                                } °C
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Vibration
                            </span>

                            <strong>
                                {
                                    selectedMachine.vibration ?? "--"
                                }
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                RPM
                            </span>

                            <strong>
                                {
                                    selectedMachine.rpm ?? "--"
                                }
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Current
                            </span>

                            <strong>
                                {
                                    selectedMachine.current ?? "--"
                                } A
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Voltage
                            </span>

                            <strong>
                                {
                                    selectedMachine.voltage ?? "--"
                                } V
                            </strong>

                        </div>


                        <div className="details-row">

                            <span>
                                Load
                            </span>

                            <strong>
                                {
                                    selectedMachine.load_percentage ?? "--"
                                } %
                            </strong>

                        </div>


                        <button
                            className="close-details"
                            onClick={() => {
                                setSelectedMachine(null);
                                setPrediction(null);
                            }}
                        >
                            Close
                        </button>

                    </div>

                </section>

            )}


            {/* ================================= */}
            {/* MAINTENANCE ALERTS */}
            {/* ================================= */}

            <section className="maintenance-alerts">

                <h2>
                    Maintenance Alerts
                </h2>


                <div className="alerts-container">

                    {machines
                        .filter(
                            machine =>
                                machine.health_status ===
                                    "Critical" ||
                                machine.health_status ===
                                    "At Risk"
                        )
                        .map(
                            machine => (

                                <div
                                    className="alert-card"
                                    key={
                                        machine.machine_id
                                    }
                                >

                                    <h3>
                                        {
                                            machine.machine_id
                                        }
                                    </h3>


                                    <p>
                                        Status:{" "}
                                        {
                                            machine.health_status
                                        }
                                    </p>


                                    <p>
                                        Failure Risk:{" "}
                                        {
                                            machine.failure_probability ?? "--"
                                        }%
                                    </p>


                                    <p>
                                        Failure Type:{" "}
                                        {
                                            machine.failure_type
                                                || "Unknown"
                                        }
                                    </p>


                                    <p>
                                        Maintenance:{" "}
                                        {
                                            machine.maintenance
                                                || "Review required"
                                        }
                                    </p>

                                </div>

                            )
                        )}

                </div>


                {machines.filter(
                    machine =>
                        machine.health_status ===
                            "Critical" ||
                        machine.health_status ===
                            "At Risk"
                ).length === 0 && (

                    <p>
                        No maintenance alerts.
                    </p>

                )}

            </section>

        </div>

    );

}

export default FactoryDashboard;