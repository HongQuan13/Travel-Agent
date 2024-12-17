export interface Message {
  content: string;
  sender: string;
  category?: "itinerary" | "text";
}

export interface LocationCardProps {
  placeName: string;
  description: string;
  address: string;
  price: string;
  googleMapsUrl?: string;
  instagramUrl?: string;
  tiktokUrl?: string;
}
export interface ImageCard {
  image_url: string;
}

export interface ItineraryCardProps {
  mainHeader: string;
  images: ImageCard[];
  subHeaders: object[];
}

export interface WebSocketContextType {
  message: string;
  sendMessage: (msg: string) => void;
  isConnected: boolean;
  close: () => void;
}

export interface WebSocketProviderProps {
  url: string;
  children: React.ReactNode;
}

export interface PlaceCardHeaderProps {
  id: string;
  title: string;
  handleClick: (event: React.MouseEvent<HTMLDivElement>) => void;
}

export const testItinerary = `{"mainHeader": "Day Trip in Singapore: Nature, Culture, and Food", "images": [{"image_url": "https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/v2dtdyvuddly2u2ehfzz"}, {"image_url": "https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/txlna9uwcgsruvebvcst"}, {"image_url": "https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/j2kxf2yx4sv7rxlfc41b"}, {"image_url": "https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/yij5kzyj6ylzadyqm7nu"}, {"image_url": "https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/u3cupkuxn3qxv2rxlfdb"}], "subHeaders": [{"title": "Morning: Gardens by the Bay", "places": [{"placeName": "Gardens by the Bay", "address": "18 Marina Gardens Dr, Singapore 018953", "description": "Start your day with a visit to this iconic garden featuring the Supertree Grove, Cloud Forest, and Flower Dome. It's a perfect blend of nature and technology."}]}, {"title": "Midday: Explore Chinatown", "places": [{"placeName": "Chinatown", "address": "Chinatown, Singapore", "description": "Explore the rich cultural heritage of Chinatown. Visit the Buddha Tooth Relic Temple and Museum, and enjoy some local street food at the Chinatown Food Street."}]}, {"title": "Afternoon: National Museum of Singapore", "places": [{"placeName": "National Museum of Singapore", "address": "93 Stamford Rd, Singapore 178897", "description": "Dive into Singapore's history and culture at the National Museum. It's the oldest museum in Singapore, offering a modern and interactive experience."}]}, {"title": "Evening: Marina Bay Sands SkyPark", "places": [{"placeName": "Marina Bay Sands SkyPark", "address": "10 Bayfront Ave, Singapore 018956", "description": "End your day with a breathtaking view of the city skyline from the SkyPark Observation Deck. It's a perfect spot to relax and enjoy the sunset."}]}, {"title": "Dinner: Lau Pa Sat", "places": [{"placeName": "Lau Pa Sat", "address": "18 Raffles Quay, Singapore 048582", "description": "Enjoy a variety of local dishes at this famous hawker center. It's a great place to experience Singapore's diverse culinary scene."}]}]}`;
