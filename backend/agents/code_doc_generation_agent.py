from autogen import ConversableAgent

def get_code_doc_generation_agent(llm_config):
    agent = ConversableAgent(
        "code_doc_generation_agent",
        system_message=(
            "You are an AI-powered Python code documentation generator. "
            "Given Python code, generate a detailed, context-aware docstring. "
            "Only return the docstring."
        ),
        llm_config=llm_config
    )
    return agent
