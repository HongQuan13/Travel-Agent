import { useContext } from "react";

import { AuthContext, AuthContextType } from "@/context/AuthProvider";

export const useAuthContext = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuthContext must be used within a AuthProvider");
  }
  return context;
};
