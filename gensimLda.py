#This program creates an LDA model through the gensim framework on a given corpus.
#Copyright (C) 2016 Magnus Johansson <magnusjohansson82(at@)gmail(dot.)com> (Enekullegatan 12, 418 75 Göteborg), Jonathan Klemetz <jonathanklemetz(at@)gmail(dot.)com> (Färgfabriksgatan 18, 417 24 Göteborg)
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import gensim, os, bz2, inspect, logging
from gensim import corpora, models, similarities

def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            document = open(os.path.join(root, file)).read() # read the entire document, as one big string
            yield gensim.utils.tokenize(document, lower=True) # or whatever tokenization suits you

class MyCorpus(object):
    def __init__(self, top_dir):
        self.top_dir = top_dir
        self.dictionary = gensim.corpora.Dictionary(iter_documents(top_dir))
        #self.dictionary.filter_extremes(no_below=1, keep_n=30000) # check API docs for pruning params
        self.dictionary.save('/tmp/hangdeerwester.dict')

    def __iter__(self):
        for tokens in iter_documents(self.top_dir):
            yield self.dictionary.doc2bow(tokens)

def main():
    top_directory = '/home/jonathan/Documents/Stuff/FixedTrainingLemHang'
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    corpus = MyCorpus(top_directory) #Creates a MyCorpus object, containing all the documents
    dictionary = corpora.Dictionary.load('/tmp/hangdeerwester.dict')

    # Not entierly sure what this is doing, but it was necessary to create a proper corpus object.
    # I think this is because that gensims algorithms require to have the corpuses stored on the hard drive.
    corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)
    corpus = corpora.MmCorpus('/tmp/corpus.mm')
    print(corpus)

    #lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=10)
    lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus, id2word=dictionary, num_topics=100, passes=50, batch=True, workers=2, chunksize=3000, iterations=1000)

    lda.save('/home/jonathan/Documents/Stuff/Models/hangsomething.lda')
    print("Ending!")

main()