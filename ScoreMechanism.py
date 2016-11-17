from PrepareText import PrepareText
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations
import copy

class ScoreMechanism(object):
    '''
    Creates a list of columns headers and score matrix
    '''

    def __init__(self, lyrics_tokenized, syllable_dict):
        self.lyrics_tokenized = lyrics_tokenized
        self.syllable_dict = syllable_dict
        self.col = []
        self.adjacency_matrix = []

        self.syllable_list()
        self.similarity_mat()


    def similarity_mat(self):
        '''
        Creates a 'score' matrix for each syllables
        '''
        temp_score = self.score_shape()
        row = copy.deepcopy(self.col)
        for ind1, val1 in enumerate(self.col):
            for ind2, val2 in enumerate(row):
                if val1 != val2:
                    common_sound = self.sound_intersect(val1, val2)
                    points = self.final_score(val1, val2, common_sound)
                    temp_score[ind1][ind2] = points
                else:
                    temp_score[ind1][ind2] = 0
        self.adjacency_matrix = temp_score

    def syllable_list(self):
        '''
        Input: syllable dictionary with value
        Output: A list which consists all the syllables

        Unpacks the values into a single list
        '''
        for val in self.syllable_dict.itervalues():
            self.col.extend(val)


    def score_shape(self):
        dim = 0
        for word in self.syllable_dict.itervalues():
            dim += len(word)
        return np.zeros((dim,dim))


    def final_score(self, phonetic1, phonetic2, common_sounds):
        '''
        Input: 2 phonetic and list of common sounds between two phonetics
        Output: Score based on phonetic sound

        Calculates score for the common sounds
        '''
        points = 0
        for sound in common_sounds:
            if len(sound) > 1:
                points += self.vowel_score(sound)
            else:
                points += self.consonant_score(phonetic1, phonetic2, sound)
        return points


    def consonant_score(self, phonetic1, phonetic2, sound):
        '''
        Input: Consonant phone
        Output: Consonant phone score

        Assigns consonant phone score based on whether it is prefix or suffix
        '''
        sound_pos = self.prefix_check(phonetic1, phonetic2, sound)
        if sound_pos == 1:
            return 1
        elif sound_pos == 2:
            return 2.5
        else:
            return 0

    def prefix_check(self, phonetic1, phonetic2, sound):
        '''
        Input: Two phonetic sounds with common element sound
        Output: Bool if the sound is prefix

        Checks whether a consonant is a prefix or suffix or didn't match either
        1 - prefix, 2 - suffix, 0 - mix-match
        '''
        ph1_len = [len(cons) for cons in phonetic1]
        ph2_len = [len(cons) for cons in phonetic2]
        ind1 = phonetic1.index(sound)
        ind2 = phonetic2.index(sound)
        if (ind1 < ph1_len.index(max(ph1_len))) and (ind2 < ph2_len.index(max(ph2_len))):
            return 1
        elif (ind1 > ph1_len.index(max(ph1_len))) and (ind2 > ph2_len.index(max(ph2_len))):
            return 2
        else:
            return 0

    def vowel_score(self, sound):
        '''
        Input: Vowel phone
        Output: Vowel phone score

        Assigns score to a common phone vowel bewteen 2 words based on their stress.
        '''
        if sound[-1] > 0:
            return len(sound) * 3
        else:
            return len(sound) + 2

    def sound_intersect(self, phonetic1, phonetic2):
        '''
        Input: Two phonetic to be compared
        Output: sound found in both phonetic

        Find common sounds in the two phonetics
        '''
        return list(set(phonetic1) & set(phonetic2))

    def is_vowel(self, text):
        '''
        Returns true if a character is a vowel
        '''
        vowels = 'aeiouAEIOU'
        return [True if char in vowels else False for char in text]

    def is_num(self, char):
        '''
        Returns true if a character is a number
        '''
        return char.isdigit()



if __name__ == '__main__':
    text = PrepareText('lyrics/forgot.md')
    score = ScoreMechanism(text.lyrics_tokenized, text.syllable_dict)
