from typing import List


class Document:
    def __init__(self, file_name, content):
        self._file_name = file_name
        self.sentences: List[str] = None
        self.processed_sentences: List[List[str]] = []
        
        self._load_sentences(content)

    def _load_sentences(self, content):
        self.sentences = content