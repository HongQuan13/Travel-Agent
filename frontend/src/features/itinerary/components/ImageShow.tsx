import { useState } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";

import { Button } from "@/components/ui/button";

export interface ImageCard {
  image_url: string;
}

export function ImageShow({ images = [] }: { images: ImageCard[] }) {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const nextImage = () => {
    setCurrentImageIndex((prev) => (prev + 1) % images.length);
  };

  const previousImage = () => {
    setCurrentImageIndex((prev) => (prev - 1 + images.length) % images.length);
  };

  return (
    <div className="relative mb-6 aspect-video bg-muted rounded-lg overflow-hidden flex justify-center items-center">
      <img
        src={images[currentImageIndex].image_url}
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
  );
}
