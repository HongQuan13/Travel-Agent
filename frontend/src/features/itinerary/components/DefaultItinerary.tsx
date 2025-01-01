import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

function DefaultItinerary() {
  return (
    <div className="h-full w-full bg-center flex items-center justify-center p-4 bg-slate-50">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-center">
            Ready to Plan Your Trip?
          </CardTitle>
          <CardDescription className="text-center">
            Let our AI assistant help you create the perfect itinerary
          </CardDescription>
        </CardHeader>
        <CardContent className="flex flex-col items-center space-y-4">
          <div className="text-4xl font-bold text-primary animate-pulse">
            Start asking chatbot
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
export default DefaultItinerary;
