import pytest
from unittest.mock import patch, MagicMock
from src.data_processing.PDFLoader import PDFLoader
from PyPDF2 import PdfWriter

class TestPDFLoader:
    @pytest.fixture
    def mock_directory(self, tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        for i in range(3):
            pdf_file = d / f"file{i}.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=72, height=72)
            with open(pdf_file, "wb") as f:
                writer.write(f)
        return str(d)

    @patch('langchain.document_loaders.PyPDFLoader')
    def test_load_pdf_documents_from_directory_paths(self, mock_loader, mock_directory):

        loader = PDFLoader()

        documents = loader.load_pdf_documents_from_directory_paths(mock_directory)

        assert len(documents) == 3

    @patch('src.data_processing.PDFLoader.logging.getLogger')
    def test_logger_error_called(self, mock_get_logger):

        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        loader = PDFLoader()

        loader.load_documents_pdf_from_path("non_existent_directory")

        mock_logger.error.assert_called_with("Arquivo ou diretório não encontrado: non_existent_directory. Detalhes: [Errno 2] No such file or directory: 'non_existent_directory'")


    @patch('src.data_processing.PDFLoader.logging.getLogger')
    @patch('os.listdir', side_effect=Exception("Erro inesperado"))
    def test_logger_error_called_with_exception(self, mock_listdir, mock_get_logger):
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        loader = PDFLoader()

        loader.load_documents_pdf_from_path("some_directory")

        mock_logger.error.assert_called_with("Erro inesperado ao carregar PDFs de some_directory: Erro inesperado")