### Installations
```bash
conda create -y --name eigen python=3.10
conda install --force-reinstall -y -q --name eigen -c conda-forge --file requirements.txt
conda activate eigen
```
In python shell run:
```python
import nltk
nltk.download()
```

### What to run?
User is expected to run the jupter notebook explore.ipynb. <br>
Comments are provided before each cell on what is being done and all heavy lifting is done in the rest of the code.<br>

### Text pre-processign:
* Text normalisation and cleaning when necessary.
* removing stopwords
* lemmatizing words

### Feature Extraction:
* where generating BOW and TFIDF vector was done.
* Ngrams were created for the most common terms

### Output files:
* tfidf.csv
* ngrams.csv