import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import {
  ChevronLeft,
  ChevronRight,
  Instagram,
  MapPin,
  MoreVertical,
  Bookmark,
  Play,
} from "lucide-react";

interface LocationCardProps {
  placeName: string;
  description: string;
  images?: string[];
  googleMapsUrl?: string;
  instagramUrl?: string;
  tiktokUrl?: string;
}

export function LocationCard({
  placeName,
  description,
  images = [],
  googleMapsUrl = "",
  instagramUrl = "",
  tiktokUrl = "",
}: LocationCardProps) {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const nextImage = () => {
    setCurrentImageIndex((prev) => (prev + 1) % images.length);
  };

  const previousImage = () => {
    setCurrentImageIndex((prev) => (prev - 1 + images.length) % images.length);
  };

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

        <div className="relative mb-6 aspect-video bg-muted rounded-lg overflow-hidden">
          <img
            src={images[currentImageIndex]}
            alt={`${name} view ${currentImageIndex + 1}`}
            className="object-cover"
          />
          <div className="absolute inset-0 flex items-center justify-between p-2">
            <Button
              variant="secondary"
              size="icon"
              onClick={previousImage}
              className="h-8 w-8 rounded-full"
            >
              <ChevronLeft className="h-4 w-4" />
            </Button>
            <Button
              variant="secondary"
              size="icon"
              onClick={nextImage}
              className="h-8 w-8 rounded-full"
            >
              <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
          <div className="absolute bottom-4 right-4 flex gap-2">
            {images.map((_, index) => (
              <div
                key={index}
                className={`w-1.5 h-1.5 rounded-full ${
                  index === currentImageIndex ? "bg-white" : "bg-white/50"
                }`}
              />
            ))}
          </div>
        </div>

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
