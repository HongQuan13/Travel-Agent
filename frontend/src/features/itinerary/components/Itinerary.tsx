import { useEffect, useRef } from "react";

import { MainHeader, SubHeader } from "./Header";
import { LocationCard } from "./LocationCard";
import { Card, CardContent } from "@/components/ui/card";
import { ImageShow } from "./ImageShow";
import { ItineraryCardProps, LocationCardProps } from "../interfaces";

function Itinerary({
  detailItinerary,
}: {
  detailItinerary: ItineraryCardProps;
}) {
  const scrollAreaRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, []);

  return (
    <Card className="h-full border-0 rounded-none">
      <CardContent className="p-6 overflow-auto max-h-full">
        {[detailItinerary].map((itinerary, index) => (
          <div key={index}>
            <MainHeader title={itinerary.mainHeader} />
            {itinerary.images.length > 0 ? (
              <ImageShow images={itinerary.images} />
            ) : (
              <></>
            )}
            <div className="space-y-8">
              {itinerary.subHeaders.map(
                (subHeader: any, subHeaderIndex: number) => (
                  <section key={subHeaderIndex}>
                    <SubHeader title={subHeader.title} />
                    <div className="space-y-6">
                      {subHeader.places.map(
                        (place: LocationCardProps, placeIndex: number) => (
                          <LocationCard key={placeIndex} locationInfo={place} />
                        )
                      )}
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

export default Itinerary;
