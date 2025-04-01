import logging
from langchain.document_loaders import WebBaseLoader

class WebLoader:
    def __init__(self, log_file: str = "WebLoader.log"):
        """
        Classe para gerenciar o carregamento de documentos da web.

        :param log_file: Nome do arquivo de log para registrar as operações.
        """
        # Configurar o logger
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_documents_from_web_sites(self, endpoints: str) -> list:
        """
        Carrega documentos de uma lista de URLs.

        :param endpoints: URLs separadas por vírgula.
        :return: Lista de documentos carregados.
        """
        knowledge = []
        endpoints = [endpoint.strip() for endpoint in endpoints.split(',')]
        for endpoint in endpoints:
            knowledge.extend(self._load_documents_web_from_url(endpoint))
        return knowledge

    def _load_documents_web_from_url(self, url: str) -> list:
        """
        Carrega documentos de uma única URL.

        :param url: URL do site.
        :return: Lista de documentos carregados.
        """
        documents = []
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            documents.extend(docs)
            self.logger.info(f"Carregado {len(docs)} documentos de {url}")
        except Exception as e:
            self.logger.error(f"Erro ao carregar documentos de {url}. Detalhes: {e}")
        return documents