from typing import List


class Document:
    def __init__(self, file_name, content):
        self._file_name = file_name
        self.sentences: List[str] = None
        self.processed_sentences: List[str] = []
        self.sentences_tokenized: List[List[str]] = []
        
        self.tfidf_matrix = None
        self.tfidf_df = None
        
        self._load_sentences(content)

    def _load_sentences(self, content):
        self.sentences = content