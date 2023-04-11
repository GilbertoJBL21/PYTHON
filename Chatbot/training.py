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
import random

#*****************************************OPEN AND LOAD JSON*****************************************************#
with open('intents.json',encoding='utf-8') as file:
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
words = sorted(list(set(words)))
tags = sorted(tags)

#******************************************TRAINING*************************************************************#
training = []
output = []

empty_output = [0 for _ in range(len(tags))]

for x, document in enumerate(auxX):
    tray = []
    mpl = [stemmer.stem(w.lower()) for w in document]
    for w in words:
        if w in mpl:
            tray.append(1)
        else:
            tray.append(0)
    output_row = empty_output[:]
    output_row[tags.index(auxY[x])] = 1
    training.append(tray)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

with open("variables.pickle","wb") as pf:
    pickle.dump((words, tags, training, output), pf)

#**********************************CREATION OF NEURAL NETWORK AND SAVE MODEL*************************************************#
tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net, 10)
net = tflearn.fully_connected(net, 10)
net = tflearn.fully_connected(net,len(output[0]),activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training,output,n_epoch=10000,batch_size=29, show_metric=True)
model.save("model.tflearn")