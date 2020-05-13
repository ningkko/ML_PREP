import csv
import scipy.stats as stats
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def jaccardDistance(text1, text2):
    # the tokenize function converts a string to a set.
    # def tokenize(self, s):
    #    return s.split(self._string)

    # by definition the jaccard distance calculates unique
    set1 = set(nltk.word_tokenize(text1))
    set2 = set(nltk.word_tokenize(text2))
    return nltk.jaccard_distance(set1, set2)


def editDistance(text1, text2):
    token1 = nltk.word_tokenize(text1)
    token2 = nltk.word_tokenize(text2)
    return nltk.edit_distance(token1, token2)


output_df = pd.read_excel('../data/msr_paraphrase_all.xlsx')
output_list = output_df.values.tolist()
output_header = list(output_df.columns.values)

edit_distances = []
jaccard_distances = []
qualities = []
index = 0
for pairs in output_list:
    sent1 = pairs[3]
    sent2 = pairs[4]

    # distances
    edit_distance = editDistance(sent1, sent2)
    jaccard_distance = jaccardDistance(sent1, sent2)
    output_list[index].append(edit_distance)
    output_list[index].append(jaccard_distance)

    edit_distances.append(edit_distance)
    jaccard_distances.append(jaccard_distance)
    qualities.append(pairs[0])

    index += 1

with open("../msr_outputs/msr_output.csv", 'w') as file:
    pen = csv.writer(file)
    # header
    pen.writerow(output_header + ['Edit Distance'] + ['Jaccard Distance'])
    for row in output_list:
        pen.writerow(row)

file.close()

# edit histogram
edit_bin_max = np.max(edit_distances)

plt.hist(edit_distances, density=True, bins=edit_bin_max, range=(0, edit_bin_max+1))
plt.title("Edit Distance Distribution")
plt.show()

edit_hist = np.histogram(edit_distances, bins=edit_bin_max, range=(0, edit_bin_max+1))

edit_hist_df = pd.DataFrame(edit_hist)
edit_hist_df.to_csv('../msr_outputs/edit_histogram.csv', index=False)

# jaccard histogram
j_distance_max = np.max(jaccard_distances)
jaccard_bin_max = int(math.ceil(j_distance_max) / 0.05)
plt.hist(jaccard_distances, density=True, bins=jaccard_bin_max)
plt.title("Jaccard Distance Distribution")
plt.show()

jaccard_hist = np.histogram(jaccard_distances, bins=jaccard_bin_max)

jaccard_hist_df = pd.DataFrame(jaccard_hist)
jaccard_hist_df.to_csv('../msr_outputs/jaccard_histogram.csv', index=False)

# mean and medians
edit_median = np.median(edit_distances)
edit_mean = np.mean(edit_distances)

jaccard_median = np.median(jaccard_distances)
jaccard_mean = np.mean(jaccard_distances)

txt = open("../msr_outputs/mean_medians.txt", "w")
txt.write("edit_median: " + str(edit_median) + "\n" +
          "edit_mean: " + str(edit_mean) + "\n" +
          "jaccard_median: " + str(jaccard_median) + "\n" +
          "jaccard_mean: " + str(jaccard_mean))

txt.close()


# mwUtest


u_statistic_j, pVal_j = stats.mannwhitneyu(qualities, jaccard_distances)
# Print results
print('quality vs Jaccard statistics: ')
print(u_statistic_j)

print('P value: ')
print(pVal_j)

u_statistic_e, pVal_e = stats.mannwhitneyu(qualities, edit_distances)
# Print results
print('quality vs Edit statistics: ')
print(u_statistic_e)

print('P value: ')
print(pVal_e)

txt = open("../msr_outputs/MWUtest.txt", "w")
txt.write("quality vs Jaccard statistics: " + str(u_statistic_j) + "\n" +
          "P value: " + str(pVal_j) + "\n" +
          "quality vs Edit statistics: " + str(u_statistic_e) + "\n" +
          "P value: " + str(pVal_e))

txt.close()