import React, { useRef, useEffect } from "react";
import { Send } from "lucide-react";

import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { PlaceCardHeader } from "@/features/itinerary";
import { useMessage } from "../hooks/useMessage";
import { Message, MessageContainerProps } from "../interfaces";

function MessageContainer({
  finalItineraryView,
  setFinalItinerary,
  setMobileView,
  handleClickItinerary,
  conversation_id,
}: MessageContainerProps) {
  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const {
    messages,
    inputValue,
    setInputValue,
    retrieveChatContent,
    handleSendMessage,
  } = useMessage(conversation_id);

  useEffect(() => {
    if (conversation_id) retrieveChatContent();
  }, [conversation_id]);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  const handleFinalize = () => {
    setFinalItinerary(true);
    setMobileView(true);
  };

  const scrollAreaRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="flex flex-col h-full">
      <ScrollArea ref={scrollAreaRef} className="flex-grow p-6">
        {messages.map((message: Message) => (
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
              {message.category === "itinerary" ? (
                <PlaceCardHeader
                  id={message.content}
                  title={message.content}
                  handleClick={handleClickItinerary}
                />
              ) : (
                <div
                  className={`mx-2 py-2 px-3 rounded-lg whitespace-pre-line break-words ${
                    message.sender === "user"
                      ? "bg-primary text-primary-foreground"
                      : "bg-muted"
                  }`}
                  style={{
                    maxWidth: "75%",
                    wordWrap: "break-word",
                    wordBreak: "break-word",
                  }}
                >
                  {message.content}
                </div>
              )}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </ScrollArea>
      <div className="p-6 border-t bg-background">
        <form
          onSubmit={(e) => {
            e.preventDefault();
          }}
          className="flex space-x-2"
        >
          <Input
            type="text"
            placeholder="Type your message..."
            value={inputValue}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
              setInputValue(e.target.value)
            }
            className="flex-grow"
          />
          <Button type="submit" size="icon" onClick={handleSendMessage}>
            <Send className="h-4 w-4" />
            <span className="sr-only">Send message</span>
          </Button>
          <Button
            onClick={handleFinalize}
            variant="secondary"
            className={finalItineraryView ? "lg:hidden" : ""}
          >
            Finalize Itinerary
          </Button>
        </form>
      </div>
    </div>
  );
}

export default MessageContainer;
