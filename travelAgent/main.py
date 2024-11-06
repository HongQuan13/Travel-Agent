from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from rich import print as rprint
from rich.pretty import Pretty
import os

from agentTools import google_search

load_dotenv()

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_API"),
    model=os.getenv("OLLAMA_MODEL"),
    temperature=0,
)

memory = MemorySaver()
tools = [google_search]
system_message = SystemMessage(
    content="""You are a helpful assistant. Only use the provided tools when necessary for specific tasks.
                For general conversation or simple responses, respond directly without using any tools.
                Available tools:
                - Use google_search for real-time events or recent information.
                
                Respond the conversation below and use tools only when appropriate:
                {messages}
            """
)

agent_executor = create_react_agent(
    llm, tools, state_modifier=system_message, checkpointer=memory
)

config = {"configurable": {"thread_id": "abc123"}}


def get_agent_response(user_input: str) -> str:
    response = agent_executor.invoke(
        {"messages": [HumanMessage(content=user_input)]}, config
    )
    return response["messages"][-1].content


if __name__ == "__main__":
    print("Start chatting with the agent! Type 'exit' to stop.")
    while True:
        print("-------------------")
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Ending the conversation. Goodbye!")
            break

        response = get_agent_response(user_input)
        rprint("travelAgent: ", Pretty(response))
