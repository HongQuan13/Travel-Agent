import { useNavigate } from "react-router-dom";
import React, { createContext, useContext, useEffect, useState } from "react";

import { authVerify } from "../services";
import { AuthContextType, AuthProviderProps } from "../interfaces";

export const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const navigate = useNavigate();
  const [user, setUser] = useState<any>(null);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

  useEffect(() => {
    checkAuthenticated();
  }, [isAuthenticated]);

  const checkAuthenticated = async () => {
    try {
      const response = await authVerify();
      setIsAuthenticated(true);
      setUser(response.data);
    } catch (error) {
      console.error("User is not authenticated", error);
      setIsAuthenticated(false);
      navigate("/login");
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, setIsAuthenticated }}>
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
