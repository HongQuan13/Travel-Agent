import { useEffect, useState } from "react";

import { ItineraryCardProps } from "../components/Itinerary";
import { testItinerary } from "@/data/testItinerary";
import { fetchItinerary, fetchLatestItinerary } from "../services";

export const useItinerary = (conversation_id: string) => {
  const defaultResponse = JSON.parse(testItinerary);
  const [detailItinerary, setDetailItinerary] =
    useState<ItineraryCardProps>(defaultResponse);

  useEffect(() => {
    const retrieveLatestItinerary = async () => {
      try {
        const itineraryDetail = await fetchLatestItinerary(conversation_id);
        setDetailItinerary(JSON.parse(itineraryDetail));
      } catch (error: any) {
        console.error("Error:", error);
      }
    };

    if (conversation_id) retrieveLatestItinerary();
  }, [conversation_id]);

  const handleClickItinerary = async (
    event: React.MouseEvent<HTMLDivElement>
  ) => {
    const id = event.currentTarget.getAttribute("id");
    if (!id) return;

    try {
      const itineraryDetail = await fetchItinerary(id);
      setDetailItinerary(JSON.parse(itineraryDetail));
    } catch (error: any) {
      console.error("Error:", error);
    }
  };

  const handleMessageItinerary = (message: string) => {
    const content = JSON.parse(message);
    setDetailItinerary(content.itinerary_detail);
  };

  return {
    detailItinerary,
    setDetailItinerary,
    handleClickItinerary,
    handleMessageItinerary,
  };
};
