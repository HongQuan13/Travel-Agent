import React, { useRef, useEffect } from "react";
import { Send } from "lucide-react";
import ReactMarkdown from "react-markdown";
import { ClimbingBoxLoader, PacmanLoader } from "react-spinners";

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
  conversationId,
}: MessageContainerProps) {
  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const {
    loading,
    messages,
    inputValue,
    setInputValue,
    retrieveChatContent,
    handleSendMessage,
  } = useMessage(conversationId);

  useEffect(() => {
    if (conversationId) retrieveChatContent();
  }, [conversationId]);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  const handleFinalizeMobile = () => {
    setFinalItinerary(true);
    setMobileView(true);
  };

  const handleFinalize = () => {
    setFinalItinerary(!finalItineraryView);
  };

  const scrollAreaRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="flex flex-col h-full">
      <ScrollArea ref={scrollAreaRef} className="flex-grow p-6 relative">
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
                  <ReactMarkdown>
                    {message.content.replace(/\n/gi, "\n &nbsp;")}
                  </ReactMarkdown>
                </div>
              )}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
        {loading && (
          <PacmanLoader
            size={10}
            style={{
              position: "absolute",
              bottom: "20px",
              left: "30px",
            }}
          />
        )}
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
            onClick={handleFinalizeMobile}
            variant="secondary"
            className="lg:hidden"
          >
            Final Itinerary
          </Button>
          <Button
            onClick={handleFinalize}
            variant="secondary"
            className="hidden lg:block"
          >
            Final Itinerary
          </Button>
        </form>
      </div>
    </div>
  );
}

export default MessageContainer;
