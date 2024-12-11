export interface Message {
  message_text: string;
  sender: string;
}

export interface Location {
  id: number;
  name: string;
  description: string;
  images: string[];
}

export interface WebSocketContextType {
  message: string;
  sendMessage: (msg: object) => void;
  isConnected: boolean;
}

export interface WebSocketProviderProps {
  url: string;
  children: React.ReactNode;
}
