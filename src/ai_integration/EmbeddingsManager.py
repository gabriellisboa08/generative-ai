# deixei os embeddings e o llm em arquivos separados para facilitar a manutenção e a organização do código
# bem como alteração de versões de embeddings e llm
from config import GOOGLE_API_KEY
from langchain_google_genai import GoogleGenerativeAIEmbeddings

class EmbeddingsManager:
    def __init__(self, api_key: str = GOOGLE_API_KEY, model: str = "models/embedding-001"):
        """
        Classe para gerenciar a criação de embeddings usando o Google Generative AI.
        
        :param api_key: Chave de API para autenticação no Google Generative AI.
        :param model: Modelo de embeddings a ser utilizado.
        """
        self.api_key = api_key
        self.model = model
        self.embeddings = None

    def initialize_embeddings(self):
        """
        Inicializa os embeddings com a API e o modelo especificados.
        """
        self.embeddings = GoogleGenerativeAIEmbeddings(api_key=self.api_key, model=self.model)

    def get_embeddings(self):
        """
        Retorna a instância de embeddings. Inicializa se ainda não estiver configurada.
        
        :return: Instância de GoogleGenerativeAIEmbeddings.
        """
        if not self.embeddings:
            self.initialize_embeddings()
        return self.embeddings