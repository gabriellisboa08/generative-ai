# deixei os embeddings e o llm em arquivos separados para facilitar a manutenção e a organização do código
# bem como alteração de versões de embeddings e llm
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

class LLMManager:
    def __init__(self, api_key: str = GOOGLE_API_KEY, model: str = "gemini-2.0-flash"):
        """
        Classe para gerenciar a criação do modelo de linguagem.

        :param api_key: Chave de API para autenticação no Google Generative AI.
        :param model: Modelo de linguagem a ser utilizado.
        """
        self.api_key = api_key
        self.model = model
        self.llm = None

    def initialize_llm(self):
        """
        Inicializa o modelo de linguagem com a API e o modelo especificados.
        """
        self.llm = ChatGoogleGenerativeAI(api_key=self.api_key, model=self.model)

    def get_llm(self):
        """
        Retorna a instância do modelo de linguagem. Inicializa se ainda não estiver configurada.

        :return: Instância de ChatGoogleGenerativeAI.
        """
        if not self.llm:
            self.initialize_llm()
        return self.llm