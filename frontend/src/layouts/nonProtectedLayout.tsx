import { useAuthContext } from "@/context/auth";
import { Navigate, Outlet } from "react-router-dom";

interface IProps {
  fallbackRoute: string;
}

export const NonProtectedLayout = ({ fallbackRoute }: IProps) => {
  const { isAuthenticated, user } = useAuthContext();

  if (isAuthenticated) {
    return <Navigate to={fallbackRoute} />;
  }

  return <Outlet />;
};
