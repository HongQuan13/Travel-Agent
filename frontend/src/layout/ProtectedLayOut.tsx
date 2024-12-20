import { useAuthContext } from "@/context/auth";
import { Navigate, Outlet } from "react-router-dom";

export const ProtectedLayout = () => {
  const { isAuthenticated, user } = useAuthContext();

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return <Outlet />;
};
