from src.database.KnowledgeBase import KnowledgeBase
from langchain_community.vectorstores import FAISS
from src.ai_integration.EmbeddingsManager import EmbeddingsManager
from langchain_text_splitters import RecursiveCharacterTextSplitter


class KnowledgeRetriever:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200, separators: list = None):
        """
        Classe para gerenciar a criação de um retriever a partir de documentos.

        :param chunk_size: Tamanho máximo de cada pedaço.
        :param chunk_overlap: Sobreposição entre os pedaços.
        :param separators: Delimitadores para divisão dos documentos.
        """
        if separators is None:
            separators = ["\n\n", "\n", ".", " "]
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators
        self.documents_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators
        )

    def create_retriever(self):
        """
        Cria um retriever a partir dos documentos carregados.

        :return: Um retriever configurado.
        """
        # Dividir os documentos usando o splitter configurado
        document_splitted = self.documents_splitter.split_documents(documents=KnowledgeBase().get_knowledge())

        # Criar o vetor FAISS a partir dos documentos divididos
        vector = FAISS.from_documents(documents=document_splitted, embedding=EmbeddingsManager().get_embeddings())

        # Retornar o retriever
        return vector.as_retriever()