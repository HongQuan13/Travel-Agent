import { fetchData, postData } from "@/services/api";

export const fetchConversation = async (conversation_id: string) => {
  const data = await fetchData(`chat/retrieve-conversation/${conversation_id}`);

  return data.all_messages;
};

export const sendMessage = async (
  conversation_id: string,
  inputValue: string
) => {
  const data = {
    conversation_id: conversation_id,
    content: inputValue.trim(),
  };
  const response = await postData("chat/send-message", data);

  return response.bot_response;
};

export const fetchConversationHistory = async () => {
  const response = await fetchData("chat/conversation-history");

  return response.conversations;
};

export const createConversation = async (first_message: string) => {
  const data = {
    first_message: first_message,
  };
  return await postData("chat/create-conversation", data);
};
