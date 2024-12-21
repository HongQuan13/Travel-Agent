class SuccessDetail:
    db_connection = "Database connection established"

    @staticmethod
    def new_user(user_id: int):
        return f"Create new user {user_id} successfully"

    @staticmethod
    def new_conversation(user_id: int):
        return f"Create new conversation for user {user_id} successfully"

    @staticmethod
    def all_conversation(user_id: int):
        return f"Query all conversations for user {user_id} successfully"

    @staticmethod
    def new_itinerary(id: int):
        return f"Create new itinerary {id} successfully"

    @staticmethod
    def new_message(conversation_id: int):
        return f"Send new message to conversation {conversation_id} successfully"

    @staticmethod
    def bot_reply_message(conversation_id: int):
        return f"Bot reply to user conversation {conversation_id} successfully"
