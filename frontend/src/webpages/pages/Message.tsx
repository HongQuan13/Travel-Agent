import { useEffect, useState } from "react";

import MessageContainer from "@/components/chat/message";
import FinalizeItinerary, {
  ItineraryCardProps,
} from "@/components/finalItinerary/itinerary";
import { Sheet, SheetContent } from "@/components/ui/sheet";
import { axiosClient } from "@/lib/axios";
import { testItinerary } from "@/data/testItinerary";
import { useLocation } from "react-router-dom";
import { useWebSocket } from "@/hooks/useWebSocket";

function Chatbot() {
  const [finalItineraryView, setFinalItineraryView] = useState(false);
  const [mobileView, setMobileView] = useState(false);
  const defaultResponse = JSON.parse(testItinerary);
  const [detailItinerary, setDetailItinerary] =
    useState<ItineraryCardProps>(defaultResponse);
  const { message } = useWebSocket();
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const conversation_id = params.get("conversation_id") ?? "";

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

  useEffect(() => {
    if (message != "") {
      const content = JSON.parse(message);
      setDetailItinerary(content.itinerary_detail);
    }
  }, [message]);

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
  }, []);

  return (
    <div className="h-full w-full max-w-[1200px] mx-auto border rounded-lg overflow-hidden flex flex-col lg:flex-row">
      <div className={`h-full ${finalItineraryView ? "lg:w-1/2" : "w-full"}`}>
        <MessageContainer
          finalItineraryView={finalItineraryView}
          setFinalItinerary={setFinalItineraryView}
          setMobileView={setMobileView}
          handleClickItinerary={handleClickItinerary}
          conversation_id={conversation_id}
        />
      </div>

      {finalItineraryView && (
        <>
          {/* Mobile and tablet view */}
          <div className="lg:hidden ">
            <Sheet open={mobileView} onOpenChange={setMobileView}>
              <SheetContent side="bottom" className="h-[85vh] p-0 lg:hidden">
                <FinalizeItinerary detailItinerary={detailItinerary} />
              </SheetContent>
            </Sheet>
          </div>

          {/* Desktop view */}
          <div className="hidden lg:block w-1/2 h-full">
            <FinalizeItinerary detailItinerary={detailItinerary} />
          </div>
        </>
      )}
    </div>
  );
}

export default Chatbot;
