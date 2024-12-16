import { Card, CardContent } from "@/components/ui/card";
import { Atom } from "lucide-react";

export default function PlaceCardHeader() {
  return (
    <Card className="w-full max-w-2xl border bg-card">
      <CardContent className="p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Atom className="h-5 w-5 text-primary" />
            <span className="font-medium">Place Card</span>
          </div>
          <span className="text-sm text-muted-foreground">v1</span>
        </div>
        <div className="mt-2">
          <span className="text-sm text-muted-foreground">
            Generated place-card.tsx
          </span>
        </div>
      </CardContent>
    </Card>
  );
}
