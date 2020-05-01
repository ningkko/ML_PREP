import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def edit_hist():
    df = pd.read_csv('outputs/output.csv')
    data = df["Levenshtein distance"].tolist()
    # buckets = edit distances
    bin_max = np.max(data)

    plt.hist(data, density=True, bins=bin_max)
    plt.title("Edit Distance Distribution")
    plt.show()
    return np.histogram(data, bins=bin_max)


def jaccard_hist():
    df = pd.read_csv('outputs/output.csv')
    data = df["Jaccard distance"].tolist()

    # buckets = 0.05
    bin_max = math.ceil(np.max(data) / 0.05)

    plt.hist(data, density=True, bins=bin_max)
    plt.title("Jaccard Distance Distribution")
    plt.show()

    return np.histogram(data, bins=bin_max)
