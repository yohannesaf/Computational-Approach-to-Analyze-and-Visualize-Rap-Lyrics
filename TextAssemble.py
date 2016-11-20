from mcl_clustering import mcl
from ScoreMechanism import ScoreMechanism
from collections import OrderedDict, defaultdict
from finnsyll import FinnSyll
import pronouncing as pr
from syllabify.syllabify import syllabify as syl
from hyphen import Hyphenator, dict_info
import pandas as pd
import numpy as np


class TextAssemble(ScoreMechanism):
    '''
    '''

    def __init__(self, filepath):
        # PrepareText.__init__(self, filepath)
        ScoreMechanism.__init__(self, filepath)
        self.M_output = None
        self.clusters = defaultdict()
        self.clustered_syl = OrderedDict()

        self.mcl_cluster()
        self.phone_name_assignment()

    def mcl_cluster(self):
        self.M_output, self.clusters = mcl(self.adjacency_matrix,
                          expand_factor = 7,
                          inflate_factor = 3,
                          max_loop = 1000,
                          mult_factor = 4
                          )

    # print score.phone_syl_col
    def phone_name_assignment(self):
        temp = self.cluster_val_inversion()
        for syl, cl in temp.iteritems():
            self.clustered_syl.update({self.word_syl_col[syl]:cl})

    def cluster_val_inversion(self):
        '''
        Assigns the value to be the key, and cluster for the values.
        nodes assigned to a unique clusters are agregated together
        '''
        temp = defaultdict()
        for cl, syl in self.clusters.iteritems():
            if len(syl) > 1:
                for sound in syl:
                    temp.update({sound:cl})
            else:
                temp.update({syl[0]:99})
        return temp


if __name__ == '__main__':

    text = TextAssemble('lyrics/mini.md')
