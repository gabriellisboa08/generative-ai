class InputPreProcessor:
    def __init__(self, input_text: str):
        self.input_text = input_text

    def process(self):
        # Remove espaços em branco e converte para minúsculas
        self.input_text = self.input_text.strip().lower()

        # Transforma a entrada em um dicionário
        return {"input": self.input_text}