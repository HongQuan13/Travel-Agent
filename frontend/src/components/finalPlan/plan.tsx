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
            <MainHeader title={plan.mainHeader} />
            <ImageShow images={plan.images} />
            <div className="space-y-8">
              {plan.subHeaders.map((subHeader: any, subHeaderIndex: number) => (
                <section key={subHeaderIndex}>
                  <SubHeader title={subHeader.title} />
                  <div className="space-y-6">
                    {subHeader.places.map((place: any, placeIndex: number) => (
                      <LocationCard key={placeIndex} {...place} />
                    ))}
                  </div>
                </section>
              ))}
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
}

export default FinalPlan;
