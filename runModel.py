import gensim, os, bz2, inspect, logging, sys
from gensim import corpora, models, similarities
from nltk import word_tokenize

def main():
    top_directory = '/home/jonathan/Documents/Stuff/Lemmatized'
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
    lda = gensim.models.LdaModel.load('/home/jonathan/Documents/Stuff/Models/something.lda')
    #lda.print_topics(num_topics=100, num_words=7)
    lda.print_topics(num_topics=100, num_words=7)
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            print(file)
            originalString = open(os.path.join(root, file)).read()
            originalString = originalString.lower()
            originalString = unicode(originalString, 'utf-8')
            document = originalString
            document = word_tokenize(document)
            bow = lda.id2word.doc2bow(document)
            topic_analysis = lda[bow]
            print(topic_analysis)

main()