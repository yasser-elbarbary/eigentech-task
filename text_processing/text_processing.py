from string import punctuation
from typing import List
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

import nltk
nltk.download('popular')


from document.document import Document


def load_docs(files: List[str]):
    docs = []
    for file_name in files:
            try:
                with open(file_name, 'r', encoding="utf8") as f:
                    content = sent_tokenize(f.read())
                    doc = Document(file_name=file_name, content=content)
                    docs.append(doc)
            except FileNotFoundError as e:
                print(f"Could not load file: {file_name}.")
    return docs
 
def normalise_text(sentence):
    punctuations = set(punctuation)
    tokens = word_tokenize(sentence)
    tokens = [word.lower() for word in tokens if word not in punctuations and word.isalpha()]
    return tokens



def remove_stopwords(tokens):
    return [word for word in tokens if word not in set(stopwords.words("english")) ]


def lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    pos_tagged  = pos_tag(tokens)
    wordnet_tagged = list(map(lambda x: (x[0], _nltk_pos_tagger(x[1])), pos_tagged))

    return [
        lemmatizer.lemmatize(token, pos=tag) 
        if tag
        else token
        for token, tag in wordnet_tagged
    ]

def _nltk_pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

