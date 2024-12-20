import { Lock, MoreVertical } from "lucide-react";

import { Button } from "@/components/ui/button";

interface ConversationProps {
  conversation_id: string;
  title: string;
  message: string;
  updatedAt: string;
}

function ConversationCard({ item }: { item: ConversationProps }) {
  return (
    <div
      key={item.conversation_id}
      className="border rounded-lg p-4 space-y-2 hover:bg-muted/50 transition-colors"
    >
      <div className="flex items-start justify-between gap-2">
        <div className="flex items-center gap-2">
          <h3 className="font-medium">{item.title}</h3>
        </div>
        <Button variant="ghost" size="icon" className="h-8 w-8 -mr-2">
          <MoreVertical className="h-4 w-4" />
        </Button>
      </div>

      <p className="text-muted-foreground text-sm">{item.message}</p>

      <div className="flex items-center gap-2">
        <span className="text-sm text-muted-foreground ml-auto">
          {item.updatedAt}
        </span>
      </div>
    </div>
  );
}

export default ConversationCard;
