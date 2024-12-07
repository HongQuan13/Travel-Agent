export interface Message {
  id: string;
  content: string;
  sender: string;
}

export interface Location {
  id: number;
  name: string;
  description: string;
  images: string[];
}
