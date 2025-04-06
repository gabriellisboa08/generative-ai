import unittest
from unittest.mock import patch, MagicMock
from src.database.KnowledgeRetriever import KnowledgeRetriever
from langchain.schema import Document


class TestKnowledgeRetriever(unittest.TestCase):
    @patch("src.database.KnowledgeRetriever.KnowledgeBase.get_knowledge")
    @patch("src.database.KnowledgeRetriever.FAISS.from_documents")
    @patch("src.database.KnowledgeRetriever.EmbeddingsManager.get_embeddings")
    def test_create_retriever(self, mock_get_embeddings, mock_faiss_from_documents, mock_get_knowledge):
        # Mockar os retornos
        mock_get_knowledge.return_value = [
            Document("teste1"),
            Document("teste2")
        ]
        mock_get_embeddings.return_value = "mocked_embeddings"
        mock_faiss_from_documents.return_value.as_retriever.return_value = "mocked_retriever"

        # Instanciar a classe KnowledgeRetriever
        retriever = KnowledgeRetriever(chunk_size=500, chunk_overlap=100)

        # Chamar o método create_retriever
        result = retriever.create_retriever()

        # Verificar se os métodos foram chamados corretamente
        mock_get_knowledge.assert_called_once()
        mock_get_embeddings.assert_called_once()
        mock_faiss_from_documents.assert_called_once_with(
            documents=[
                Document("teste1"),
                Document("teste2")
            ],
            embedding="mocked_embeddings"
        )

        # Verificar o resultado
        self.assertEqual(result, "mocked_retriever")

    @patch("src.database.KnowledgeRetriever.RecursiveCharacterTextSplitter.split_documents")
    def test_document_splitter(self, mock_split_documents):
        # Mockar o retorno do splitter
        mock_split_documents.return_value = [
            {"content": "Split Document 1"},
            {"content": "Split Document 2"}
        ]

        # Instanciar a classe KnowledgeRetriever
        retriever = KnowledgeRetriever(chunk_size=500, chunk_overlap=100)

        # Simular o carregamento de documentos
        documents = [{"content": "Document 1"}, {"content": "Document 2"}]
        result = retriever.documents_splitter.split_documents(documents)

        # Verificar se o splitter foi chamado corretamente
        mock_split_documents.assert_called_once_with(documents)

        # Verificar o resultado
        self.assertEqual(result, [
            {"content": "Split Document 1"},
            {"content": "Split Document 2"}
        ])


if __name__ == "__main__":
    unittest.main()