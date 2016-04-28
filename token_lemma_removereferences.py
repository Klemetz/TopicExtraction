from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk.corpus
import sys

stopWords = nltk.corpus.stopwords

file = open(sys.argv[1])

print str(sys.argv[1])
originalString = file.read()
originalString = originalString.lower()
originalString = unicode(originalString, 'utf-8')


tokenizedString = word_tokenize(originalString)
print(tokenizedString)

for word in tokenizedString:
    if word in stopWords.words('english'):
        tokenizedString.remove(word)

lemmatizer = WordNetLemmatizer()
lemmatizedList = [lemmatizer.lemmatize(t) for t in tokenizedString]

print(lemmatizedList)

""" look through the list, find the last occurence of "reference" (remember s is removed)
and delete the rest of the list

code goes here....
"""
refID = 0
for index, word in enumerate(lemmatizedList):
    if word == "reference":
        print(index)
        refID = index


print(refID)

finalString = lemmatizedList[: refID]


newFileName = 'lemmatized_' + str(sys.argv[1])

with open(newFileName, 'w') as newFile:

    for item in finalString:
        newFile.write(" " + item.encode('utf-8'))
