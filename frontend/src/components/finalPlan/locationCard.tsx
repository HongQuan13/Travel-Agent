import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Instagram, MapPin, MoreVertical, Bookmark, Play } from "lucide-react";
import { LocationCardProps } from "@/interfaces/interface";

export function LocationCard({
  placeName,
  description,
  googleMapsUrl = "",
  instagramUrl = "",
  tiktokUrl = "",
}: LocationCardProps) {
  return (
    <Card className="bg-card">
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <div className="bg-primary/10 w-8 h-8 rounded-full flex items-center justify-center">
              <MapPin className="h-4 w-4 text-primary" />
            </div>
            <h3 className="text-xl font-semibold">{placeName}</h3>
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

        <p className="text-muted-foreground mb-6">{description}</p>
        <div className="flex items-center justify-between">
          <div className="flex gap-2">
            {instagramUrl && (
              <Button variant="outline" size="icon" className="rounded-full">
                <Instagram className="h-4 w-4" />
              </Button>
            )}
            {tiktokUrl && (
              <Button variant="outline" size="icon" className="rounded-full">
                <Play className="h-4 w-4" />
              </Button>
            )}
          </div>
          <Button
            variant="outline"
            className="rounded-full"
            onClick={() => window.open(googleMapsUrl, "_blank")}
          >
            <img
              src="/placeholder.svg?height=16&width=16"
              alt="Google Maps"
              width={16}
              height={16}
              className="mr-2"
            />
            Google Maps
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
