export interface Message {
  id: string;
  message_text: string;
  sender: string;
}

export interface Location {
  id: number;
  name: string;
  description: string;
  images: string[];
}
