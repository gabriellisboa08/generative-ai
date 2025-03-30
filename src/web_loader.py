import logging
from langchain.document_loaders import WebBaseLoader

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

def load_documents_from_web_sites(endpoints):
    knowledge = []
    endpoints = [endpoint.strip() for endpoint in endpoints.split(',')]
    for endpoint in endpoints:
        knowledge.extend(load_documents_web_from_url(endpoint))
    return knowledge


def load_documents_web_from_url(url):
    documents = []
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        documents.extend(docs)
        logger.info(f"Carregado {len(docs)} documentos de {url}")
    except Exception as e:
        logger.error(f"Erro ao carregar documentos de {url}. Detalhes: {e}")
    return documents

