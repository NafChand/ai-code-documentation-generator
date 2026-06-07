from datasets import load_dataset
import ast

def preprocess_python_code_dataset():
    dataset = load_dataset("jtatman/python-code-dataset-500k", split="train")
    clean_data = []
    for item in dataset:
        code = item.get("code")
        doc = item.get("docstring")
        if code and doc:
            try:
                ast.parse(code)
                clean_data.append({"code": code, "docstring": doc})
            except SyntaxError:
                continue
    return f"Preprocessed {len(clean_data)} code-docstring pairs."
