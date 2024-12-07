import React from "react";
import { Location } from "@/interfaces/chat";
import { Card, CardContent } from "../ui/card";
import {
  Share2,
  Instagram,
  Map,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";
import { Button } from "../ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../ui/tabs";

function FinalizePlan() {
  const [currentImageIndex, setCurrentImageIndex] = React.useState(0);

  const location: Location = {
    id: 1,
    name: "Space Needle",
    description:
      "The iconic Space Needle offers panoramic views of Seattle and the surrounding landscape, making it a must-visit destination for capturing stunning Instagram photos.",
    images: [
      "/placeholder.svg?height=400&width=600",
      "/placeholder.svg?height=400&width=600",
      "/placeholder.svg?height=400&width=600",
    ],
  };

  const nextImage = () => {
    setCurrentImageIndex((prev) => (prev + 1) % location.images.length);
  };

  const previousImage = () => {
    setCurrentImageIndex(
      (prev) => (prev - 1 + location.images.length) % location.images.length
    );
  };

  return (
    <Card className="h-full border-0 rounded-none">
      <CardContent className="p-6 overflow-auto max-h-full">
        <div className="flex items-start justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold mb-2">{location.name}</h2>
            <div className="flex items-center gap-2">
              <Instagram className="h-5 w-5" />
              <Map className="h-5 w-5" />
            </div>
          </div>
          <Button variant="ghost" size="icon">
            <Share2 className="h-5 w-5" />
          </Button>
        </div>

        <div className="relative mb-6 aspect-video bg-muted rounded-lg overflow-hidden">
          <img
            src={location.images[currentImageIndex]}
            alt={`${location.name} view ${currentImageIndex + 1}`}
            className="object-cover"
          />
          <div className="absolute inset-0 flex items-center justify-between p-2">
            <Button
              variant="secondary"
              size="icon"
              className="h-8 w-8"
              onClick={previousImage}
            >
              <ChevronLeft className="h-4 w-4" />
            </Button>
            <Button
              variant="secondary"
              size="icon"
              className="h-8 w-8"
              onClick={nextImage}
            >
              <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
        </div>

        <Tabs defaultValue="overview" className="w-full">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="bydays">By Days</TabsTrigger>
          </TabsList>
          <TabsContent value="overview">
            <p className="text-muted-foreground">{location.description}</p>
          </TabsContent>
          <TabsContent value="bydays">
            <div className="space-y-4">
              <h3 className="font-semibold">Day 1</h3>
              <p className="text-muted-foreground">
                Visit the Space Needle in the morning for the best lighting
                conditions. The observation deck opens at 10 AM.
              </p>
            </div>
          </TabsContent>
        </Tabs>
      </CardContent>
    </Card>
  );
}

export default FinalizePlan;
