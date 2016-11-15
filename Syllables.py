import pandas as pd
import numpy as np
import pronouncing as pr
from nltk.tokenize import word_tokenize
from collections import OrderedDict
from syllabify.syllabify import syllabify as sly
from nltk.corpus import cmudict


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
    for line in string:
        for word in line:
            try:
                # word_phonetic.update({word:aphabet[word][0]}) # using nltk
                word_phonetic.update({word:pr.phones_for_word(word)[0]})
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
                # output.append((word, aphabet[word][0])) # using nltk tools
                output.append((word, pr.phones_for_word(word)[0]))
            except Exception as e:
                print e
    return output

def clean_syllables(phonetic_dict):
    '''
    Input: None
    Output: Ordered dictionary
           Keys - word
           Value - phonetic syllable replresentation of each word

    Calls the function constructing_syllables & clean up the syllables
    '''
    phonetic_dict = constructing_syllables(phonetic_dict)
    clean_syll = OrderedDict()
    for key, val in phonetic_dict.iteritems():
        word_sounds = []
        for syl in val:
            sound = []
            for ph in syl:
                sound += ph
            word_sound.append(sound)
        clean_syll.update({key:word_sound})
    return clean_syll

def constructing_syllables(phonetic_dict):
    '''
    Input: Ordered dictionary
           Keys - word
           Value - phonetic representation of the key
    Output: Ordered dictionary
           Keys - word
           Value - phonetic syllable replresentation of each word
    '''
    syl_list = OrderedDict()
    for key, val in phonetic_dict.iteritems():
        syl_of_key = syl(val.split())
        syl_list.update({key:syl_of_key})
    return syl_list


def is_vowel(char):
    '''
    Returns true if a character is a vowel
    '''
    vowels = 'aeiouAEIOU'
    return char in vowels

def is_num(char = 'x'):
    '''
    Returns true if a character is a number
    '''
    return char.isdigit()




if __name__ == '__main__':
    verse = read_tokenize_file('lyrics/forgot.txt')
    # verse = read_tokenize_file('lyrics/mini.txt')
    check = is_vowel('w')
    phonetics_dict = word_aphabet_dict(verse)
    # phonetics_tuple = word_aphabet_tuple(verse)
    test = constructing_syllables(phonetics_dict)
    check = clean_syll(test)
