import { useState, useEffect } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { cn } from "@/lib/utils";
import { Review, ReviewsProps } from "../interfaces";

export function Reviews({ reviews }: ReviewsProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedReview, setSelectedReview] = useState<Review | null>(null);
  const [isOpen, setIsOpen] = useState(false);

  // Auto slide every 5 seconds
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((current) => (current + 1) % reviews.length);
    }, 5000);

    return () => clearInterval(timer);
  }, [reviews.length]);

  const handlePrevious = () => {
    setCurrentIndex(
      (current) => (current - 1 + reviews.length) % reviews.length
    );
  };

  const handleNext = () => {
    setCurrentIndex((current) => (current + 1) % reviews.length);
  };

  const handleReviewClick = (review: Review) => {
    setSelectedReview(review);
    setIsOpen(true);
  };

  return (
    <div className="relative mt-6 px-4">
      <div className="overflow-hidden">
        <div
          className="flex transition-transform duration-300 ease-in-out cursor-pointer"
          style={{ transform: `translateX(-${currentIndex * 100}%)` }}
          onClick={() => handleReviewClick(reviews[currentIndex])}
        >
          {reviews.map((review: Review) => (
            <div className="w-full flex-shrink-0 px-4">
              <div className="bg-muted/50 rounded-lg p-4">
                <div className="flex items-center justify-between mb-2">
                  <span className="font-medium">{review?.author_name}</span>
                  <div className="flex">
                    {[...Array(5)].map((_, i) => (
                      <span
                        key={i}
                        className={cn(
                          "h-4 w-4",
                          i < review?.rating
                            ? "text-yellow-400"
                            : "text-gray-300"
                        )}
                      >
                        ★
                      </span>
                    ))}
                  </div>
                </div>
                <p className="text-muted-foreground line-clamp-3">
                  {review?.text}
                </p>
                <span className="text-sm text-muted-foreground mt-2 block">
                  {review?.relative_time_description}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {reviews.length > 1 && (
        <>
          <Button
            variant="ghost"
            size="icon"
            className="absolute left-0 top-1/2 -translate-y-1/2"
            onClick={handlePrevious}
          >
            <ChevronLeft className="h-4 w-4" />
          </Button>
          <Button
            variant="ghost"
            size="icon"
            className="absolute right-0 top-1/2 -translate-y-1/2"
            onClick={handleNext}
          >
            <ChevronRight className="h-4 w-4" />
          </Button>
        </>
      )}

      <Dialog open={isOpen} onOpenChange={setIsOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Review by {selectedReview?.author_name}</DialogTitle>
          </DialogHeader>
          <div className="mt-4">
            <div className="flex mb-2">
              {[...Array(selectedReview?.rating || 0)].map((_, i) => (
                <span key={i} className="text-yellow-400">
                  ★
                </span>
              ))}
            </div>
            <p className="text-muted-foreground">{selectedReview?.text}</p>
            <span className="text-sm text-muted-foreground mt-4 block">
              {selectedReview?.relative_time_description}
            </span>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
