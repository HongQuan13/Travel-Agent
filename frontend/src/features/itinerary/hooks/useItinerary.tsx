import { useEffect, useState } from "react";

import { testItinerary } from "@/data/testItinerary";
import { fetchItinerary, fetchLatestItinerary } from "../services";
import { ItineraryCardProps } from "../interfaces";

export const useItinerary = (conversationId: string) => {
  const defaultResponse = JSON.parse(testItinerary);
  const [detailItinerary, setDetailItinerary] =
    useState<ItineraryCardProps>(defaultResponse);

  useEffect(() => {
    const retrieveLatestItinerary = async () => {
      try {
        const itineraryDetail = await fetchLatestItinerary(conversationId);
        console.log(itineraryDetail);
        setDetailItinerary(JSON.parse(itineraryDetail));
      } catch (error: any) {
        console.error("Error:", error);
      }
    };

    if (conversationId) retrieveLatestItinerary();
  }, [conversationId]);

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
    setDetailItinerary(content.itineraryDetail);
  };

  return {
    detailItinerary,
    setDetailItinerary,
    handleClickItinerary,
    handleMessageItinerary,
  };
};
