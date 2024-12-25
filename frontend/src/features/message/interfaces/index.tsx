export interface ConversationProps {
  conversationId: string;
  conversationTitle: string;
  lastUserMessage: string;
  updatedAt: string;
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
  conversationId: string;
}
