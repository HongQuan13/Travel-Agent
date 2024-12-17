import { useEffect, useState } from "react";

import MessageContainer from "@/components/chat/message";
import FinalizePlan from "@/components/finalPlan/plan";
import { Sheet, SheetContent } from "@/components/ui/sheet";
import { axiosClient } from "@/lib/axios";
import { useWebSocket } from "@/context/websocket";
import { PlanCardProps, testPlan } from "@/interfaces/interface";

function Chatbot() {
  const [finalPlanView, setFinalPlanView] = useState(false);
  const [mobileView, setMobileView] = useState(false);
  const defaultResponse = JSON.parse(testPlan);
  const [detailPlan, setDetailPlan] = useState<PlanCardProps>(defaultResponse);
  const { message, sendMessage, isConnected } = useWebSocket();

  const handleClickPlan = async (event: React.MouseEvent<HTMLDivElement>) => {
    const id = event.currentTarget.getAttribute("id");

    try {
      //hardcode conversation_id = 1
      const response = await axiosClient.get(`chat/retrieve-plan/${id}`);

      const planDetail = response.data.plan_detail;
      setDetailPlan(JSON.parse(planDetail));
    } catch (error: any) {
      console.error("Error:", error);
    }
  };

  useEffect(() => {
    if (message != "") {
      const content = JSON.parse(message);
      setDetailPlan(content.plan_detail);
    }
  }, [message]);

  useEffect(() => {
    const retrieveLatestPlan = async () => {
      try {
        //hardcode conversation_id = 1
        const response = await axiosClient.get("chat/retrieve-latest-plan/1");

        const planDetail = response.data.plan_detail;
        setDetailPlan(JSON.parse(planDetail));
      } catch (error: any) {
        console.error("Error:", error);
      }
    };

    retrieveLatestPlan();
  }, []);

  return (
    <div className="h-full w-full max-w-[1200px] mx-auto border rounded-lg overflow-hidden flex flex-col lg:flex-row">
      <div className={`h-full ${finalPlanView ? "lg:w-1/2" : "w-full"}`}>
        <MessageContainer
          finalPlanView={finalPlanView}
          setFinalPlan={setFinalPlanView}
          setMobileView={setMobileView}
          handleClickPlan={handleClickPlan}
        />
      </div>

      {finalPlanView && (
        <>
          {/* Mobile and tablet view */}
          <div className="lg:hidden ">
            <Sheet open={mobileView} onOpenChange={setMobileView}>
              <SheetContent side="bottom" className="h-[85vh] p-0 lg:hidden">
                <FinalizePlan detailPlan={detailPlan} />
              </SheetContent>
            </Sheet>
          </div>

          {/* Desktop view */}
          <div className="hidden lg:block w-1/2 h-full">
            <FinalizePlan detailPlan={detailPlan} />
          </div>
        </>
      )}
    </div>
  );
}

export default Chatbot;
