import { Card, CardContent } from "@/components/ui/card";
import { Atom } from "lucide-react";

export default function PlaceCardHeader({
  title = "Default title",
}: {
  title?: string;
}) {
  return (
    <Card className="w-1/2 max-w-2xl border bg-card ml-10">
      <CardContent className="p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Atom className="h-5 w-5 text-primary" />
            <span className="font-medium">Final Initerary</span>
          </div>
        </div>
        <div className="mt-2">
          <span className="text-sm text-muted-foreground">{title}</span>
        </div>
      </CardContent>
    </Card>
  );
}
