import unittest
import os

from text_processing.text_processing import load_docs


REAL_FILE = "example_docs_for_backend_test/test docs/doc1.txt"
NONEXISTING_FILE = "example_docs_for_backend_test/test docs/doc99.txt"


class TestLoadDocs(unittest.TestCase):
    
    def test_loading_real_file(self):
        file_name = REAL_FILE
        number_of_lines = 46
        doc = load_docs([file_name])[0]
        self.assertEqual(len(doc.sentences), number_of_lines)
        
    def test_not_loading_nonexisting_file(self):
        file_name = NONEXISTING_FILE
        self.assertEqual(len(load_docs([file_name])), 0)
        
        
if __name__ == '__main__':
    unittest.main()