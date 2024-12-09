import os
import logging
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from travel_agent.helpers.agent_constant import PROMPT_TEMPLATE
from travel_agent.helpers.agent_tools.agent_tools import google_search
from travel_agent.helpers.agent_tools.finalize_plan import finalize_plan_tool


logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class GPTAgentManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GPTAgentManager, cls).__new__(cls)
            cls._instance._agent_executor = None
        return cls._instance

    def __init__(self):
        logger.info("Starting initialize agent manager!")
        self._check_env()
        self._load_agent()

    def _load_agent(self):
        if self._agent_executor is None:
            llm = ChatOpenAI(
                model=self._model,
                temperature=0,
            )
            memory = MemorySaver()
            tools = [google_search, finalize_plan_tool]
            system_message = SystemMessage(content=PROMPT_TEMPLATE)

            self._agent_executor = create_react_agent(
                llm, tools, state_modifier=system_message, checkpointer=memory
            )

    def _check_env(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("GPT_MODEL")

        if openai_api_key is None or model is None:
            raise ValueError(f"Unable to access openai_api_key or model in .env file")

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
    newAgent = GPTAgentManager()

    response = newAgent.generate_response(
        "Human: Can you help me planning for 3 days trip vacation in Singapore?",
        "conversationId",
    )
    logger.info(f"AI Response: {response} ")
