export interface AuthContextType {
  isAuthenticated: boolean;
  user: any;
  setIsAuthenticated: React.Dispatch<React.SetStateAction<boolean>>;
}

export interface AuthProviderProps {
  children: React.ReactNode;
}
