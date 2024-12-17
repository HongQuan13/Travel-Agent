import { Card, CardContent } from "@/components/ui/card";
import { Atom } from "lucide-react";

export default function PlaceCardHeader({
  id,
  title = "Default title",
}: {
  id: string;
  title?: string;
}) {
  return (
    <Card className="w-full max-w-2xl border bg-card ml-2" id={id}>
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
