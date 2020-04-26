import pandas as pd

def sort():
    df = pd.read_csv('output.csv')

    df = df.sort_values(['Levenshtein distance'], ascending=[True])
    df.to_csv('Levenshtein_min.csv')

    df = df.sort_values(['Levenshtein distance'], ascending=[False])
    df.to_csv('Levenshtein_max.csv')

    df = df.sort_values(['Jaccard distance'], ascending=[True])
    df.to_csv('Jaccard_min.csv')

    df = df.sort_values(['Jaccard distance'], ascending=[False])
    df.to_csv('Jaccard_max.csv')
