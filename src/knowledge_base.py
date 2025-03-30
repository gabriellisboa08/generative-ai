from pdf_loader import load_pdf_documents_from_directory_paths
from web_loader import load_documents_from_web_sites
from config import KNOWLEDGE_PDF_PATH, KNOWLEDGE_WEB_URL_PATH

# Base de dados simulada. Carregar documentos de PDFs de diretórios do sistema e dados da web.
knowledge = []
knowledge.extend(load_pdf_documents_from_directory_paths(KNOWLEDGE_PDF_PATH))
knowledge.extend(load_documents_from_web_sites(KNOWLEDGE_WEB_URL_PATH))