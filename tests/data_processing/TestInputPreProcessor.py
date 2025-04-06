import unittest
from src.data_processing.InputPreProcessor import InputPreProcessor

class TestInputPreProcessor(unittest.TestCase):
    def test_process_removes_whitespace_and_lowercases(self):
        processor = InputPreProcessor("  Exemplo de Entrada  ")
        result = processor.process()
        self.assertEqual(result, {"input": "exemplo de entrada"})

    def test_process_empty_string(self):
        processor = InputPreProcessor("  ")
        result = processor.process()
        self.assertEqual(result, {"input": ""})

    def test_process_mixed_case(self):
        processor = InputPreProcessor("TeStE De MiXed CaSe")
        result = processor.process()
        self.assertEqual(result, {"input": "teste de mixed case"})

    def test_process_no_whitespace(self):
        processor = InputPreProcessor("semEspacos")
        result = processor.process()
        self.assertEqual(result, {"input": "semespacos"})

if __name__ == "__main__":
    unittest.main()