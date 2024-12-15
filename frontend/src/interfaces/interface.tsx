export interface Message {
  message_text: string;
  sender: string;
}

export interface LocationCardProps {
  placeName: string;
  description: string;
  googleMapsUrl?: string;
  instagramUrl?: string;
  tiktokUrl?: string;
}

export interface PlanCardProps {
  mainHead: string;
  images: string[];
  subHeaders: object;
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

export const testPlan = `{"mainHead": "2-Day Trip to India", "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRN7fIsq7JVP045499zcXJmse5_m0RTXbXkxrlRbQ-Bm_mJMpkEMFep6aqOow&s",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2G-luksTRsr2Qm7f1lp7eoaLVq5vG3S7yLousPRfvaA1fVP7CS7stP7KwrxE&s",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlcY06-Ar-SMr3uWTbL7_avJWxZjt4b7oxDWNxQA9fSAramw7Qbzclc3oEZg&s",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_grCZAZpgH5IqBZqmcXMSUUXlp0561CnM-LNMxJLr3eOczlWduXYUW7guzg&s",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2L7RSlOxJMxCdE_nAbQOQV3qMvE-r4HYQRGkhx8ibmz9BITOkvmRSBeG9Xg&s"], "subHeaders": {"Day 1: Exploring Delhi": [{"placeName": "Red Fort", "location": "Delhi, India", "description": "Start your day with a visit to this iconic UNESCO World Heritage site."}, {"placeName": "Local Cafe", "location": "Delhi, India", "description": "Enjoy a traditional Indian breakfast at a local cafe."}, {"placeName": "Jama Masjid", "location": "Delhi, India", "description": "One of the largest mosques in India."}, {"placeName": "Karim's", "location": "Delhi, India", "description": "Famous for its Mughlai cuisine."}, {"placeName": "India Gate and Rashtrapati Bhavan", "location": "Delhi, India", "description": "Enjoy a leisurely walk around these historic landmarks."}, {"placeName": "Connaught Place", "location": "Delhi, India", "description": "Explore shops and enjoy street food."}, {"placeName": "Rooftop Restaurant", "location": "Delhi, India", "description": "Enjoy a meal with a view."}], "Day 2: Agra Day Trip": [{"placeName": "Travel to Agra", "location": "Agra, India", "description": "Take an early morning train or hire a car."}, {"placeName": "Taj Mahal", "location": "Agra, India", "description": "Explore this wonder of the world."}, {"placeName": "Local Restaurant", "location": "Agra, India", "description": "Enjoy local cuisine."}, {"placeName": "Agra Fort", "location": "Agra, India", "description": "Another UNESCO World Heritage site."}, {"placeName": "Return to Delhi", "location": "Delhi, India", "description": "Travel back to Delhi."}, {"placeName": "Local Dhaba", "location": "Delhi, India", "description": "Experience authentic Indian food."}]}}`;
