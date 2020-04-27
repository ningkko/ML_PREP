import pandas as pd
import CSV

df = pd.read_csv('Jaccard_min.csv')
df = df.drop(['row'], axis=1)
df = df.head(600)
CSV.write('Jaccard_min.csv', df.values.tolist())
df.to_csv('Jaccard_min.csv')


df = pd.read_csv('Jaccard_max.csv')
df = df.drop(['row'], axis=1)
CSV.write('Jaccard_max.csv', df.values.tolist())
df.to_csv('Jaccard_max.csv')

df = pd.read_csv('Levenshtein_max.csv')
df = df.drop(['row'], axis=1)
CSV.write('Levenshtein_max.csv', df.values.tolist())
df.to_csv('Levenshtein_max.csv')

df = pd.read_csv('Levenshtein_min.csv')
df = df.drop(['row'], axis=1)
CSV.write('Levenshtein_min.csv', df.values.tolist())
df.to_csv('Levenshtein_min.csv')
