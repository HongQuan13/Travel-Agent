import { useEffect, useRef, useState } from "react";

import { MainHeader, SubHeader } from "@/components/finalPlan/header";
import { LocationCard } from "@/components/finalPlan/locationCard";
import { Card, CardContent } from "@/components/ui/card";
import { useWebSocket } from "@/context/websocket";
import { ImageShow } from "./imageShow";
import { PlanCardProps, testPlan } from "@/interfaces/interface";

function FinalPlan() {
  const scrollAreaRef = useRef<HTMLDivElement>(null);
  const defaultResponse = JSON.parse(testPlan);
  const [detailPlan, setDetailPlan] = useState<PlanCardProps>(defaultResponse);
  const { message, sendMessage, isConnected } = useWebSocket();

  useEffect(() => {
    if (message != "") setDetailPlan(JSON.parse(message));
  }, [message]);

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, []);

  return (
    <Card className="h-full border-0 rounded-none">
      <CardContent className="p-6 overflow-auto max-h-full">
        {[detailPlan].map((plan, index) => (
          <div key={index}>
            <MainHeader title={plan.mainHead} />
            <ImageShow images={plan.images} />
            <div className="space-y-8">
              {Object.entries(plan.subHeaders).map(
                ([subHeader, locations]: [string, any]) => (
                  <section key={subHeader}>
                    <SubHeader title={subHeader} />
                    <div className="space-y-6">
                      {locations.map((location: any, locIndex: number) => (
                        <LocationCard key={locIndex} {...location} />
                      ))}
                    </div>
                  </section>
                )
              )}
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
}

export default FinalPlan;
