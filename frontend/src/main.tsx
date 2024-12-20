import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "@/index.css";
import App from "@/App.tsx";
import { WebSocketProvider } from "@/context/websocket.tsx";
import { AuthProvider } from "@/context/auth";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <WebSocketProvider url={import.meta.env.VITE_WEBSOCKET_URL}>
        <AuthProvider>
          <App />
        </AuthProvider>
      </WebSocketProvider>
    </BrowserRouter>
  </StrictMode>
);
