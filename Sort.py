import pandas as pd

df = pd.read_csv('output.csv')

df = df.sort_values(['Levenshtein distance'], ascending=[True])
df.to_csv('Levenshtein_min.csv')
