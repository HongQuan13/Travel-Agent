import { useState } from "react";

import MessageContainer from "@/components/chat/message";
import FinalizePlan from "@/components/chat/finalPlan";
import { Sheet, SheetContent } from "@/components/ui/sheet";

function Chatbot() {
  const [finalPlanView, setFinalPlanView] = useState(false);
  const [mobileView, setMobileView] = useState(false);

  return (
    <div className="h-full w-full max-w-[1200px] mx-auto border rounded-lg overflow-hidden flex flex-col lg:flex-row">
      <div className={`h-full ${finalPlanView ? "lg:w-1/2" : "w-full"}`}>
        <MessageContainer
          finalPlanView={finalPlanView}
          setFinalPlan={setFinalPlanView}
          setMobileView={setMobileView}
        />
      </div>

      {finalPlanView && (
        <>
          {/* Mobile and tablet view */}
          <div className="lg:hidden ">
            <Sheet open={mobileView} onOpenChange={setMobileView}>
              <SheetContent side="bottom" className="h-[85vh] p-0 lg:hidden">
                <FinalizePlan />
              </SheetContent>
            </Sheet>
          </div>

          {/* Desktop view */}
          <div className="hidden lg:block w-1/2 h-full">
            <FinalizePlan />
          </div>
        </>
      )}
    </div>
  );
}

export default Chatbot;
