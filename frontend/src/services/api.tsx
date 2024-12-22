import { axiosClient } from "@/lib/axios";

export const fetchData = async (endpoint: string) => {
  try {
    const response = await axiosClient.get(endpoint);
    return response.data;
  } catch (error) {
    console.log(`fetchData error ${endpoint}:`, error);
  }
};

export const postData = async (endpoint: string, data?: object) => {
  try {
    const response = await axiosClient.post(endpoint, data);
    return response.data;
  } catch (error) {
    console.log(`postData error ${endpoint}:`, error);
  }
};
