from PrepareText import PrepareText
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations
import copy

text = PrepareText()
text.read_tokenize_file('lyrics/mini.md')
text.word_aphabet_dict()
text.clean_syllables()

def similarity_mat():
    syllable_dict = text.syllable_dict
    syl_list1 = syllable_list(syllable_dict)
    syl_list2 = copy.deepcopy(syl_list1)
    score = score_size(syllable_dict)
    for ind1, val1 in enumerate(syl_list1):
        for ind2, val2 in enumerate(syl_list2):
            if val1 != val2:
                common_sound = sound_intersect(val1, val2)
                if len(common_sound) > 0:
                    points = final_score(val1, val2, common_sound)
                    score[ind1][ind2] = points
                else:
                    score[ind1][ind2] = 0
            else:
                score[ind1][ind2] = np.nan
    return score, syl_list1

# Update the input function
def syllable_list(syllable_dict):
    '''
    Input: syllable dictionary with value
    Output: A list which consists all the syllables

    Unpacks the values into a single list
    '''
    syllable_dict = text.syllable_dict # UPDATE
    syl_list = []
    for val in syllable_dict.itervalues():
        syl_list.extend(val)
    return syl_list

def score_size(syllable_dict):
    dim = 0
    for word in syllable_dict.itervalues():
        dim += len(word)
    return np.zeros((dim,dim))


def final_score(phonetic1, phonetic2, common_sounds):
    '''
    Input: 2 phonetic and list of common sounds between two phonetics
    Output: Score based on phonetic sound

    Calculates score for the common sounds
    '''
    points = 0
    for sound in common_sounds:
        if len(sound) > 1:
            points += vowel_score(sound)
        else:
            points += consonant_score(phonetic1, phonetic2, sound)
    return points


def consonant_score(phonetic1, phonetic2, sound):
    '''
    Input: Consonant phone
    Output: Consonant phone score

    Assigns consonant phone score based on whether it is prefix or suffix
    '''
    sound_pos = prefix_check(phonetic1, phonetic2, sound)
    if sound_pos == 1:
        return 1
    elif sound_pos == 2:
        return 2.5
    else:
        return 0

def prefix_check(phonetic1, phonetic2, sound):
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
    elif (ind1 > ph2_len.index(max(ph1_len))) and (ind2 > ph2_len.index(max(ph2_len))):
        return 2
    else:
        return 0

def vowel_score(sound):
    '''
    Input: Vowel phone
    Output: Vowel phone score

    Assigns score to a common phone vowel bewteen 2 words based on their stress.
    '''
    if sound[-1] > 0:
        return len(sound) * 3
    else:
        return len(sound) + 2

def sound_intersect(phonetic1, phonetic2):
    '''
    Input: Two phonetic to be compared
    Output: sound found in both phonetic

    Find common sounds in the two phonetics
    '''
    return list(set(phonetic1) & set(phonetic2))

def is_vowel(text):
    '''
    Returns true if a character is a vowel
    '''
    vowels = 'aeiouAEIOU'
    return [True if char in vowels else False for char in text]

def is_num(char = 'x'):
    '''
    Returns true if a character is a number
    '''
    return char.isdigit()



if __name__ == '__main__':
    score, col = similarity_mat()
    print score

# text = PrepareText()
# text.read_tokenize_file('lyrics/forgot.md')
# text.word_aphabet_dict()
# text.clean_syllables()
#
# cv = CountVectorizer()
# cv_fit = cv.fit_transform(text.aphabet.values())
# print cv_fit.toarray
#
