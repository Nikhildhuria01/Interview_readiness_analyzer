import axios from "axios";

const api = axios.create({
    baseURL: "https://lucid-analysis-production-d0ef.up.railway.app",
});

export default api;