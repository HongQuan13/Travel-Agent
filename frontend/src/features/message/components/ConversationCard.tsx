import { MoreVertical } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";
import { ConversationProps } from "../interfaces";

function ConversationCard({ item }: { item: ConversationProps }) {
  const timeDifference = (time: string | Date): string => {
    const now = new Date();
    const targetDate = new Date(time);

    const diffInMs = now.getTime() - targetDate.getTime();
    const diffInMinutes = diffInMs / (1000 * 60);
    const diffInHours = diffInMinutes / 60;
    const diffInDays = diffInHours / 24;

    if (diffInMinutes < 60) {
      return `${Math.floor(diffInMinutes)} minutes`;
    } else if (diffInHours < 24) {
      return `${Math.floor(diffInHours)} hours`;
    } else {
      return `${Math.floor(diffInDays)} days`;
    }
  };

  const handleBriefMessage = (message: string): string => {
    if (message) {
      const splitMessage = message.split(" ");
      const briefMessage = splitMessage.slice(0, 10).join(" ");
      return briefMessage;
    }

    return "Default message";
  };

  return (
    <div
      key={item.conversationId}
      className="border rounded-lg p-4 space-y-2 hover:bg-muted/50 transition-colors"
    >
      <Link to={`/chatbot?conversationId=${item.conversationId}`}>
        <div className="flex items-start justify-between gap-2">
          <div className="flex items-center gap-2">
            <h3 className="font-medium">
              {item.conversationTitle ?? "Default title"}
            </h3>
          </div>
          <Button variant="ghost" size="icon" className="h-8 w-8 -mr-2">
            <MoreVertical className="h-4 w-4" />
          </Button>
        </div>

        <p className="text-muted-foreground text-sm">
          {`${handleBriefMessage(item.lastUserMessage)} ...`}
        </p>

        <div className="flex items-center gap-2">
          <span className="text-sm text-muted-foreground ml-auto">
            {`Last update at ${timeDifference(item.updatedAt)} ago`}
          </span>
        </div>
      </Link>
    </div>
  );
}

export default ConversationCard;
