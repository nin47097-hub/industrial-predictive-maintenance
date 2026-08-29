const axios = require("axios");
const flask_url = "https://industrial-predictive-maintenance-ml.onrender.com/predict";
const flask_machine_url = "https://industrial-predictive-maintenance-ml.onrender.com/machines";
exports.getMachines = async (req, res) => {

    try {

        const response = await axios.get(
            flask_machine_url
        );

        return res.status(200).json(response.data);

    } catch (error) {

        return res.status(500).json({
            message: "Failed to get machines",
            error: error.message
        });

    }

};
exports.predictions = async (req, res) => {
    try {

        const {
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
        } = req.body;

        if (
            !machine_id ||
            !production_line ||
            !machine_type ||
            temperature === undefined ||
            vibration === undefined ||
            rpm === undefined ||
            current === undefined ||
            voltage === undefined ||
            torque === undefined ||
            pressure === undefined ||
            flow_rate === undefined ||
            load_percentage === undefined ||
            frequency === undefined ||
            power_factor === undefined ||
            cycle_time === undefined ||
            operating_hours === undefined ||
            maintenance_count === undefined
        ) {
            return res.status(400).json({
                message: "All machine data is required"
            });
        }

        const dataresponse = await axios.post(
            flask_url,
            {
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
            }
        );

        return res.status(200).json({
            message: "Displaying outputs",
            data: dataresponse.data
        });

    } catch (error) {

        return res.status(500).json({
            message: "Prediction failed",
            error: error.message
        });

    }
};
    
exports.getMachine = async (req, res) => {

    try {

        const machine_id = req.params.machine_id;

        const response = await axios.get(
            `${flask_machine_url}/${machine_id}`
        );

        return res.status(200).json(response.data);

    } catch (error) {

        return res.status(500).json({
            message: "Failed to get machine data",
            error: error.message
        });

    }

};


    
   


