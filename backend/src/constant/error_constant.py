from typing import Any


class ErrorDetail:
    exist_user = "User account already exist"
    non_exist_user = "User account not exist"
    non_exist_conversation = "Conversation not exist"
    non_exist_itinerary = "Itinerary not exist"

    @staticmethod
    def unknown(func_name: str, error: Any):
        return f"Unknown error at function {func_name}: {error}"
