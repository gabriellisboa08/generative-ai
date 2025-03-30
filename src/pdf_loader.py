import os
import logging
from langchain.document_loaders import PyPDFLoader

# Configurar o logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("knowledge_loader.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def load_pdf_documents_from_directory_paths(directory_paths : list):
    document_list = []
    directory_paths = [directory_path.strip() for directory_path in directory_paths.split(',')]
    for directory_path in directory_paths:
        document_list.extend(load_documents_pdf_from_path(directory_path))
    return document_list


def load_documents_pdf_from_path(directory_path):
    documents = []
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory_path, filename)
                loader = PyPDFLoader(pdf_path)
                docs = loader.load()
                documents.extend(docs)
                logger.info(f"Carregado {len(docs)} documentos de {pdf_path}")
    except FileNotFoundError as e:
        logger.error(f"Arquivo ou diretório não encontrado: {directory_path}. Detalhes: {e}")
    except Exception as e:
        logger.error(f"Erro inesperado ao carregar PDFs de {directory_path}: {e}")
    return documents