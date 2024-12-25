import { fetchData } from "@/services/api";

export const fetchLatestItinerary = async (conversationId: string) => {
  const response = await fetchData(
    `chat/retrieve-latest-itinerary/${conversationId}`
  );

  return response.itineraryDetail;
};

export const fetchItinerary = async (id: string) => {
  const response = await fetchData(`chat/retrieve-itinerary/${id}`);

  return response.itineraryDetail;
};
