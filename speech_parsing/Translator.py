import openai

class Translator():
    def __init__(self, language: str):
        self.language = language

    def get_prompt(self, text: str):
        return f'Translate this into {self.language} : \n\n{text}\n\n'
    
    def translate(self, text: str) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.get_prompt(text),
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response["choices"][0]["text"].replace("\n", "")

