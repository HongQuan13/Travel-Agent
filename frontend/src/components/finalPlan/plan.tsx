import { MainHeader, SubHeader } from "@/components/finalPlan/header";
import { LocationCard } from "@/components/finalPlan/locationCard";
import { useEffect, useRef } from "react";
import { Card, CardContent } from "@/components/ui/card";

function FinalPlan() {
  const locations = [
    {
      name: "Space Needle",
      description:
        "The iconic Space Needle offers panoramic views of Seattle and the surrounding landscape, making it a must-visit destination for capturing stunning Instagram photos.",
      images: [
        "/placeholder.svg?height=400&width=600",
        "/placeholder.svg?height=400&width=600",
        "/placeholder.svg?height=400&width=600",
      ],
      googleMapsUrl: "https://maps.google.com/?q=Space+Needle",
      instagramUrl: "https://instagram.com/spaceneedle",
      tiktokUrl: "https://tiktok.com/@spaceneedle",
    },
    {
      name: "Pike Place Market",
      description:
        "A historic public market overlooking the Elliott Bay waterfront. Known for its fresh produce, flying fish, and the original Starbucks store.",
      images: [
        "/placeholder.svg?height=400&width=600",
        "/placeholder.svg?height=400&width=600",
      ],
      googleMapsUrl: "https://maps.google.com/?q=Pike+Place+Market",
      instagramUrl: "https://instagram.com/pikeplace",
    },
  ];

  const scrollAreaRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, []);

  return (
    <Card className="h-full border-0 rounded-none">
      <CardContent className="p-6 overflow-auto max-h-full">
        <MainHeader title="Seattle Instagram Getaway" />

        <div className="space-y-8">
          <section>
            <SubHeader title="Day 1" />
            <div className="space-y-6">
              {locations.map((location, index) => (
                <LocationCard key={index} {...location} />
              ))}
            </div>
          </section>
        </div>
      </CardContent>
    </Card>
  );
}

export default FinalPlan;
