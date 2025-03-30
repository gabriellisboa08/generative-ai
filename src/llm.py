# deixei os embeddings e o llm em arquivos separados para facilitar a manutenção e a organização do código
# bem como alteração de versões de embeddings e llm
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(api_key=GOOGLE_API_KEY, model="gemini-2.0-flash")