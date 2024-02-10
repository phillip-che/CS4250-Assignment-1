#-------------------------------------------------------------------------
# AUTHOR: Phillip Che
# FILENAME: indexing.py
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = set(["I", "and", "her", "She", "They", "their"])

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {"cat": {"cat", "cats"}, "dog": {"dog", "dogs"}, "love": {"love", "loves"}}

#Identifying the index terms.
terms = set()
tf = []
df = {}
size = len(documents)
for i in range(0, size):
    doc = documents[i].split()
    freq = {}
    for word in doc:
        if (word not in stopWords):
          for key in stemming:
              if (key not in freq):
                  freq[key] = 0
              if(word in stemming[key]):
                  terms.add(key)
                  freq[key] = freq[key]+1
    tf.append(freq)

for term in terms:
  if(term not in df):
      df[term] = 0
  for i in range(0, size):
    if(term in documents[i]):
      df[term] = df[term]+1

idf = {}
for key in df:
   idf[key] = math.log((size/df[key]), 10)

#Building the document-term matrix by using the tf-idf weights.
docTermMatrix = []
wordCount = []

for i in range(0, len(tf)):
  count = 0
  for key in tf[i]:
    count += tf[i][key]
  wordCount.append(count)

for i in range(0, len(tf)):
  docTerm = {}
  for key in tf[i]:
    x = (tf[i][key]/wordCount[i])*idf[key]
    docTerm[key] = round(x, 3)
  docTermMatrix.append(docTerm)

#Printing the document-term matrix.
#--> add your Python code here

for i in range(0, len(docTermMatrix)):
   print("d" + str(i+1) + ":", docTermMatrix[i])