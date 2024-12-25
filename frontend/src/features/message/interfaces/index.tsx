export interface ConversationProps {
  conversation_id: string;
  conversation_title: string;
  last_user_message: string;
  updated_at: string;
}

type Category = "itinerary" | "text";

export interface Message {
  id?: number;
  content: string;
  sender: string;
  category?: Category;
}

export interface MessageContainerProps {
  finalItineraryView: Boolean;
  setFinalItinerary: React.Dispatch<React.SetStateAction<boolean>>;
  setMobileView: React.Dispatch<React.SetStateAction<boolean>>;
  handleClickItinerary: (event: React.MouseEvent<HTMLDivElement>) => void;
  conversation_id: string;
}
