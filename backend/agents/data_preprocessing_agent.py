from autogen import ConversableAgent
from utils.dataset_utils import preprocess_python_code_dataset

def get_data_preprocessing_agent(llm_config):
    agent = ConversableAgent(
        "data_preprocessing_agent",
        system_message="You load and clean the jtatman/python-code-dataset-500k dataset.",
        llm_config=llm_config
    )
    agent.register_for_llm(
        name="preprocess_python_code_dataset",
        description="Loads and cleans the jtatman/python-code-dataset-500k dataset."
    )(preprocess_python_code_dataset)
    agent.register_for_execution(
        name="preprocess_python_code_dataset"
    )(preprocess_python_code_dataset)
    return agent
