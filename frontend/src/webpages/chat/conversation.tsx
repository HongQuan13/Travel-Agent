import { Lock, MoreVertical, Search } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import ConversationCard from "@/components/chat/conversationCard";

const chatItems: any[] = [
  {
    conversation_id: "1",
    title: "Custom chatbot design",
    message:
      "Design like this for me. a chatbot at the center. using tailwind css and shadcn",
    updatedAt: "Updated 9 minutes ago",
  },
  {
    conversation_id: "2",
    title: "Tailwind design example",
    message:
      "Using tailwind css and shadcn design for me this one: a title below is a message box.",
    updatedAt: "Updated 10 minutes ago",
  },
];

export default function ChatHistory() {
  return (
    <div className="max-w-3xl mx-auto p-4 space-y-4">
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input placeholder="Search for a chat..." className="pl-9" />
      </div>

      <div className="space-y-4">
        {chatItems.map((item) => (
          <ConversationCard item={item} />
        ))}
      </div>
    </div>
  );
}
