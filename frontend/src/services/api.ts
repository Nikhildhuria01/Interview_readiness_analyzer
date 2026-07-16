import axios from "axios";

const api = axios.create({
    baseURL: "https://lucid-analysis-production-f238.up.railway.app",
});

export default api;