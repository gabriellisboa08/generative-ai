# deixei os embeddings e o llm em arquivos separados para facilitar a manutenção e a organização do código
# bem como alteração de versões de embeddings e llm
from config import GOOGLE_API_KEY
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(api_key=GOOGLE_API_KEY,model="models/embedding-001")