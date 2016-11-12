import pandas as pd
import numpy as np
import pronouncing as pr
from nltk.tokenize import word_tokenize
from nltk.corpus import cmudict
from collections import OrderedDict

def read_tokenize_file(filepath):
    '''
    Returns 2 - d lists of tokenize lyrics
    '''
    content = []
    with open(filepath) as f:
        for line in f.readlines():
            content.append(word_tokenize(line.lower().strip()))
    return content


def word_aphabet_dict(string):
    '''
    Input: 2 - d list of tokenied workds
    Output: Ordered dictionary:
        Keys - word
        Value - phonetic representation of the key
    '''
    aphabet = cmudict.dict()
    word_phonetic = OrderedDict()
    for l in string:
        print l
        print '\n***************\n'
        for word in l:
            try:
                # print word
                word_phonetic.update({word:aphabet[word][0]})
            except Exception as e:
                print e
    return word_phonetic


def word_aphabet_tuple(string):
    '''
    Input: 2 - d list of tokenied workds
    Output: Tuple:
        Keys - word
        Value - phonetic representation of the key
    '''
    aphabet = cmudict.dict()
    output = []
    for line in string:
        for  word in line:
            try:
                output.append((word, aphabet[word][0]))
            except Exception as e:
                print e
    return output





if __name__ == '__main__':
    verse = read_tokenize_file('mini.txt')
    # for line in verse:
        # print verse
        # print '\n******2******\n'
    phonetics = word_aphabet_tuple(verse)
    print phonetics
