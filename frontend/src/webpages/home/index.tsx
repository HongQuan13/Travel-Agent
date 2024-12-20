import { ArrowUp } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <Card className="w-full max-w-3xl">
        <CardHeader>
          <CardTitle className="text-4xl font-bold text-center">
            Hi, I'm your personal travel agent
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="relative">
            <Input
              placeholder="Let's plan your trip..."
              className="pr-24 pl-20"
            />
            <div className="absolute right-1 top-1/2 -translate-y-1/2 flex items-center gap-2">
              <Button variant="outline" size="icon" className="h-8 w-8">
                <ArrowUp className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
