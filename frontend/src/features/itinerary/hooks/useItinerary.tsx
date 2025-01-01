import { useEffect, useState } from "react";

import { fetchItinerary, fetchLatestItinerary } from "../services";
import { ItineraryCardProps } from "../interfaces";
import { transformBackendDataToFrontend } from "@/utils/variableConversion";

export const useItinerary = (conversationId: string) => {
  const [detailItinerary, setDetailItinerary] =
    useState<ItineraryCardProps | null>(null);

  useEffect(() => {
    const retrieveLatestItinerary = async () => {
      try {
        const itineraryDetail = await fetchLatestItinerary(conversationId);
        setDetailItinerary(itineraryDetail);
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
      setDetailItinerary(itineraryDetail);
    } catch (error: any) {
      console.error("Error:", error);
    }
  };

  const handleMessageItinerary = (message: string) => {
    const content = JSON.parse(message);
    const transformedData = transformBackendDataToFrontend(content);

    if (transformedData.conversationId == conversationId)
      setDetailItinerary(transformedData.itineraryDetail);
  };

  return {
    detailItinerary,
    setDetailItinerary,
    handleClickItinerary,
    handleMessageItinerary,
  };
};
