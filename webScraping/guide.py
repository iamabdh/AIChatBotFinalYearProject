# add directories for calling submodule
import os, sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

"""
This script used mainly to develop guides to user base on some query
that may written by user end 
"""


def guide():
    return {
        "Main Guide": {
            "subText": ["Hi This guide message you can select any topics you want to search: "]
        },
        "Library Search": {
            "subText": ["You can type Any SQU library such as: where is main library. Library included are: "],
            "extend": ["Main Library", "Medical Library", "Sciences Library", "CEPS Library", "Mosque Library", "Education Library"]
        },
        "Job": {
            "subText": ["You can type any thing about job will find available positions in SQU."]
        },
        "Course Search": {
            "subText" :  ['Just type course code follwed by course number such as <mark>course search ECCE 4242</mark>. All SQU courses are available.'],
        },
         "Faculty Search": {
             "subText": ["For searching faculty just provide Mr or Dr, Prof.  For example <mark>Dr Zia Nadir </mark> or if only first name. Faculty College avalible: "],
             "extend": ["Engineering", "Economic", "Art and Social Sciences", "Medicine", "Science"]
         }, 
         "Degree Plan": {
             "subText": ["For searching degree plan please provide the department and the year for example: <mark>degree plan of electrical 2020</mark>. Degree plan only for college of engineering 👨🏻‍🔧."]
         }
    }
