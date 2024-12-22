import { fetchData } from "@/services/api";

export const fetchLatestItinerary = async (conversation_id: string) => {
  const response = await fetchData(
    `chat/retrieve-latest-itinerary/${conversation_id}`
  );

  return response.itinerary_detail;
};

export const fetchItinerary = async (id: string) => {
  const response = await fetchData(`chat/retrieve-itinerary/${id}`);

  return response.itinerary_detail;
};
