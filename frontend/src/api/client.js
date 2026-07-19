import axios from "axios";


const DEFAULT_API_BASE_URL = "https://tengxun-production.up.railway.app/api";

const apiClient = axios.create({
  baseURL: DEFAULT_API_BASE_URL,
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
