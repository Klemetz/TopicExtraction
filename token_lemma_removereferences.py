#This program pre-proccess text files so that they are in proper shape before being entered in any of the other programs. 
#Copyright (C) 2016 Magnus Johansson <magnusjohansson82(at@)gmail(dot.)com> (Enekullegatan 12, 418 75 Göteborg), Jonathan Klemetz <jonathanklemetz(at@)gmail(dot.)com> (Färgfabriksgatan 18, 417 24 Göteborg)
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import nltk.corpus
import sys

#stopWords = nltk.corpus.stopwords
stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'fig']

currentFile = open(sys.argv[1])

print str(sys.argv[1])
stringToTokenize = currentFile.read()
#currentFile.close()
stringToTokenize = stringToTokenize.lower()
stringToTokenize = unicode(stringToTokenize, 'utf-8')

tokenizer = RegexpTokenizer('[a-z]\w+')

tokenizedString = tokenizer.tokenize(stringToTokenize)
#print(tokenizedString)


lemmatizer = WordNetLemmatizer()
lemmatizedList = [lemmatizer.lemmatize(t) for t in tokenizedString]

counter = 0
for word in lemmatizedList:
    if word == 'the':
        counter = (counter + 1)

print("No of the's: ", counter)
for word in lemmatizedList:
    if word in stopWords:
        print("removing ", word, " from list")
	#if word in stopWords.words('english'):
        lemmatizedList.remove(word)

counter2 = 0
for word in lemmatizedList:
    if word == 'the':
        counter2 = (counter2 + 1)

print("No of the's after stopword removal: ", counter2)

counter3 = 0
for word in lemmatizedList:
    if word in stopWords:
        print("removing ", word, " from list")
        # if word in stopWords.words('english'):
        lemmatizedList.remove(word)
print("No of the's after stopword removal 2nd pass xD : ", counter3)


#print(lemmatizedList)

""" look through the list, find the last occurence of "reference" (remember s is removed)
and delete the rest of the list

code goes here....
"""


refID = 0
hasReferences = False
for index, word in enumerate(lemmatizedList):
    if word == "reference":
        # print(index)
        hasReferences = True
        refID = index

finalString = lemmatizedList
#print(refID)
if hasReferences:
    finalString = lemmatizedList[: refID]


newFileName = 'lemmatized_' + str(sys.argv[1])
with open(newFileName, 'w') as newFile:

    for item in finalString:
        newFile.write(" " + item.encode('utf-8'))