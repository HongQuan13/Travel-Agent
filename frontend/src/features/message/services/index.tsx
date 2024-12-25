import { fetchData, postData } from "@/services/api";

export const fetchConversation = async (conversationId: string) => {
  const data = await fetchData(`chat/retrieve-conversation/${conversationId}`);

  return data.allMessages;
};

export const sendMessage = async (
  conversationId: string,
  inputValue: string
) => {
  const data = {
    conversationId: conversationId,
    content: inputValue.trim(),
  };
  const response = await postData("chat/send-message", data);

  return response.botResponse;
};

export const fetchConversationHistory = async () => {
  const response = await fetchData("chat/conversation-history");
  return response.conversations;
};

export const createConversation = async (firstMessage: string) => {
  const data = {
    firstMessage: firstMessage,
  };
  return await postData("chat/create-conversation", data);
};
