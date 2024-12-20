import React, { createContext, useContext, useEffect, useState } from "react";

import { axiosClient } from "@/lib/axios";

interface AuthContextType {
  isAuthenticated: boolean;
  user: any;
}

interface AuthProviderProps {
  children: React.ReactNode;
}

const AuthContext = createContext<AuthContextType | null>(null);

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
    <AuthContext.Provider value={{ isAuthenticated, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuthContext must be used within a AuthProvider");
  }
  return context;
};
