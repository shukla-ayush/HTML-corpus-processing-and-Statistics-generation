# HTML Corpus Statistics using inverted index

Implementation has been done in Python 3.

* Raw downloaded HTML files are required as input to Text_Processing.py which then generates a clean and processed text file.
* The processed text files (corresponding to the web pages), are given as input to Corpus_Statistics.py, that generates the Inverted index, each for unigram, bigram and trigram.
* Corpus_Statistics.py then generates text files showing term frequency and document frequency statistics, for all the generated inverted indexes (unigram, bigram, trigram).
