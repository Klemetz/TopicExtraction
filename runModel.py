import gensim, os, bz2, inspect, logging, sys
from gensim import corpora, models, similarities
from nltk import word_tokenize
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Most popular topics"
number_of_topics = 3

def store_papername(name, row_number):
    ws.cell(column=1, row=row_number, value=name)

def store_probable(data, row_number):
    col = 2
    for i in range(0,number_of_topics):
        if(len(data) != 0):
            ws.cell(column = col+i, row=row_number, value=str(data[i]))
        else:
            pass

def main():
#<<<<<<< Updated upstream
#    top_directory = '/home/magnus/Textfiles/TestForExporting'
#    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#    dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
#    lda = gensim.models.LdaModel.load('/home/magnus/Textfiles/TrainedModel/trained_model.lda')
#=======
    top_directory = '/home/jonathan/Documents/Stuff/FixedLemmatizedHang'
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
    lda = gensim.models.LdaModel.load('/home/jonathan/Documents/Stuff/Models/hangsomething.lda')
#>>>>>>> Stashed changes
    #lda.print_topics(num_topics=100, num_words=7)
    lda.print_topics(num_topics=100, num_words=7)
    row_number = 1
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            store_papername(file, row_number)
            print(file)
            originalString = open(os.path.join(root, file)).read()
            #originalString = originalString.lower()
            #originalString = unicode(originalString, 'utf-8')
            document = originalString
            document = word_tokenize(document)
            bow = lda.id2word.doc2bow(document)
            topic_analysis = lda[bow]
            sorted_analysis = sorted(topic_analysis, key = lambda x: x[1], reverse=True)
            print("WE HAVE CAR!", sorted_analysis)
            store_probable(sorted_analysis, row_number)
            row_number = row_number+1
            print(topic_analysis)

main()
name_of_workbook = 'most_popular_topics.xlsx'
wb.save(filename = name_of_workbook)
