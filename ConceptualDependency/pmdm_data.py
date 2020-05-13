import csv
import scipy.stats as stats
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# calculate histograms for “most_equiv” “least_equiv” and “best_example” columns
output_df = pd.read_csv('../data/Paraphrases McTurk Data May 2020 Processed.csv')
output_list = output_df.values.tolist()

most_equiv = []
least_equiv = []
best_example = []
for line in output_list:
    most_equiv.append(line[19])
    least_equiv.append(line[20])
    best_example.append(line[21])

# histograms
plt.hist(most_equiv, density=True)
plt.title("most_equiv Distribution")
plt.show()
most_equiv_hist = pd.value_counts(most_equiv)
most_equiv_df = pd.DataFrame(most_equiv_hist)
most_equiv_df.to_csv('../pmdm_outputs/most_equiv_histogram', index=False)


plt.hist(least_equiv, density=True)
plt.title("least_equiv Distribution")
plt.show()
least_equiv_hist = pd.value_counts(least_equiv)
least_equiv_df = pd.DataFrame(least_equiv_hist)
least_equiv_df.to_csv('../pmdm_outputs/least_equiv_histogram', index=False)


plt.hist(best_example, density=True)
plt.title("best_example Distribution")
plt.show()

best_example_hist = pd.value_counts(best_example)
best_example_df = pd.DataFrame(best_example_hist)
best_example_df.to_csv('../pmdm_outputs/best_example_histogram', index=False)
