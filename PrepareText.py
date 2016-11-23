import pandas as pd
import numpy as np
import pronouncing as pr
from nltk.tokenize import word_tokenize
from collections import OrderedDict, defaultdict
from syllabify.syllabify import syllabify as syl
from nltk.corpus import cmudict
from hyphen import Hyphenator, dict_info
from hyphen.dictools import *
from finnsyll import FinnSyll
import copy


class PrepareText(object):
    '''
    '''

    def __init__(self, filepath):
        self.original = []
        self.lyrics_tokenized = []
        self.arpabet_dict = OrderedDict()
        self.word_syl_dict = OrderedDict()
        self.phonetic_syl_dict = OrderedDict()
        self.wrapped_vowels = OrderedDict()
        self.phone_syl_col = [] # fix issue
        self.word_syl_col = [] # fix issue

        self.read_tokenize_file(filepath)
        self.word_phonic_dict_func()
        self.clean_syllables_func()
        self.wrapping_vowel_func()
        self.phonetic_syl_list_func()
        self.word_syl_dict_update_func()
        self.word_syl_list_func()


    def read_tokenize_file(self, filepath):
        '''
        Returns a lists of tokenize lyrics
        '''
        # self.original = filepath.split('\n')
        # for line in self.original:
        #     self.lyrics_tokenized.append(line.split())

        with open(filepath) as f:
            for line in f.readlines():
                self.original.append(line)
                self.lyrics_tokenized.append(line.replace(',','').lower().split())

    def word_phonic_dict_func(self):
        '''
        Output: Ordered dictionary
            Keys - word
            Value - phonetic representation of the key
        '''
        h_en = Hyphenator('en_US')
        for line in self.lyrics_tokenized:
            for word in line:
                if word not in self.arpabet_dict.keys():
                    try:
                        self.arpabet_dict.update({word:pr.phones_for_word(word)[0]})
                        temp = h_en.syllables(unicode(word))
                        if len(temp) > 0:
                            self.word_syl_dict.update({word:temp})
                        else:
                            self.word_syl_dict.update({word:[unicode(word)]})
                    except Exception as e:
                        print e

    def word_syl_dict_update_func(self):
        word_syl_copy = self.word_syl_dict.copy()
        f = FinnSyll()
        for (w1, s1), (p1, s2) in zip(word_syl_copy.items(), self.phonetic_syl_dict.items()):
            if len(s1) < len(s2):
                leng = [len(sound) for sound in s1]
                n = max(leng)
                temp_syl = s1[leng.index(max(leng))]
                s1.remove(temp_syl)
                replace_syl = [temp_syl[:(n/2)], temp_syl[(n/2):]]
                s1.extend(replace_syl)
                self.word_syl_dict.update({w1:s1})

    def wrapping_vowel_func(self):
        '''
        Ensures that that a vowel is wrapped by consonants
        '''
        self.wrapped_vowels = copy.deepcopy(self.phonetic_syl_dict)
        for key, val in self.phonetic_syl_dict.iteritems():
            for ind, syl in enumerate(val[1:], 1):
                if self.wrapped_vowels[key][ind-1][-1][-1] == unicode(1):
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
            self.phonetic_syl_dict.update({key:word_sounds})

    def constructing_syllables(self):
        '''
        Output: Ordered dictionary
               Keys - word
               Value - phonetic syllable resentation of each word
        '''
        syl_list = OrderedDict()
        for key, val in self.arpabet_dict.iteritems():
            syl_of_key = syl(val.split())
            syl_list.update({key:syl_of_key})
        return syl_list

    def phonetic_syl_list_func(self):
        '''
        Input: syllable phonetic dictionary with value
        Output: A list which consists all the syllables

        Unpacks the values into a single list
        '''
        for phone in self.wrapped_vowels.itervalues():
            self.phone_syl_col.extend(phone)

    def word_syl_list_func(self):
        '''
        Input: syllable word dictionary with value
        Output: A list which consists all the syllables

        Unpacks the values into a single list
        '''
        for syl in self.word_syl_dict.itervalues():
            self.word_syl_col.extend(syl)



if __name__ == '__main__':
    prep = PrepareText('lyrics/mini.md')
