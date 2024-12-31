import { Search } from "lucide-react";
import { useEffect, useState } from "react";

import { Input } from "@/components/ui/input";
import { ConversationCard, fetchConversationHistory } from "@/features/message";

export default function ConversationHistory() {
  const [conversationHistory, setConversationHistory] = useState<any>([]);

  useEffect(() => {
    retrieveConversationHistory();
  }, []);

  const retrieveConversationHistory = async () => {
    try {
      const conversations = await fetchConversationHistory();
      setConversationHistory(conversations);
    } catch (error) {
      console.log("Retrieve conversation history error", error);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-4 space-y-4">
      {/* <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input placeholder="Search for a chat..." className="pl-9" />
      </div> */}

      <div className="space-y-4">
        {conversationHistory.map((item: any) => (
          <ConversationCard item={item} />
        ))}
      </div>
    </div>
  );
}
