import { Instagram, MapPin, MoreVertical, Bookmark, Play } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { InfoItem } from "./InfoItem";
import { LocationCardProps } from "../interfaces";
import { SiGooglemaps } from "react-icons/si";

export function LocationCard({
  locationInfo,
}: {
  locationInfo: LocationCardProps;
}) {
  return (
    <Card className="bg-card">
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <div className="bg-primary/10 w-8 h-8 rounded-full flex items-center justify-center">
              <MapPin className="h-4 w-4 text-primary" />
            </div>
            <h3 className="text-xl font-semibold">{locationInfo.placeName}</h3>
          </div>
          <div className="flex items-center gap-2">
            <Button variant="ghost" size="icon" className="rounded-full">
              <Bookmark className="h-4 w-4" />
            </Button>
            <Button variant="ghost" size="icon" className="rounded-full">
              <MoreVertical className="h-4 w-4" />
            </Button>
          </div>
        </div>
        <>
          <p className="text-muted-foreground mb-6">
            {locationInfo.description}
            <InfoItem placeInfo={locationInfo} />
          </p>
        </>
        <div className="flex items-center justify-between">
          <div className="flex gap-2">
            {locationInfo.instagramUrl && (
              <Button variant="outline" size="icon" className="rounded-full">
                <Instagram className="h-4 w-4" />
              </Button>
            )}
            {locationInfo.tiktokUrl && (
              <Button variant="outline" size="icon" className="rounded-full">
                <Play className="h-4 w-4" />
              </Button>
            )}
          </div>
          <Button
            variant="outline"
            className="rounded-full"
            onClick={() => {
              window.open(
                `https://maps.google.com/?q=${locationInfo.placeName}`
              );
            }}
          >
            <SiGooglemaps size={32} className="text-blue-500" />
            Google Maps
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
