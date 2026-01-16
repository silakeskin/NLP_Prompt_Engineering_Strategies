from openai import OpenAI

class PromptRunner:
    def __init__(self, api_key, model_name="gpt-4.1-mini"):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def run(self, prompt, question):
        full_prompt = prompt.strip() + "\nQuestion: " + question

        response = self.client.responses.create(
            model=self.model_name,
            input=full_prompt,
        )

        return response.output_text.strip()
