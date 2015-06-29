
# coding: utf-8

# In[284]:

import nltk
from nltk import FreqDist
import csv
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict


# In[285]:

with open ("SGLyrics.txt", "r") as myfile:
    text=myfile.read().replace('\n', '')


# In[286]:

tokenizer = RegexpTokenizer(r'\w+')
nltext=nltk.Text(tokenizer.tokenize(text))


# In[287]:

print (nltext)


# In[288]:

nltext[1024:1062]


# In[289]:

nltext.collocations()


# In[290]:

filtered_words=[word for word in nltext if word.lower() not in stopwords.words('english') and len(word) >=3]


# In[291]:

print (filtered_words)


# In[292]:

commonText=nltk.Text(filtered_words)


# In[293]:

commonText


# In[294]:

freq=FreqDist(commonText)


# In[295]:

visualize=(freq.most_common(25))


# In[296]:

dV=dict(visualize)


# In[297]:

finalData=OrderedDict(sorted(dV.items(), key=lambda t: t[1],reverse=True))


# In[298]:

print (finalData)


# In[299]:

writer = csv.writer(open('visual.csv', 'a'))
for key, value in finalData.items():
   writer.writerow([key, value])


# In[ ]:



