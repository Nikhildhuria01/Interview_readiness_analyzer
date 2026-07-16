import axios from "axios";

const api = axios.create({
    baseURL: "https://interview-readiness-analyzer.up.railway.app",
});

export default api;