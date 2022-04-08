import json, pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# add directories for calling submodule
import os, sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

import brain
import responseHandler
from flask import Flask
from flask import request

# setup flask server
app = Flask(__name__)

lemmatizer = WordNetLemmatizer()
intents = json.loads(open(f'{currentDir}/karakDatabase/intents.json').read())
words = pickle.load(open(f'{currentDir}/karakPickle/words.pkl', 'rb'))
classes = pickle.load(open(f'{currentDir}/karakPickle/classes.pkl', 'rb'))
model = load_model(f'{currentDir}/karakModel/chatbotmodel.h5')


@app.route('/getData', methods=['POST'])
def getData():
    message = request.get_json()
    message = message.get('msg')
    ints = brain.brain(words, classes, model).predictClass(message.lower())
    print(ints)
    response = responseHandler.getResponses(ints, intents, message)
    if response["flag"] == 404:
        """
        check spelling correction based on shawarma module
        """
        from shawarma.CorrectSpelling import CorrectSpelling
        correctIntent = CorrectSpelling(message).spell()
        print("corrected word: ", correctIntent)
        ints = brain.brain(words, classes, model).predictClass(correctIntent.lower())
        if ints:
            # found response that may resolve wrong query 
            # saveInts is used to perform standard query request without repeating ML code again
            response = {
                'response': correctIntent,
                'flag': 9,
                'savedInts': ints
            }
        else:
            response = {
                'response': "I don't understand!",
                'flag': 404
            }

    return json.dumps({'result': json.dumps(response)})


@app.route('/getInitData', methods=['POST'])
def getInitData():
    objectDataInit = request.get_json()
    from webScraping import resolverMainWeb as res
    dataObj = res.resloverIntents(objectDataInit.get('initData'))
    subText = dataObj.get(objectDataInit.get('required')).get('subText')
    extend = dataObj.get(objectDataInit.get('required')).get('extend')
    objectResponse = json.dumps({
        'subText': subText,
        'extend': extend,
        'flag': 1,
        'linker': True if len(objectDataInit.get('additional')) > 0 else False,
        'init': objectDataInit.get('initData'),
        'notInit': False,
        'additional': objectDataInit.get('additional')})
    return json.dumps({'result': objectResponse})


# this post route for flag 9 that is used to handle uncorrected query
@app.route('/getDataWithInts', methods=['POST'])
def getDataWithInts():
    objectDataWithInts = request.get_json()
    ints = objectDataWithInts.get('savedInts')
    clickedSuggestion = objectDataWithInts.get('clickedSuggestion')
    response = responseHandler.getResponses(ints, intents, clickedSuggestion)
    return json.dumps({'result': json.dumps(response)})


if __name__ == '__main__':
    app.run(port=5000)
