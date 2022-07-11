from collections import Counter, defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from nltk.util import ngrams


def get_tfidf(sentences, ngram_range=(1,5)):
    tfidf = TfidfVectorizer(min_df=2, ngram_range=ngram_range)
    features = tfidf.fit_transform(sentences)
    return {
        'tfidf_df': pd.DataFrame(
            features.todense(),
            columns=tfidf.get_feature_names_out()
        ),
        'tfidf_matrix':features}
    
def most_common_terms(sentences_tokenized,sentences, doc_id, min_gram=1, max_gram=5):
    ngram_counter = defaultdict(dict)
    for sentence_idx, tokens in enumerate(sentences_tokenized):
        # create ngrams from, to
        for n in range(min_gram,max_gram+1):
            n_grams = ngrams(tokens,n)
            for gram in n_grams:
                if gram in ngram_counter:
                    ngram_counter[gram]['count'] += 1
                    ngram_counter[gram]['sentences'].add(sentences[sentence_idx])
                    ngram_counter[gram]['sentence_index'].add((doc_id,sentence_idx)) 
                else:
                    ngram_counter[gram]['count'] = 1
                    ngram_counter[gram]['sentences'] = {sentences[sentence_idx]}
                    ngram_counter[gram]['sentence_index'] = {(doc_id, sentence_idx)}



    return dict(sorted(ngram_counter.items(),key=lambda item:item[1]['count'],reverse = True))
