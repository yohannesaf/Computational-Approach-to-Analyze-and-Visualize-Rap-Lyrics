from PrepareText import PrepareText
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations


text = PrepareText()
text.read_tokenize_file('lyrics/forgot.md')
text.word_aphabet_dict()
text.clean_syllables()

def similarity():
    mat = []
    for w1, w2 in combinations(text.syllable_dict.values(), 2):
        for syl1 in w1:
            for syl2 in w2:
                # score(SOMETHING)
                return mat[syl1][syl2] = 1

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
    test = similarity(), 'check'
    print test

# text = PrepareText()
# text.read_tokenize_file('lyrics/forgot.md')
# text.word_aphabet_dict()
# text.clean_syllables()
#
# cv = CountVectorizer()
# cv_fit = cv.fit_transform(text.aphabet.values())
# print cv_fit.toarray
#
