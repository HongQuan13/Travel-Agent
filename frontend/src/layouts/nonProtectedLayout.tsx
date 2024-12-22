import { useAuthContext } from "@/features/auth";
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
