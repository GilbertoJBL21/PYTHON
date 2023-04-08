#*********************************************IMPORTS************************************************************#
import nltk
from nltk.stem.lancaster import LancasterStemmer#This is a module found in the NLTK library that provides us with the necessary tools for natural language
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import json
import pickle
import numpy

#*****************************************OPEN AND LOAD JSON*****************************************************#
with open('intents.json') as file:
    data = json.load(file)

#*******************************************EMPTY LISTS*********************************************************#
words = []
tags = []
auxX = []
auxY = []

#****************************************FUNCTION TO ORGANIZE THE WORDS******************************************#
for intents in data["intents"]:
    for patterns in intents["patterns"]:
        mpl = nltk.word_tokenize(patterns)
        words.extend(mpl)
        auxX.append(mpl)
        auxY.append(intents["tag"])
        
        if intents["tag"] not in tags:
            tags.append(intents["tag"])

#**********************CODES TO SCROLL THE EXTRACTED WORDS AND ELIMINATE THE REPEATED WORDS*********************#
words = [stemmer.stem(w.lower()) for w in words if w!="?"]