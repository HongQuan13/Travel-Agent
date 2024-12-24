import os
import logging
import sys
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_constant import PROMPT_TEMPLATE
from travel_agent.helpers.agent_tools.browsing_internet.browser_internet_tool import (
    browser_internet_tool,
)
from travel_agent.helpers.agent_tools.google_map.get_distance_tool import (
    get_distance_tool,
)
from travel_agent.helpers.agent_tools.google_map.get_place_detail_tool import (
    get_detail_place_tool,
)
from travel_agent.helpers.agent_tools.text_search_tool import (
    google_search,
    duckduckgo_search,
)
from travel_agent.helpers.agent_tools.image_search.image_search_tool import (
    image_search_tool,
)
from travel_agent.helpers.agent_tools.final_itinerary.finalize_itinerary_tool import (
    finalize_itinerary_tool,
)
from travel_agent.helpers.agent_tools.final_itinerary.generate_place_tool import (
    generate_place_tool,
)
from travel_agent.helpers.agent_tools.final_itinerary.generate_itinerary_notice_tool import (
    notice_generate_itinerary_successful_tool,
)
from travel_agent.helpers.agent_tools.final_itinerary.generate_subheader_tool import (
    generate_subheaders_tool,
)


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
        logger.info(InfoDetail.class_initialize("GPTAgentManager"))
        self._check_env()
        self._load_agent()

    def _load_agent(self):
        if self._agent_executor is None:
            llm = ChatOpenAI(
                model=self._model,
                temperature=0,
            )
            memory = MemorySaver()
            tools = [
                # google_search,
                # duckduckgo_search,
                image_search_tool,
                finalize_itinerary_tool,
                generate_place_tool,
                notice_generate_itinerary_successful_tool,
                generate_subheaders_tool,
                get_distance_tool,
                get_detail_place_tool,
                browser_internet_tool,
            ]
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

    def generate_conversation_title(self, user_input: str) -> str:
        config = {"configurable": {"thread_id": "0"}}
        title_prompt = PromptTemplate(
            input_variables=["user_input"],
            template="Generate a concise and relevant title (less than 10 words) for this trip plan conversation: {user_input}",
        )

        title = title_prompt.format(user_input=user_input)

        response = self._agent_executor.invoke(
            {"messages": [HumanMessage(content=title)]}, config
        )
        return response["messages"][-1].content


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)
    load_dotenv()
    newAgent = GPTAgentManager()

    response = newAgent.generate_conversation_title(
        " Can you help me planning for 3 days trip vacation in Singapore?",
    )
    logger.info(f"AI Response: {response} ")
