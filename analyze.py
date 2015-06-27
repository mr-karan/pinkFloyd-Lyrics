__author__ = 'karan'

import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer
import csv

with open ("lyricsAll.txt", "r") as myfile:
    text=myfile.read().replace('\n', '')

tokenizer = RegexpTokenizer(r'\w+')
nltext=nltk.Text(tokenizer.tokenize(text))
filtered_words = [w for w in nltext if not w in stopwords.words('english')]

commonText=nltk.Text(filtered_words)
freq=FreqDist(commonText)
visualize=(freq.most_common(50))
finalVisual=dict(visualize)
writer = csv.writer(open('visual.csv', 'a'))
for key, value in finalVisual.items():
   writer.writerow([key, value])