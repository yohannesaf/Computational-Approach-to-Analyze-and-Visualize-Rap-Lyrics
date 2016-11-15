from PrepareText import PrepareText
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations


text = PrepareText()
text.read_tokenize_file('lyrics/forgot.md')
text.word_aphabet_dict()
text.clean_syllables()



def similarity_mat():
    temp = text.syllable_dict.values()
    n = score_size()
    col = []
    row = []
    score = np.zeros((n,n))
    for word1 in text.syllable_dict.values():
        col_ind = 0
        for syl1 in word1:
            col.append(syl1)
            row_ind = 0
            for word2 in temp:
                if word1 != word2:
                    for syl2 in word2:
                        row.append(syl2)
                        score[row_ind][col_ind] = 1
                else:
                    for syl2 in word2:
                        row.append(syl2)
                        score[row_ind][col_ind] = 0
            row_ind += 1
        col_ind +=1
    return score, col, row


def similarity1():
    score = []
    col = []
    row = []
    for w1, w2 in combinations(text.syllable_dict.values(), 2):
        for syl1 in w1:
            col.append(syl1)
            for syl2 in w2:
                row.append(syl2)
                score.append(1)
    return score, col, row

def score_size():
    size = 0
    for word in text.syllable_dict.values():
        size += len(word)

def prefix_score():
    pass

def suffix_score():
    pass

def vowel_score():
    pass

def sound_intersect(phonetic1, phonetic2):
    return list(set(a) & set(b))

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
    score, col, row = similarity1()
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
