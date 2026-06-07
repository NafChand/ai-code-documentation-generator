import os
import dotenv
from autogen import ConversableAgent
from agents.data_preprocessing_agent import get_data_preprocessing_agent
from agents.code_doc_generation_agent import get_code_doc_generation_agent
from agents.quality_check_agent import get_quality_check_agent

dotenv.load_dotenv()

def run_pipeline(code_snippet):
    llm_config = {
        "config_list": [
            {"model": "gpt-4o-mini", "api_key": os.environ.get("OPENAI_API_KEY")}
        ]
    }

    user_proxy = ConversableAgent(
        "user_proxy",
        llm_config=False,
        system_message="You are the user."
    )

    # Step 1: Preprocess dataset
    preprocess_result = user_proxy.initiate_chat(
        recipient=get_data_preprocessing_agent(llm_config),
        message="Please preprocess the jtatman/python-code-dataset-500k dataset.",
        max_turns=2,
        summary_method="last_msg"
    )

    # Step 2: Generate docstring
    docstring_result = get_code_doc_generation_agent(llm_config).initiate_chat(
        recipient=get_code_doc_generation_agent(llm_config),
        message=f"Generate a detailed docstring for the following Python code:\n{code_snippet}",
        max_turns=2,
        summary_method="last_msg"
    )
    docstring = docstring_result.summary

    # Step 3: Quality check
    quality_result = get_quality_check_agent(llm_config).initiate_chat(
        recipient=get_quality_check_agent(llm_config),
        message=f"Code:\n{code_snippet}\nDocstring:\n{docstring}",
        max_turns=2,
        summary_method="last_msg"
    )

    # Step 4: Return output for API
    if "good" in quality_result.summary.lower():
        return { "doc": docstring }
    else:
        return { "suggestions": quality_result.summary }

# Optional: run from terminal
if __name__ == "__main__":
    import sys
    assert len(sys.argv) > 1, "Please provide a Python code snippet as input."
    code_snippet = sys.argv[1]
    result = run_pipeline(code_snippet)
    print(result)
