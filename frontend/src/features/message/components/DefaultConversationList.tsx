import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter } from "@/components/ui/card";
import { MessageSquarePlus } from "lucide-react";
import { useNavigate } from "react-router-dom";

function DefaultConversationList() {
  const navigate = useNavigate();
  return (
    <div className="flex items-center justify-center min-h-screen">
      <Card className="w-full max-w-md">
        <CardContent className="pt-6 text-center">
          <h2 className="mt-2 text-xl font-semibold text-gray-900">
            No conversations yet
          </h2>
          <p className="mt-1 text-sm text-gray-500">
            Get started by creating a new conversation.
          </p>
        </CardContent>
        <CardFooter className="flex flex-col space-y-2">
          <Button className="w-full" size="lg" onClick={() => navigate("/")}>
            <MessageSquarePlus className="mr-2 h-4 w-4" />
            Start New Conversation Here
          </Button>
        </CardFooter>
      </Card>
    </div>
  );
}

export default DefaultConversationList;
