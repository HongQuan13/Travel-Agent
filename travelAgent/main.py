from dotenv import load_dotenv
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType

import os
import transformers
import torch

from ollamaAPI import OllamaLLM

load_dotenv()
ollamda_llm = OllamaLLM()

response = ollamda_llm.invoke(
    "Hi, how are you? May help me plan a trip to singapore in 2 days"
)
print(response)
