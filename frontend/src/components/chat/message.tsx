import React, { useRef, useEffect } from "react";
import { Send } from "lucide-react";
import { Avatar, AvatarFallback } from "../ui/avatar";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { ScrollArea } from "../ui/scroll-area";
import { Message } from "@/interfaces/chat";
import axios from "axios";

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

  useEffect(() => {
    retrieveChatContent();
  }, []);

  const retrieveChatContent = async () => {
    try {
      //hardcode conversation_id = 1
      const response = await axios.get(
        `${import.meta.env.VITE_BACKEND_BASE_URL}/chat/retrieve-conversation/1`,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          withCredentials: true,
        }
      );

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
      const response = await axios.post(
        `${import.meta.env.VITE_BACKEND_BASE_URL}/chat/send-message`,
        {
          conversation_id: 1,
          user_id: 1,
          message_text: inputValue.trim(),
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );

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
                className={`mx-2 py-2 px-3 rounded-lg ${
                  message.sender === "user"
                    ? "bg-primary text-primary-foreground"
                    : "bg-muted"
                }`}
              >
                {message.message_text}
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
