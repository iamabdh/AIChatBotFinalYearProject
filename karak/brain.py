# add directories for calling submodule
import os, sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

import random, json, pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()


class brain:
    """
    """

    def __init__(self, words, classes, model):
        self.words = words
        self.classes = classes
        self.model = model

    def cleanUpSent(self, sent):
        sentence_words = nltk.word_tokenize(sent)
        sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words

    def bagOfWords(self, sent):
        sentence_words = self.cleanUpSent(sent)
        bag = [0] * len(self.words)

        for w in sentence_words:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1

        print(np.array(bag))
        return np.array(bag)

    def predictClass(self, sent):
        bagOfWord = self.bagOfWords(sent)
        prediction = self.model.predict(np.array([bagOfWord]))[0]
        print(prediction)
        errorThershold = 0.7
        results = [[i, r] for i, r in enumerate(prediction) if r > errorThershold]
        results.sort(key=lambda x: x[1], reverse=True)
        print(results)
        return_list = []
        for r in results:
            return_list.append({'intent': self.classes[r[0]], 'probability': str(r[1])})

        return return_list
