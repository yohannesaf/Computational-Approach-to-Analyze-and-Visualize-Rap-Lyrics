from PrepareText import PrepareText
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations
import copy

class ScoreMechanism(PrepareText):
    '''
    Creates a list of columns headers and score matrix
    '''

    def __init__(self, filepath):
        PrepareText.__init__(self, filepath)
        self.adjacency_matrix = []

        self.similarity_mat()


    def similarity_mat(self):
        '''
        Creates a 'score' matrix for each syllables
        '''
        temp_score = self.score_shape()
        row = copy.deepcopy(self.phone_syl_col)
        for ind1, val1 in enumerate(self.phone_syl_col):
            for ind2, val2 in enumerate(row):
                if val1 != val2:
                    common_sound = self.sound_intersect(val1, val2)
                    if len(common_sound) > 1:
                        points = self.final_score(val1, val2, common_sound)
                        temp_score[ind1][ind2] = points
                else:
                    temp_score[ind1][ind2] = 0
        self.adjacency_matrix = temp_score


    def score_shape(self):
        dim = 0
        for word in self.phonetic_syl_dict.itervalues():
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
            return 1.5
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
            return .5
        elif (ind1 > ph1_len.index(max(ph1_len))) and (ind2 > ph2_len.index(max(ph2_len))):
            return .5
        else:
            return 3

    def vowel_score(self, sound):
        '''
        Input: Vowel phone
        Output: Vowel phone score

        Assigns score to a common phone vowel bewteen 2 words based on their stress.
        '''
        if sound[-1] > 0:
            return 2.5
        else:
            return 1.6

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

    score = ScoreMechanism('lyrics/forgot.md')
