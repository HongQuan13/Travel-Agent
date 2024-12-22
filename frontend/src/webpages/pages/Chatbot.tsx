import { useEffect, useState } from "react";

import MessageContainer from "@/features/message/components/Message";
import { Sheet, SheetContent } from "@/components/ui/sheet";
import { useLocation } from "react-router-dom";
import { useWebSocket } from "@/hooks/useWebSocket";
import { ItineraryComponent } from "@/features/itinerary";
import { useItinerary } from "@/features/itinerary/hooks/useItinerary";

function Chatbot() {
  const [finalItineraryView, setFinalItineraryView] = useState(false);
  const [mobileView, setMobileView] = useState(false);
  const { message } = useWebSocket();
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const conversation_id = params.get("conversation_id") ?? "";
  const { detailItinerary, handleClickItinerary, handleMessageItinerary } =
    useItinerary(conversation_id);

  useEffect(() => {
    if (message) {
      handleMessageItinerary(message);
    }
  }, [message]);

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
                <ItineraryComponent detailItinerary={detailItinerary} />
              </SheetContent>
            </Sheet>
          </div>

          {/* Desktop view */}
          <div className="hidden lg:block w-1/2 h-full">
            <ItineraryComponent detailItinerary={detailItinerary} />
          </div>
        </>
      )}
    </div>
  );
}

export default Chatbot;
