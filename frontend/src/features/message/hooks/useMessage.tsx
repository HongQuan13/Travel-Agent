import { useEffect, useState } from "react";
import { fetchConversation, sendMessage } from "../services";
import { useWebSocket } from "@/hooks/useWebSocket";
import { Message } from "../interfaces";

export const useMessage = (conversationId: string) => {
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const { message } = useWebSocket();

  useEffect(() => {
    handleReceivedItinerary();
  }, [message]);

  const handleReceivedItinerary = () => {
    if (message == "") return;

    const content = JSON.parse(message);
    const newMessage: Message = {
      content: content.itineraryId,
      sender: "bot",
      category: "itinerary",
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
  };

  const retrieveChatContent = async () => {
    try {
      const allMessages = await fetchConversation(conversationId);
      setMessages(allMessages);
    } catch (error: any) {
      console.error("Error:", error);
    }
  };

  const handleSendMessage = async () => {
    if (inputValue == "") return;
    if (inputValue.trim()) {
      const newMessage: Message = {
        content: inputValue,
        sender: "user",
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
      setInputValue("");
    }

    try {
      const reply = await sendMessage(conversationId, inputValue);
      const replyMessage: Message = {
        content: reply,
        sender: "bot",
      };
      setMessages((prevMessages) => [...prevMessages, replyMessage]);
    } catch (error: any) {
      console.error("Error:", error.message);
    }
  };
  return {
    messages,
    inputValue,
    setInputValue,
    handleReceivedItinerary,
    retrieveChatContent,
    handleSendMessage,
  };
};
