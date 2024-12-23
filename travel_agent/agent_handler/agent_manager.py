import os
import logging
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_constant import PROMPT_TEMPLATE
from travel_agent.helpers.agent_tools.text_search_tool import google_search

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class AgentManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentManager, cls).__new__(cls)
            cls._instance._agent_executor = None
        return cls._instance

    def __init__(self):
        logger.info(InfoDetail.class_initialize("AgentManager"))
        self._check_env()
        self._load_agent()

    def _load_agent(self):
        if self._agent_executor is None:
            llm = ChatOllama(
                base_url=self._ollama_api,
                model=self._model,
                temperature=0,
            )
            memory = MemorySaver()
            tools = [google_search]
            system_message = SystemMessage(content=PROMPT_TEMPLATE)

            self._agent_executor = create_react_agent(
                llm, tools, state_modifier=system_message, checkpointer=memory
            )

    def _check_env(self):
        ollama_api = os.getenv("OLLAMA_API")
        model = os.getenv("OLLAMA_MODEL")

        if ollama_api is None or model is None:
            raise ValueError(f"Unable to access ollama_api or model in .env file")

        self._ollama_api = ollama_api.lower().strip()
        self._model = model.lower().strip()

    def generate_response(self, user_input: str, conversation_id: str) -> str:
        config = {"configurable": {"thread_id": conversation_id}}

        response = self._agent_executor.invoke(
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
