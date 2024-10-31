from typing import Any, List, Optional
from dotenv import load_dotenv
import requests
import os

from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun

load_dotenv()


class OllamaLLM(LLM):

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        model = os.getenv("OLLAMA_MODEL")
        url = os.getenv("OLLAMA_API")
        payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            content = (
                response.json()
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "No response from model.")
            )

            return content

        except requests.exceptions.RequestException as e:
            print(f"Error querying Ollama model: {e}")
            return ""

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "custom"

    @property
    def _identifying_params(self) -> dict:
        return {}
