import { useContext } from "react";

import {
  WebSocketContext,
  WebSocketContextType,
} from "@/context/WebSocketProvider";

export const useWebSocket = (): WebSocketContextType => {
  const context = useContext(WebSocketContext);
  if (!context) {
    throw new Error("useWebSocket must be used within a WebSocketProvider");
  }
  return context;
};