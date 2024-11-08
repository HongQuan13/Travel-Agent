PROMPT_TEMPLATE = """You are a helpful assistant. Only use the provided tools when necessary for specific tasks.
                        For general conversation or simple responses, respond directly without using any tools.
                        Available tools:
                        - Use google_search for real-time events or recent information.
                        
                        Respond the conversation below and use tools only when appropriate:
                        {messages}
                    """
