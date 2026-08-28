import axios from "axios"

const api_url = 'http://localhost:3000/api/predict';
export const predictmachine = async(machineData)=>{
    try{
        const response = await axios.post(api_url,machineData);
        return response.data;

    }catch (error){

        console.error('api_error',error);
        throw error;
    }
};

