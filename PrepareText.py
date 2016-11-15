import pandas as pd
import numpy as np
import pronouncing as pr
from nltk.tokenize import word_tokenize
from collections import OrderedDict
from syllabify.syllabify import syllabify as syl
from nltk.corpus import cmudict


class PrepareText(object):
    '''
    '''

    def __init__(self):
        self.lyrics_tokenized = []
        self.aphabet_dict = OrderedDict()
        self.syllable_dict = OrderedDict()
        # self.aphabet_tuple = None
        # self.syllable_tuple = None


    def read_tokenize_file(self, filepath):
        '''
        Returns 2 - d lists of tokenize lyrics
        '''
        self.lyrics_tokenized = []
        with open(filepath) as f:
            for line in f.readlines():
                self.lyrics_tokenized.append(word_tokenize(line.lower().strip()))


    def word_aphabet_dict(self):
        '''
        Input: 2 - d list of tokenied workds
        Output: Ordered dictionary:
            Keys - word
            Value - phonetic representation of the key
        '''
        for line in self.lyrics_tokenized:
            for word in line:
                try:
                    self.aphabet_dict.update({word:pr.phones_for_word(word)[0]})
                except Exception as e:
                    print e


    def word_aphabet_tuple(self):
        '''
        Input: 2 - d list of tokenied workds
        Output: Tuple:
            Keys - word
            Value - phonetic representation of the key
        '''
        for line in self.lyrics_tokenized:
            for  word in line:
                try:
                    self.aphabet_tuple.append((word, pr.phones_for_word(word)[0]))
                except Exception as e:
                    print e

    def clean_syllables(self):
        '''
        Input: None
        Output: Ordered dictionary
               Keys - word
               Value - phonetic syllable replresentation of each word

        Calls the function constructing_syllables & clean up the syllables
        '''
        syl_temp = self._constructing_syllables(self.phonetic_dict)
        for key, val in syl_temp.iteritems():
            word_sounds = []
            for syl in val:
                sound = []
                for ph in syl:
                    sound += ph
                word_sounds.append(sound)
            self.syllable_dict.update({key:word_sounds})

    def _constructing_syllables(self):
        '''
        Input: Ordered dictionary
               Keys - word
               Value - phonetic representation of the key
        Output: Ordered dictionary
               Keys - word
               Value - phonetic syllable replresentation of each word
        '''
        syl_list = OrderedDict()
        for key, val in self.phonetic_dict.iteritems():
            syl_of_key = syl(val.split())
            syl_list.update({key:syl_of_key})
        return syl_list





if __name__ == '__main__':
    verse = read_tokenize_file('lyrics/forgot.txt')
    # verse = read_tokenize_file('lyrics/mini.txt')
    check = is_vowel('w')
    phonetics_dict = word_aphabet_dict(verse)
    # phonetics_tuple = word_aphabet_tuple(verse)
    test = constructing_syllables(phonetics_dict)
    check = clean_syllables(test)
