import axios from "axios";

const api = axios.create({
    baseURL: "https://industrial-predictive-maintenance-1-jvmj.onrender.com/api"
});

export const getMachines = async () => {
    try {
        const response = await api.get("/machines");
        return response.data;
    } catch (error) {
        console.error("machines_api_error", error);
        throw error;
    }
};

export const getMachine = async (machineId) => {
    try {
        const response = await api.get(`/machines/${machineId}`);
        return response.data;
    } catch (error) {
        console.error("machine_api_error", error);
        throw error;
    }
};

export const predictmachine = async (machineData) => {
    try {
        const response = await api.post("/predict", machineData);
        return response.data;
    } catch (error) {
        console.error("prediction_api_error", error);
        throw error;
    }
};