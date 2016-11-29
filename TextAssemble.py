from mcl_clustering import mcl
from ScoreMechanism import ScoreMechanism
from collections import OrderedDict, defaultdict
from syllabify.syllabify import syllabify as syl
from hyphen import Hyphenator, dict_info
from colors import color
import random
import copy
import pandas as pd
import numpy as np
import sys

class RapVision(ScoreMechanism):
    '''
    Clusters the syllables into a ryhme families, and prints them with unique color
    for each ryhme groups
    '''

    def __init__(self, filepath):
        ScoreMechanism.__init__(self, filepath)
        self.M_output = None
        self.clusters = defaultdict()
        self.unique_clusters = 0
        self.clustered_syl_dict = defaultdict()
        self.clustered_syl = []
        self.grouped_syl = OrderedDict()
        self.display_syl = []
        self.colored_syl = []
        self.output_text = []

        self.mcl_cluster()
        self.word_name_assignment()
        self.clustered_syl_list()
        self.syl_combine()
        self.lyric_reconstruction()
        self.color_assignment()
        self.print_text()

    def mcl_cluster(self):
        '''
        Computes Marcov Cluster Algorithm
        '''
        self.M_output, self.clusters = mcl(self.adjacency_matrix,
                          expand_factor = 7,
                          inflate_factor = 3,
                          max_loop = 100,
                          mult_factor = 2
                          )

    def word_name_assignment(self):
        '''
        Assigns the word syllables the approprate cluster
        '''
        temp = self.cluster_val_inversion()
        self.unique_clusters = list(set(temp.values()))
        [self.clustered_syl_dict.update({self.word_syl_col[syl]:cl}) for  syl, cl in temp.iteritems()]

    def clustered_syl_list(self):
        for word in self.word_syl_col:
            if word in self.clustered_syl_dict.iterkeys():
                self.clustered_syl.append([word, self.clustered_syl_dict[word]])
            else:
                self.clustered_syl.append([word, 99])


    def cluster_val_inversion(self):
        '''
        Assigns the value to be the key, and cluster for the values.
        nodes assigned to a unique clusters are agregated together
        '''

        temp = defaultdict()
        [temp.update({sound:cl}) if len(syl) > 1 else temp.update({syl[0]:99}) \
            for cl, syl in self.clusters.iteritems() for sound in syl ]
        return temp

    def syl_combine(self):
        '''
        Groups each words syllables together
        '''
        word_ind = 0
        syl_counts = self.word_syl_count()
        for key, syl_len in syl_counts.iteritems():
            temp = self.clustered_syl[word_ind:word_ind+syl_len]
            self.grouped_syl.update({key:temp})
            word_ind += syl_len


    def word_syl_count(self):
        '''
        Returns the syllable counts for each word
        '''
        syl_counts = OrderedDict()
        [syl_counts.update({key:len(val)}) for key, val in self.phonetic_syl_dict.iteritems()]
        return syl_counts


    def lyric_reconstruction(self):
        '''
        Appends non-unique keys back for text print.
        '''
        for line in self.lyrics_tokenized:
            temp = []
            for word in line:
                key = self.append_keys(word)
                temp.append((word, key))
            self.display_syl.append(temp)

    def append_keys(self, word):
        '''
        Appends non-unique keys back for text print.
        '''
        if word in self.grouped_syl.keys():
            return self.grouped_syl[word]
        else:
            return [[word, 99]]

    def color_assignment(self):
        '''
        Assigns unique color for each unique ryhme families
        '''
        color_cl = copy.deepcopy(self.unique_clusters)
        color_cl.pop(color_cl.index(99))
        black = 233
        color_pallets = random.sample(range(230), len(color_cl))

        for line in self.display_syl:
            word_color = []
            for word, syl_cl in line:
                syl_color = []
                for syl, cl in syl_cl:
                    if cl == 99:
                        syl_color.append(color(syl, fg=black))
                    else:
                        index_cl = color_cl.index(cl)
                        syl_color.append(color(syl, fg=color_cl[index_cl]))
                word_color.append([word, syl_color])
            self.colored_syl.append(word_color)


    def print_text(self):
        '''
        Prints color coded lyrics
        '''
        temp_text = []
        for line in self.colored_syl:
            line_text = [''.join(syl_cl) for _, syl_cl in line]
            print ' '.join(line_text)

if __name__ == '__main__':

    text = RapVision('lyrics/nas.md')
