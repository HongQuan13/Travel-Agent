import os
import logging
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent, chat_agent_executor
from langchain_ollama import ChatOllama

from travel_agent.agent_constant import PROMPT_TEMPLATE
from travel_agent.agent_tools import google_search


class AgentManager:
    def __init__(self):
        logger.info("Starting initialize agent manager!")
        self._check_env()
        self.agent_executor = self._load_agent()

    def _load_agent(self) -> chat_agent_executor:
        llm = ChatOllama(
            base_url=self.ollama_api,
            model=self.model,
            temperature=0,
        )
        memory = MemorySaver()
        tools = [google_search]
        system_message = SystemMessage(content=PROMPT_TEMPLATE)

        agent_executor = create_react_agent(
            llm, tools, state_modifier=system_message, checkpointer=memory
        )
        return agent_executor

    def _check_env(self):
        ollama_api = os.getenv("OLLAMA_API")
        model = os.getenv("OLLAMA_MODEL")

        if ollama_api is None or model is None:
            raise ValueError(f"Unable to access ollama_api or model in .env file")

        self.ollama_api = ollama_api.lower().strip()
        self.model = model.lower().strip()

    def generate_response(self, user_input: str, conversation_id: str) -> str:
        config = {"configurable": {"thread_id": conversation_id}}

        response = self.agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]}, config
        )
        return response["messages"][-1].content


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    load_dotenv()
    newAgent = AgentManager()

    response = newAgent.generate_response(
        "Human: Can you help me planning for 3 days trip vacation in Singapore?",
        "conversationId",
    )
    logger.info(f"AI Response: {response} ")
