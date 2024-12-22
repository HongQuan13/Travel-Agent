import { fetchData, postData } from "@/services/api";

export const logout = async () => {
  return await postData("auth/logout");
};

export const authVerify = async () => {
  return await fetchData("auth/verify");
};
