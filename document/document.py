from typing import List


class Document:
    def __init__(self, file_name, content):
        self._file_name = file_name
        self.sentences: List[str] = None
        self.normalized_sentences: List[str] = None
        
        self._load_sentences(content)

    def _load_sentences(self, content):
        self.sentences = content