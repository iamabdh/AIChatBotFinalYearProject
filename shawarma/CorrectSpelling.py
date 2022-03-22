"""
******************  This code (Algorithm) cloned from blog Peter Norvig
******************  http://norvig.com/spell-correct.html
******************  Datasets available http://norvig.com/ngrams/
Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""
# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

import re
from collections import Counter

def words(text):
    """
    :param text:
    :return:
    """
    return re.findall(r'\w+', text.lower())

# file name
WORDS = Counter(words(open(f'{currentDir}/data.txt').read()))


def Probability(word, NoW=sum(WORDS.values())):
    """
    calculate the probability of each word may be the misspelled
    :param word:
    :param NoW:
    :return:
    """
    return WORDS[word] / NoW


def correction(word):
    return candidates(word)

def candidates(word):
    return known([word]) or known(edits1(word)) or known(edits2(word) or [word])



# only insert word that appears in the sample data ==> (datasets)
def known(words):
    """
    :param words:
    :return:
    """
    return set(w for w in words if w in WORDS)


def edits1(word) -> {}:
    """
    :param word:
    :return:
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # This step is used to separate word to two part each letters positions
    # starting from left to right
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    # list all combination of that word without one letter
    deletes = [L + R[1:] for L, R in splits if R]
    # move letter one awat to its left from its position
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    # replace first letter of the word till last letter with alphabet
    replaces = [L + C + R[1:] for L, R in splits if R for C in letters]
    # insert alphabet each position in the word
    inserts = [L + C + R for L, R in splits for C in letters]
    return set(deletes + transposes + replaces + inserts)



def edits2(word):
    """
    :param word:
    :return:
    """
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))