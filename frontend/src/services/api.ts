import axios from "axios";

const api = axios.create({
    baseURL: "https://interview-readiness-analyzer-1.onrender.com",
});

export default api;