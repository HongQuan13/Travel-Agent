import React, { useRef, useEffect } from "react";
import { Send } from "lucide-react";
import { Avatar, AvatarFallback } from "../ui/avatar";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { ScrollArea } from "../ui/scroll-area";
import { Message } from "@/interfaces/chat";

interface MessageContainerProps {
  finalPlanView: Boolean;
  setIsFinalized: React.Dispatch<React.SetStateAction<boolean>>;
  setMobileView: React.Dispatch<React.SetStateAction<boolean>>;
}

function MessageContainer({
  finalPlanView,
  setIsFinalized,
  setMobileView,
}: MessageContainerProps) {
  const [inputValue, setInputValue] = React.useState("");
  const [messages, setMessages] = React.useState<Message[]>([
    {
      id: "1",
      content: "Hello! Let's plan your Seattle Instagram getaway!",
      sender: "bot",
    },
    { id: "2", content: "I'd love to visit the Space Needle!", sender: "user" },
    {
      id: "3",
      content:
        "Great choice! The Space Needle offers amazing photo opportunities.",
      sender: "bot",
    },
  ]);
  const scrollAreaRef = useRef<HTMLDivElement>(null);

  const handleSendMessage = () => {
    if (inputValue.trim()) {
      const newMessage: Message = {
        id: Date.now().toString(),
        content: inputValue,
        sender: "user",
      };
      setMessages([...messages, newMessage]);
      setInputValue("");
    }
  };

  const handleFinalize = () => {
    setIsFinalized(true);
    setMobileView(true);
  };

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="flex flex-col h-full">
      <ScrollArea ref={scrollAreaRef} className="flex-grow p-6">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${
              message.sender === "user" ? "justify-end" : "justify-start"
            } mb-4`}
          >
            <div
              className={`flex items-end ${
                message.sender === "user" ? "flex-row-reverse" : "flex-row"
              }`}
            >
              <Avatar className="w-8 h-8">
                <AvatarFallback>
                  {message.sender === "user" ? "U" : "B"}
                </AvatarFallback>
              </Avatar>
              <div
                className={`mx-2 py-2 px-3 rounded-lg ${
                  message.sender === "user"
                    ? "bg-primary text-primary-foreground"
                    : "bg-muted"
                }`}
              >
                {message.content}
              </div>
            </div>
          </div>
        ))}
      </ScrollArea>
      <div className="p-6 border-t bg-background">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSendMessage();
          }}
          className="flex space-x-2"
        >
          <Input
            type="text"
            placeholder="Type your message..."
            value={inputValue}
            onChange={(e: any) => setInputValue(e.target.value)}
            className="flex-grow"
          />
          <Button type="submit" size="icon">
            <Send className="h-4 w-4" />
            <span className="sr-only">Send message</span>
          </Button>
          {!finalPlanView && (
            <Button onClick={handleFinalize} variant="secondary">
              Finalize Plan
            </Button>
          )}
        </form>
      </div>
    </div>
  );
}

export default MessageContainer;
