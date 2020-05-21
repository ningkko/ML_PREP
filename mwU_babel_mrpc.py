import nltk
import scipy.stats as stats
import ast
from ConceptualDependency import Distance, CSV, histogram, Sort
import numpy as np
import pandas as pd


def jaccardDistance(text1, text2):
    # the tokenize function converts a string to a set.
    # def tokenize(self, s):
    #    return s.split(self._string)

    # by definition the jaccard distance calculates unique
    set1 = set(nltk.word_tokenize(text1))
    set2 = set(nltk.word_tokenize(text2))
    return nltk.jaccard_distance(set1, set2)

def main():
    print("Reading file...")
    texts = CSV.read_to_list("data/babel_paraphrases_bert_classifications.tsv", "tsv")
    print("++++++++++++++++++++++++++++++\nReading done")

    # text1, text2 = Distance.getInputs()

    print("Calculating...")

    bert_jaccard_distances = []

    i = 0
    for pairs in texts:
        # progress
        print(i / 186624)

        sent1 = pairs[3]
        sent2 = pairs[4]

        bert_jaccard_distance = Distance.jaccardDistance(sent1, sent2)
        bert_jaccard_distances.append(bert_jaccard_distance)

        i += 1

    output_df = pd.read_excel('data/msr_paraphrase_all.xlsx')
    output_list = output_df.values.tolist()

    mpr_jaccard_distances = []
    for pairs in output_list:
        sent1 = pairs[3]
        sent2 = pairs[4]

        # distances
        mpr_jaccard_distance = jaccardDistance(sent1, sent2)
        mpr_jaccard_distances.append(mpr_jaccard_distance)

    u_statistic_j, pVal_j = stats.mannwhitneyu(bert_jaccard_distances, mpr_jaccard_distances)
    # Print results
    print('J statistics:')
    print(u_statistic_j)

    print('P value:')
    print(pVal_j)

main()