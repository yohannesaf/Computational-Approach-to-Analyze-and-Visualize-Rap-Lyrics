import numpy as np
import pronouncing as pr
from collections import OrderedDict, defaultdict
from syllabify.syllabify import syllabify
from nltk.corpus import cmudict
from hyphen import Hyphenator, dict_info
from unidecode import unidecode
import regex
import copy


class PrepareText(object):
    '''
    Breaks lyrics apart for analysis
    '''

    def __init__(self, filepath):
        self.root = []
        self.lyrics_tokenized = []
        self.arpabet_dict = OrderedDict()
        self.word_syl_dict = OrderedDict()
        self.phonetic_syl_dict = OrderedDict()
        self.wrapped_vowels = OrderedDict()
        self.phone_syl_col = []
        self.word_syl_col = []

        self.read_tokenize_file(filepath)
        self.tokenize_lyric_clean_up()
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
        with open(filepath) as f:
            for line in f.readlines():
                self.root.append(line)
                self.lyrics_tokenized.append(line.replace(',','').replace('?','').lower().split())

    def tokenize_lyric_clean_up(self):
        lines = []
        for line in self.lyrics_tokenized:
            words = []
            for word in line:
                words.append(unicode(word.decode('utf8').encode('ascii', errors='ignore')))
            lines.append(words)
        self.lyrics_tokenized = lines

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
        '''
        Updates word syllables not syllabified like phonetic syllables
        '''
        word_syl_copy = self.word_syl_dict.copy()
        for (w1, s1), (p1, s2) in zip(word_syl_copy.items(), self.phonetic_syl_dict.items()):
            while len(s1) < len(s2):
                leng = [len(sound) for sound in s1]
                ind = leng.index(max(leng))
                temp_syl = s1[leng.index(max(leng))]
                split1, split2 = self.first_vowel_split(temp_syl)
                s1.remove(temp_syl)
                s1.insert(ind, split1)
                s1.insert(ind+1, split2)
                self.word_syl_dict.update({w1:s1})
            while len(s1) > len(s2):
                s1 = [''.join(s1)]
                self.word_syl_dict.update({w1:s1})

    def first_vowel_split(self, word):
        '''
        Additional split of sylable to match the number of phonetic syl
        '''
        index = self.index_split(word)
        index += 1
        return word[:index], word[index:]

    def index_split(self, word):
        '''
        Returns the index of the first vowel occurance
        '''
        for index, char in enumerate(word):
            if char in 'aeiouy':
                return int(index)
            elif len(word) == 2:
                return 0
            else:
                return len(word)/2

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
               Value - phonetic syllable representation of each word
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
               Value - phonetic syllable reprentation of each word
        '''
        syl_list = OrderedDict()
        for key, val in self.arpabet_dict.iteritems():
            syl_of_key = syllabify(val.split())
            syl_list.update({key:syl_of_key})
        return syl_list

    def phonetic_syl_list_func(self):
        '''
        Input: syllable phonetic dictionary with value
        Output: A list which consists all the syllables

        Unpacks the values into a single list
        '''
        for phone in self.wrapped_vowels.itervalues():
            for sound in phone:
                self.phone_syl_col.append(sound)

    def word_syl_list_func(self):
        '''
        Input: syllable word dictionary with value
        Output: A list which consists all the syllables

        Unpacks the values into a single list
        '''
        for syl in self.word_syl_dict.itervalues():
            for sound in syl:
                self.word_syl_col.append(sound)


if __name__ == '__main__':

    prep = PrepareText('lyrics/Andre_3000.md')
