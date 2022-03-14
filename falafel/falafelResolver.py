import random, json, pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# add directories for calling submodule
import os, sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)
from karak.brain import brain
from falafel.falafelTraining import train
import re


def degreePlanResolver(intent):
    """
    :param intent:
    :return:
    """
    fileIntent = 'degreePlanDepartment'
    intents = json.loads(open(f'{currentDir}/falafelDatabase/{fileIntent}.json').read())
    train('degreePlanDepartment')
    words = pickle.load(open(f'{currentDir}/falafelPickle/words{fileIntent}.pkl', 'rb'))
    classes = pickle.load(open(f'{currentDir}/falafelPickle/classes{fileIntent}.pkl', 'rb'))
    model = load_model(f'{currentDir}/falafelModel/{fileIntent}model.h5')
    intents_list = brain(words, classes, model).predictClass(intent)
    if not intents_list:
        return {
            'flag': 27,
            'content': 'Unfortunately, degree plan not available'
        }
    tag = intents_list[0]['intent']
    parameter = ''
    for i in intents['intents']:
        if i['tag'] == tag:
            parameter = i['parameter']
            break
    from webScraping.degreePlanF import degreePlan
    # extract year as number from intent suppose it's written
    # conditional statement required to track missing
    year = re.findall('\d+', intent)
    if not year:
        return {
            'flag': 27,
            'content': 'You may type year in wrong way. Please type the year properly :)'
        }
    else:
        return degreePlan(parameter[0], int(year[0]))