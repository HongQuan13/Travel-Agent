import { MainHeader, SubHeader } from "@/components/finalPlan/header";
import { LocationCard } from "@/components/finalPlan/locationCard";
import { useEffect, useRef } from "react";
import { Card, CardContent } from "@/components/ui/card";

function FinalPlan() {
  const response = `{"isFinalized": true, "mainHead": "2-Day Trip to India", "subHeaders": {"Day 1: Exploring Delhi": [{"placeName": "Red Fort", "location": "Delhi, India", "description": "Start your day with a visit to this iconic UNESCO World Heritage site.", "images": []}, {"placeName": "Local Cafe", "location": "Delhi, India", "description": "Enjoy a traditional Indian breakfast at a local cafe.", "images": []}, {"placeName": "Jama Masjid", "location": "Delhi, India", "description": "One of the largest mosques in India.", "images": []}, {"placeName": "Karim's", "location": "Delhi, India", "description": "Famous for its Mughlai cuisine.", "images": []}, {"placeName": "India Gate and Rashtrapati Bhavan", "location": "Delhi, India", "description": "Enjoy a leisurely walk around these historic landmarks.", "images": []}, {"placeName": "Connaught Place", "location": "Delhi, India", "description": "Explore shops and enjoy street food.", "images": []}, {"placeName": "Rooftop Restaurant", "location": "Delhi, India", "description": "Enjoy a meal with a view.", "images": []}], "Day 2: Agra Day Trip": [{"placeName": "Travel to Agra", "location": "Agra, India", "description": "Take an early morning train or hire a car.", "images": []}, {"placeName": "Taj Mahal", "location": "Agra, India", "description": "Explore this wonder of the world.", "images": []}, {"placeName": "Local Restaurant", "location": "Agra, India", "description": "Enjoy local cuisine.", "images": []}, {"placeName": "Agra Fort", "location": "Agra, India", "description": "Another UNESCO World Heritage site.", "images": []}, {"placeName": "Return to Delhi", "location": "Delhi, India", "description": "Travel back to Delhi.", "images": []}, {"placeName": "Local Dhaba", "location": "Delhi, India", "description": "Experience authentic Indian food.", "images": []}]}}`;
  const jsonResponse = JSON.parse(response);

  const scrollAreaRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, []);

  return (
    <Card className="h-full border-0 rounded-none">
      <CardContent className="p-6 overflow-auto max-h-full">
        {[jsonResponse].map((plan: any, index: number) => (
          <div key={index}>
            <MainHeader title={plan.mainHead} />
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
