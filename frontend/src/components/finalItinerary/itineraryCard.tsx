import { Atom } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";

interface PlaceCardHeaderProps {
  id: string;
  title: string;
  handleClick: (event: React.MouseEvent<HTMLDivElement>) => void;
}

export default function PlaceCardHeader({
  id,
  title = "Default title",
  handleClick,
}: PlaceCardHeaderProps) {
  return (
    <Card
      className="w-full max-w-2xl border bg-card ml-2"
      id={id}
      onClick={handleClick}
    >
      <CardContent className="p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Atom className="h-5 w-5 text-primary" />
            <span className="font-medium">Final Itinerary</span>
          </div>
        </div>
        <div className="mt-2">
          <span className="text-sm text-muted-foreground">{title}</span>
        </div>
      </CardContent>
    </Card>
  );
}
