from data_processing.PDFLoader import PDFLoader
from data_processing.WebLoader import WebLoader
from config import KNOWLEDGE_PDF_PATH, KNOWLEDGE_WEB_URL_PATH


class KnowledgeBase:
    def __init__(self, pdf_paths: str = KNOWLEDGE_PDF_PATH, web_urls: str = KNOWLEDGE_WEB_URL_PATH):
        """
        Classe para gerenciar a base de conhecimento, carregando documentos de PDFs e da web.

        :param pdf_paths: Caminhos dos diretórios contendo PDFs, separados por vírgula.
        :param web_urls: URLs de sites para carregar documentos, separados por vírgula.
        """
        self.pdf_paths = pdf_paths
        self.web_urls = web_urls
        self.knowledge = []

    def load_knowledge(self):
        """
        Carrega documentos de PDFs e da web para a base de conhecimento.
        """
        pdf_loader = PDFLoader()
        web_loader = WebLoader()

        # Carregar documentos de PDFs
        self.knowledge.extend(pdf_loader.load_pdf_documents_from_directory_paths(self.pdf_paths))

        # Carregar documentos da web
        self.knowledge.extend(web_loader.load_documents_from_web_sites(self.web_urls))

    def get_knowledge(self):
        """
        Retorna a base de conhecimento carregada.

        :return: Lista de documentos carregados.
        """
        if not self.knowledge:
            self.load_knowledge()
        
        return self.knowledge