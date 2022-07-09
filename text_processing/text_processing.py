from tkinter import EXCEPTION
from typing import List
from document.document import Document


def load_docs(files: List[str]):
    docs = []
    for file_name in files:
            try:
                with open(file_name, 'r') as f:
                    # TODO: tokenizing senctences is better than rading lines in the future.
                    doc = Document(file_name=file_name, content=f.readlines())
                    docs.append(doc)
            except Exception as e:
                print(f"Could not load file: {file_name}.")
    return docs

def normalise_text():
    pass


def tokenize_to_sentences(Document):
    pass


def tokenize_to_words(sentence):
    pass


def remove_stopwords(sentence):
    pass


def lemmatize(sentence, pos):
    pass
