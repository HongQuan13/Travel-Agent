import { useEffect, useState } from "react";

import { axiosClient } from "@/lib/axios";
import { ItineraryCardProps } from "@/features/itinerary/components/Itinerary";
import { testItinerary } from "@/data/testItinerary";

export const useItinerary = (conversation_id: string) => {
  //   const [finalItineraryView, setFinalItineraryView] = useState(false);
  //   const [mobileView, setMobileView] = useState(false);
  const defaultResponse = JSON.parse(testItinerary);
  const [detailItinerary, setDetailItinerary] =
    useState<ItineraryCardProps>(defaultResponse);

  useEffect(() => {
    const retrieveLatestItinerary = async () => {
      try {
        const response = await axiosClient.get(
          `chat/retrieve-latest-itinerary/${conversation_id}`
        );

        const itineraryDetail = response.data.itinerary_detail;
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

    try {
      const response = await axiosClient.get(`chat/retrieve-itinerary/${id}`);

      const itineraryDetail = response.data.itinerary_detail;
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
