import React, { useRef, useEffect } from "react";
import { Send } from "lucide-react";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Message } from "@/interfaces/interface";
import { axiosClient } from "@/lib/axios";

interface MessageContainerProps {
  finalPlanView: Boolean;
  setFinalPlan: React.Dispatch<React.SetStateAction<boolean>>;
  setMobileView: React.Dispatch<React.SetStateAction<boolean>>;
}

function MessageContainer({
  finalPlanView,
  setFinalPlan,
  setMobileView,
}: MessageContainerProps) {
  const [inputValue, setInputValue] = React.useState("");
  const [messages, setMessages] = React.useState<Message[]>([]);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    retrieveChatContent();
  }, []);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  const retrieveChatContent = async () => {
    try {
      //hardcode conversation_id = 1
      const response = await axiosClient.get("chat/retrieve-conversation/1");

      const allMessages = response.data.all_messages;
      setMessages(allMessages);
    } catch (error: any) {
      console.error("Error:", error);
    }
  };

  const scrollAreaRef = useRef<HTMLDivElement>(null);

  const handleSendMessage = async () => {
    if (inputValue.trim()) {
      const newMessage: Message = {
        message_text: inputValue,
        sender: "user",
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
      setInputValue("");
    }

    try {
      const response = await axiosClient.post("chat/send-message", {
        conversation_id: 1,
        user_id: 1,
        message_text: inputValue.trim(),
      });

      const replyMessage: Message = {
        message_text: response.data.bot_response,
        sender: "bot",
      };
      setMessages((prevMessages) => [...prevMessages, replyMessage]);
    } catch (error: any) {
      console.error("Error:", error.message);
    }
  };

  const handleFinalize = () => {
    setFinalPlan(true);
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
        {messages.map((message: any) => (
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
                {message.message_text}
              </div>
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
            onChange={(e: any) => setInputValue(e.target.value)}
            className="flex-grow"
          />
          <Button type="submit" size="icon" onClick={handleSendMessage}>
            <Send className="h-4 w-4" />
            <span className="sr-only">Send message</span>
          </Button>
          <Button
            onClick={handleFinalize}
            variant="secondary"
            className={finalPlanView ? "lg:hidden" : ""}
          >
            Finalize Plan
          </Button>
        </form>
      </div>
    </div>
  );
}

export default MessageContainer;
