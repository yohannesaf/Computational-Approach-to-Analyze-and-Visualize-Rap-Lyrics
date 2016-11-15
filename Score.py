from PrepareText import PrepareText
import pandas as pd
import numpy as np

def prefix_score():
    pass

def suffix_score():
    pass

def vowel_score():
    pass

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
    text = PrepareText()
    text.read_tokenize_file('lyrics/forgot.md')
    text.word_aphabet_dict()
    text.clean_syllables()
