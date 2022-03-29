# add directories for calling submodule
import os, sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

"""
This script used mainly to develop guides to user base o some query
that may written by user end 
"""


def guide():
    return {
        "Main Guide ": {
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
            "subText" :  ["Just type course code follwed by course number such as ECCE4242. All SQU courses are available."],
        },
         "Faculty Search": {
             "subText": ["For searching faculty just provide Mr. or Dr. Prof. For example Dr. Zia Nadir or if only first name. Faculty College avalible: "],
             "extend": ["Engineering", "Economic", "Art and Social Sciences", "Medicine", "Science"]
         }
    }
