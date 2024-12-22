import { useAuthContext } from "@/features/auth/context/AuthContext";
import { Navigate, Outlet } from "react-router-dom";

export const ProtectedLayout = () => {
  const { isAuthenticated } = useAuthContext();

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return <Outlet />;
};
