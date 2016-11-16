from PrepareText import PrepareText
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations
import copy


text = PrepareText()
text.read_tokenize_file('lyrics/forgot.md')
text.word_aphabet_dict()
text.clean_syllables()

# def similarity_mat():
#     temp = text.syllable_dict.values()
#     n = score_size()
#     col = []
#     row = []
#     score = np.zeros((n,n))
#     print score.shape
#     for word1 in text.syllable_dict.values():
#         col_ind = 0
#         for syl1 in word1:
#             col.append(syl1)
#             row_ind = 0
#             for word2 in temp:
#                 if word1 != word2:
#                     for syl2 in word2:
#                         row.append(syl2)
#                         score[row_ind][col_ind] = 1
#                 else:
#                     for syl2 in word2:
#                         row.append(syl2)
#                         score[row_ind][col_ind] = 0
#             row_ind += 1
#         col_ind +=1
#     return score, col, row

def similarity_mat():
    syl_list1 = syllable_list()
    syl_list2 = copy.deepcopy(syl_list1)
    score = score_size()
    for ind1, val1 in enumerate(syl_list1):
        for ind2, val2 in enumerate(syl_list2):
            if val1 != val2:
                common_sound = sound_intersect(val1, val2)
                if len(common_sound) > 0:
                    # points = final_score(val1, val2, common_sound)
                    score[ind1][ind2] = 1
                else:
                    score[ind1][ind2] = 0
            else:
                score[ind1][ind2] = -1
    return score, syl_list1

def syllable_list():
    syl_list = []
    for val in text.syllable_dict.itervalues():
        syl_list.extend(val)
    return syl_list

def score_size():
    size = 0
    for word in text.syllable_dict.values():
        size += len(word)
    return np.zeros((size,size))

# CONTINUE FROM HERE
def final_score(phonetic1, phonetic2, common_sounds):
    points = 0
    for sound in common_sounds:
        if len(sound) > 1:
            points += vowel_score(sound)
        else:
            ind1 = phonetic1.index(sound)
            ind2 = phonetic2.index(sound)
            if (ind1 == ind2) and :
                prefix = prefix_score()

def consonant_score():
    '''
    Input: Consonant phone
    Output: Consonant phone score

    Assigns consonant phone score based on whether it is prefix or suffix
    '''
    pass

def vowel_score(sound):
    '''
    Input: Vowel phone
    Output: Vowel phone score

    Assigns score to a common phone vowel bewteen 2 words based on their stress.
    '''
    if syllable[-1] > 0:
        return len(syllable) * 3
    else:
        return len(syllable) + 2

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
    return [True if char in vowels for char in text]

def is_num(char = 'x'):
    '''
    Returns true if a character is a number
    '''
    return char.isdigit()

# def similarity1():
#     score = []
#     col = []
#     row = []
#     for w1, w2 in combinations(text.syllable_dict.values(), 2):
#         for syl1 in w1:
#             col.append(syl1)
#             for syl2 in w2:
#                 row.append(syl2)
#                 print syl1, syl2
#                 score.append(1)
#     return score, col, row



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
