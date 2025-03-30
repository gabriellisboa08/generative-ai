import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
KNOWLEDGE_WEB_URL_PATH = os.getenv("KNOWLEDGE_WEB_URL_PATH")
KNOWLEDGE_PDF_PATH = os.getenv("KNOWLEDGE_PDF_PATH")