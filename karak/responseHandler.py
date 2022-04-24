import random
# add directories for calling submodule
import os, sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)


def getResponses(intents_list, intents_json, quires=None):
    result = ''
    objectResponse = ''
    try:
        tag = intents_list[0]['intent']

        listOfIntents = intents_json['intents']
        for i in listOfIntents:
            if i['tag'] == tag:
                if i['response'][0] != 0:

                    reesponseRandomly = random.choice(i['response'])
                    objectResponse = {
                        'response': reesponseRandomly,
                        'flag': 0
                    }
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
                        dataObj = res.resloverIntents(i['init'])
                        print("*"*100)
                        print(dataObj)
                        print("*"*100)
                        subText = dataObj.get(i['required']).get('subText')
                        extend = dataObj.get(i['required']).get('extend')

                        objectResponse = {
                            'subText': subText,
                            'extend': extend,
                            'flag': 1,
                            'linker': True,
                            'init': i['init'],
                            'notInit': False,
                            'additional': [item for item in list(dataObj.keys()) if item != i['required']]
                        }
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
                            objectResponse = {
                                "searchFFResult": dataObj,
                                'flag': 2
                            }
                        else:
                            objectResponse = {
                                'flag': 22
                            }
                    elif i['flag'] == 3:
                        """

                        """
                        from webScraping import resolverMainWeb as res
                        dataObj = res.resloverIntents(i['init'], quires)
                        if dataObj != 0:
                            objectResponse = {
                                "StaffServices": dataObj,
                                'flag': 3
                            }
                        else:
                            objectResponse = {
                                'flag': 33
                            }
                    elif i['flag'] == 4:
                        """

                        """
                        from webScraping import resolverMainWeb as res
                        dataObj = res.resloverIntents(i['init'], quires)
                        if dataObj != 0:
                            objectResponse = {
                                "OnlineServices": dataObj,
                                'flag': 4
                            }
                        else:
                            objectResponse = {
                                'flag': 44
                            }
                    elif i['flag'] == 5:
                        """

                        """
                        from webScraping import resolverMainWeb as res
                        dataObj = res.resloverIntents(i['init'], quires)
                        if dataObj != 0:
                            objectResponse = {
                                "JobServices": dataObj,
                                'flag': 5
                            }
                        else:
                            objectResponse = {
                                'flag': 55
                            }

                    elif i['flag'] == 7:
                        from falafel.falafelResolver import degreePlanResolver
                        objectResponse = degreePlanResolver(quires)
                    elif i['flag'] == 8:
                        from webScraping import resolverMainWeb as res
                        dataObj = res.resloverIntents(i['init'], quires)
                        if dataObj:
                            objectResponse = {
                                "CourseSearch": dataObj,
                                'flag': 8
                            }
                        else:
                            objectResponse = {
                                "ERROR": "Unfortunatelly, the course not available or you typed it wrongly",
                                'flag': 88
                            }
    except IndexError:
        objectResponse = {
            'response': "I don't understand!",
            'flag': 404
        }

    return objectResponse
