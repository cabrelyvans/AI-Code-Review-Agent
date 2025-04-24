import yaml
from agent.llm_interface import LLMClient

def load_prompt_template(mode: str, template_path="prompts/templates.yaml") -> str:
    with open(template_path, "r", encoding="utf-8") as f:
        templates = yaml.safe_load(f)
    if mode not in templates:
        raise ValueError(f"Mode de prompt inconnu : {mode}")
    return templates[mode]["description"]

def load_code(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def analyze_code(file_path: str, mode: str = "strict", model: str = "mistral") -> str:
    prompt = load_prompt_template(mode)
    code = load_code(file_path)

    client = LLMClient(model=model)
    review = client.run(prompt, code)

    return review

def save_review(output: str, file_name="reviews/review_output.md"):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(output)
