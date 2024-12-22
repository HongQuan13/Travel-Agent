import { useAuthContext } from "@/context/AuthProvider";
import { Navigate, Outlet } from "react-router-dom";

export const ProtectedLayout = () => {
  const { isAuthenticated } = useAuthContext();

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return <Outlet />;
};
