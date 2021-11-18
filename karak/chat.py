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


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')


def cleanUpSent(sent):
    sentence_words = nltk.word_tokenize(sent)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bagOfWords(sent):
    sentence_words = cleanUpSent(sent)
    bag = [0]*len(words)

    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    print(np.array(bag))
    return np.array(bag)


def predictClass(sent):
    bagOfWord = bagOfWords(sent)
    prediction = model.predict(np.array([bagOfWord]))[0]
    print(prediction)
    errorThershold = 0.6
    results = [[i, r] for i, r in enumerate(prediction) if r > errorThershold]
    results.sort(key = lambda x : x[1], reverse = True)
    print(results) 
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list 


def getResponses(intents_list, intents_json, quires = None):
    result = ''
    try: 
        tag = intents_list[0]['intent']
            
        listOfIntents = intents_json['intents']
        for i in listOfIntents:
            if i['tag'] == tag:
                if i['response'][0] != 0:
                    result = random.choice(i['response'])
                    break
                else:
                    # excute function that will resolve the kind of initents
                    # excute based on classes that may initats
                    if i['flag'] == 1:
                        from webScraping import resolverMainWeb as res
                        '''
                        retrive response with required intents
                        that will add to result based on quires
                        '''
                        dataObj= res.resloverIntents(i['init'])

                        subText = dataObj.get(i['required']).get('subText') 
                        extend = dataObj.get(i['required']).get('extend')
                     

                        for item in subText:
                            result += item + '\n'
                        if extend is not None:
                            for index, item in enumerate(extend):
                                result += f'{index + 1} ' + item + '\n'
                    
                    elif i['flag'] == 2:
                        '''
                        flag 2 that resolve  for faculty stuff search 
                        based static intents that user may required the intent such as Dr. or prof or whatever
                        the chat will check the all intents if doesnt find any thing will will check faculty stuff 
                        to resolve the intents 
                        '''
                        from webScraping import resolverMainWeb as res
                        dataObj = res.resloverIntents(i['init'], quires)
                        if dataObj != 0:
                            result += 'name: '+ dataObj.get('name') + '\n'
                            result += 'role: '+ dataObj.get('role') + '\n'
                            result += 'room: '+ dataObj.get('roomNo') + '\n'
                            result += 'email: '+ dataObj.get('email') + '\n'
                        else:
                            result = "please provide correct and full faculty names"


                        
                        
    except IndexError:
        result = "I dont understnad"

    return result

print("BOT IS RUNNING")



from flask import Flask
from flask import request

# setup flask server
app = Flask(__name__)

@app.route('/getData', methods = ['POST'])
def getData():
    message = request.get_json()
    message = message.get('msg')
    ints = predictClass(message.lower())
    print(ints)
    res = getResponses(ints, intents, message)
    return json.dumps({'result' : res})


if __name__ == '__main__':
    app.run(port=5000)