import pandas as pd
from ConceptualDependency import CSV

df = pd.read_csv('Jaccard_min.csv')
df = df.drop(['row'], axis=1)
df = df.head(600)
CSV.write_data('Jaccard_min.csv', df.values.tolist())
df.to_csv('Jaccard_min.csv')


df = pd.read_csv('Jaccard_max.csv')
df = df.drop(['row'], axis=1)
CSV.write_data('Jaccard_max.csv', df.values.tolist())
df.to_csv('Jaccard_max.csv')

df = pd.read_csv('Levenshtein_max.csv')
df = df.drop(['row'], axis=1)
CSV.write_data('Levenshtein_max.csv', df.values.tolist())
df.to_csv('Levenshtein_max.csv')

df = pd.read_csv('Levenshtein_min.csv')
df = df.drop(['row'], axis=1)
CSV.write_data('Levenshtein_min.csv', df.values.tolist())
df.to_csv('Levenshtein_min.csv')
