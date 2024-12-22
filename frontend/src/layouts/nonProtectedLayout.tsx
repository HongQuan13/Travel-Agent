import { useAuthContext } from "@/context/AuthProvider";
import { Navigate, Outlet } from "react-router-dom";

interface IProps {
  fallbackRoute: string;
}

export const NonProtectedLayout = ({ fallbackRoute }: IProps) => {
  const { isAuthenticated } = useAuthContext();

  if (isAuthenticated) {
    return <Navigate to={fallbackRoute} />;
  }

  return <Outlet />;
};
