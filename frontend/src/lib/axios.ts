import axios from "axios";

import {
  transformBackendDataToFrontend,
  transformFrontendDataToBackend,
} from "@/utils/variableConversion";

const axiosClient = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_BASE_URL,
  withCredentials: true,
});

axiosClient.interceptors.request.use((config) => {
  if (config.data) {
    config.data = transformFrontendDataToBackend(config.data);
  }
  return config;
});

axiosClient.interceptors.response.use((response) => {
  if (response.data) {
    response.data = transformBackendDataToFrontend(response.data);
  }
  return response;
});

axiosClient.defaults.headers.common["Content-Type"] = "application/json";
axiosClient.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

export default axiosClient;
