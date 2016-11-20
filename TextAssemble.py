from mcl_clustering import mcl
from ScoreMechanism import ScoreMechanism
from collections import OrderedDict, defaultdict
from finnsyll import FinnSyll
import pronouncing as pr
from syllabify.syllabify import syllabify as syl
from hyphen import Hyphenator, dict_info
import pandas as pd
import numpy as np

score = ScoreMechanism('lyrics/text.md')


M_output, clusters = mcl(score.adjacency_matrix,
                  expand_factor = 7,
                  inflate_factor = 3,
                  max_loop = 1000,
               #  mult_factor = <mult_factor>
                  )

# print score.phone_syl_col
def node_name_assignment(clusters):
    syllable_clusters = OrderedDict()
    for syl, cl in clusters.iteritems():
        syllable_clusters.update({tuple(score.phone_syl_col[syl]):cl})
    return syllable_clusters

def cluster_val_inversion(clusters):
    '''
    Assigns the value to be the key, and cluster for the values.
    nodes assigned to a unique clusters are agregated together
    '''
    temp = defaultdict()
    for cl, syl in clusters.iteritems():
        if len(syl) > 1:
            for sound in syl:
                temp.update({sound:cl})
        else:
            temp.update({syl[0]:99})
    return temp


test1 = cluster_val_inversion(clusters)
test2 = node_name_assignment(test1)
