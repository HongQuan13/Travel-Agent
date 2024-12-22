import React, { createContext, useEffect, useState } from "react";

import { axiosClient } from "@/lib/axios";

export interface AuthContextType {
  isAuthenticated: boolean;
  user: any;
  setIsAuthenticated: React.Dispatch<React.SetStateAction<boolean>>;
}

interface AuthProviderProps {
  children: React.ReactNode;
}

export const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<any>(null);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

  useEffect(() => {
    checkAuthenticated();
  }, [isAuthenticated]);

  const checkAuthenticated = async () => {
    try {
      const response = await axiosClient.get("auth/verify");
      if (response.status === 200) {
        setIsAuthenticated(true);
        setUser(response.data);
      }
    } catch (error) {
      console.error("User is not authenticated", error);
      setIsAuthenticated(false);
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, setIsAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
};
