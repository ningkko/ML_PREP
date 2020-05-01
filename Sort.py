import pandas as pd


def sort():
    df = pd.read_csv('outputs/output.csv')

    df = df.sort_values(['Levenshtein distance'], ascending=[True])
    df.to_csv('outputs/Levenshtein_min.csv', index=False)

    df = df.sort_values(['Levenshtein distance'], ascending=[False])
    df.to_csv('outputs/Levenshtein_max.csv', index=False)

    df = df.sort_values(['Jaccard distance'], ascending=[True])
    df.to_csv('outputs/Jaccard_min.csv', index=False)

    df = df.sort_values(['Jaccard distance'], ascending=[False])
    df.to_csv('outputs/accard_max.csv', index=False)
