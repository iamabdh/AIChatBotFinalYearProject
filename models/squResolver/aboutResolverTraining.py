import random, json
import pickle

import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('aboutIntents.json').read())
print(intents)

