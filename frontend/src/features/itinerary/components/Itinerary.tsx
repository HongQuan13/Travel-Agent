import { useEffect, useRef } from "react";

import { MainHeader, SubHeader } from "./Header";
import { LocationCard } from "./LocationCard";
import { Card, CardContent } from "@/components/ui/card";
import { ImageCard, ImageShow } from "./ImageShow";

export interface ItineraryCardProps {
  mainHeader: string;
  images: ImageCard[];
  subHeaders: object[];
}

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
            <ImageShow images={itinerary.images} />
            <div className="space-y-8">
              {itinerary.subHeaders.map(
                (subHeader: any, subHeaderIndex: number) => (
                  <section key={subHeaderIndex}>
                    <SubHeader title={subHeader.title} />
                    <div className="space-y-6">
                      {subHeader.places.map(
                        (place: any, placeIndex: number) => (
                          <LocationCard key={placeIndex} {...place} />
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
