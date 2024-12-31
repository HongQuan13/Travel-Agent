import { useState } from "react";
import { ArrowUp } from "lucide-react";
import { useNavigate } from "react-router-dom";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { createConversation } from "@/features/message";

export default function Home() {
  const [inputValue, setInputValue] = useState("");
  const navigate = useNavigate();

  const handleSendMessage = async () => {
    try {
      if (inputValue == "") return;

      const newConversation = await createConversation(inputValue);
      const conversationId = newConversation.conversationId;
      navigate(`/chatbot?conversationId=${conversationId}`);
    } catch (error) {
      console.log("handle send message error", error);
    }
  };

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
            <form
              onSubmit={(e) => {
                e.preventDefault();
              }}
            >
              <Input
                placeholder="Let's plan your trip..."
                className="pr-24 pl-20"
                onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                  setInputValue(e.target.value)
                }
              />
              <div className="absolute right-1 top-1/2 -translate-y-1/2 flex items-center gap-2">
                <Button
                  variant="outline"
                  size="icon"
                  className="h-8 w-8"
                  onClick={handleSendMessage}
                >
                  <ArrowUp className="h-4 w-4" />
                </Button>
              </div>
            </form>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
