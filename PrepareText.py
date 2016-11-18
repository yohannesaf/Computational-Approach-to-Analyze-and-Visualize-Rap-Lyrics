import pandas as pd
import numpy as np
import pronouncing as pr
from nltk.tokenize import word_tokenize
from collections import OrderedDict, defaultdict
from syllabify.syllabify import syllabify as syl
from nltk.corpus import cmudict
import copy


class PrepareText(object):
    '''
    '''

    def __init__(self, filepath):
        self.original = []
        self.lyrics_tokenized = []
        self.aphabet_dict = OrderedDict()
        self.syllable_dict = OrderedDict()
        self.wrapped_vowels = OrderedDict()

        self.read_tokenize_file(filepath)
        self.word_aphabet_dict()
        self.clean_syllables_func()
        self.wrapping_vowel_func()

    def read_tokenize_file(self, filepath):
        '''
        Returns a lists of tokenize lyrics
        '''
        with open(filepath) as f:
            for line in f.readlines():
                self.original.append(line)
                self.lyrics_tokenized.append(word_tokenize(line.lower().strip()))

    def word_aphabet_dict(self):
        '''
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

    def wrapping_vowel_func(self):
        '''
        Ensures that that a vowel is wrapped by consonants
        '''
        self.wrapped_vowels = copy.deepcopy(self.syllable_dict)
        # for key, val in self.syllable_dict.iteritems():
        #     for ind, syl in enumerate(val[1:], 1):
        #         self.wrapped_vowels[key][ind-1].append(syl[0])
        for key, val in self.syllable_dict.iteritems():
            for ind, syl in enumerate(val[1:], 1):
                self.wrapped_vowels[key][ind-1].append(syl[0])

    def clean_syllables_func(self):
        '''
        Input: None
        Output: Ordered dictionary
               Keys - word
               Value - phonetic syllable replresentation of each word
        Calls the function constructing_syllables & clean up the syllables
        '''
        syl_temp = self.constructing_syllables()
        for key, val in syl_temp.iteritems():
            word_sounds = []
            for syl in val:
                sound = []
                for ph in syl:
                    sound += ph
                word_sounds.append(sound)
            self.syllable_dict.update({key:word_sounds})

    def constructing_syllables(self):
        '''
        Output: Ordered dictionary
               Keys - word
               Value - phonetic syllable replresentation of each word
        '''
        syl_list = OrderedDict()
        for key, val in self.aphabet_dict.iteritems():
            syl_of_key = syl(val.split())
            syl_list.update({key:syl_of_key})
        return syl_list


if __name__ == '__main__':
    text = PrepareText('lyrics/mini.md')
