import pytest
from unittest.mock import patch, MagicMock
from src.data_processing.WebLoader import WebLoader

class TestWebLoader:

    @patch('src.data_processing.WebLoader.WebBaseLoader')
    def test_load_documents_from_web_sites(self, mock_loader):
        mock_loader_instance = MagicMock()
        mock_loader_instance.load.return_value = ["doc1", "doc2"]
        mock_loader.return_value = mock_loader_instance

        loader = WebLoader()
        documents = loader.load_documents_from_web_sites("http://example.com,http://example2.com")

        assert len(documents) == 4
        mock_loader.assert_any_call("http://example.com")
        mock_loader.assert_any_call("http://example2.com")

    @patch('src.data_processing.WebLoader.logging.getLogger')
    @patch('src.data_processing.WebLoader.WebBaseLoader')
    def test_logger_error_called(self, mock_loader, mock_get_logger):
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        mock_loader.side_effect = Exception("Erro inesperado")

        loader = WebLoader()
        loader.load_documents_from_web_sites("http://example.com")

        mock_logger.error.assert_called_with("Erro ao carregar documentos de http://example.com. Detalhes: Erro inesperado")