from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
import os

from agentTools import google_search

load_dotenv()

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_API"),
    model=os.getenv("OLLAMA_MODEL"),
    temperature=0,
)

memory = MemorySaver()
# tools = [google_search]
tools = []
agent_executor = create_react_agent(llm, tools, checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}


def get_agent_response(user_input: str) -> str:
    response = agent_executor.invoke(
        {"messages": [HumanMessage(content=user_input)]}, config
    )

    return response["messages"][-1].pretty_print()


if __name__ == "__main__":
    print("Start chatting with the agent! Type 'exit' to stop.")
    while True:
        print("-------------------")
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Ending the conversation. Goodbye!")
            break

        get_agent_response(user_input)
