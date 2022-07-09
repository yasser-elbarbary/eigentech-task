from typing import List


class Document:
    def __init__(self, file_name):
        self._file_name = file_name
        self.sentences: List[str] = None
        self.normalized_sentences: List[str] = None

