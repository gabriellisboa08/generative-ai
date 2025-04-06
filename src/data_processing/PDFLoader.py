import os
import logging
from langchain.document_loaders import PyPDFLoader

class PDFLoader:
    def __init__(self, log_file: str = "PDFLoader.log"):
        """
        Classe para gerenciar o carregamento de documentos PDF de diretórios.

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

    def load_pdf_documents_from_directory_paths(self, directory_paths: str) -> list:

        document_list = []
        directory_paths = [directory_path.strip() for directory_path in directory_paths.split(',')]
        for directory_path in directory_paths:
            document_list.extend(self.load_documents_pdf_from_path(directory_path))
        return document_list

    def load_documents_pdf_from_path(self, directory_path: str) -> list:

        documents = []
        try:
            for filename in os.listdir(directory_path):
                if filename.endswith(".pdf"):
                    pdf_path = os.path.join(directory_path, filename)
                    loader = PyPDFLoader(pdf_path)
                    docs = loader.load()
                    documents.extend(docs)
                    self.logger.info(f"Carregado {len(docs)} documentos de {pdf_path}")
        except FileNotFoundError as e:
            self.logger.error(f"Arquivo ou diretório não encontrado: {directory_path}. Detalhes: {e}")
        except Exception as e:
            self.logger.error(f"Erro inesperado ao carregar PDFs de {directory_path}: {e}")
        return documents