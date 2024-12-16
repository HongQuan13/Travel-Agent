import React, { createContext, useContext, useEffect, useState } from "react";
import {
  WebSocketContextType,
  WebSocketProviderProps,
} from "@/interfaces/interface";
import { AutoReconnectWebSocket } from "./autoReconnectWebsocket";

const WebSocketContext = createContext<WebSocketContextType | null>(null);

export const WebSocketProvider: React.FC<WebSocketProviderProps> = ({
  url,
  children,
}) => {
  const [message, setMessage] = useState<string>("");
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [wsClient, setWsClient] = useState<AutoReconnectWebSocket | null>(null);

  useEffect(() => {
    const client = new AutoReconnectWebSocket(url, {
      reconnectInterval: 1000,
      maxReconnectAttempts: 20,
    });

    setWsClient(client);

    const handleMessage = (msg: string) => {
      setMessage(msg);
    };

    client.onMessage = handleMessage;

    const interval = setInterval(() => {
      setIsConnected(client.isConnected());
    }, 1000);

    return () => {
      client.close();
      clearInterval(interval);
    };
  }, [url]);

  const sendMessage = (message: string) => {
    if (wsClient) {
      wsClient.send(message);
    } else {
      console.error("WebSocket client is not initialized.");
    }
  };

  const close = () => {
    wsClient?.close();
  };

  return (
    <WebSocketContext.Provider
      value={{ close, message, sendMessage, isConnected }}
    >
      {children}
    </WebSocketContext.Provider>
  );
};

export const useWebSocket = (): WebSocketContextType => {
  const context = useContext(WebSocketContext);
  if (!context) {
    throw new Error("useWebSocket must be used within a WebSocketProvider");
  }
  return context;
};
