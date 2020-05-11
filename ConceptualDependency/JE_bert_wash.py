import pandas as pd

# means of Jaccard distance(Bert == 1)
# means of Jaccard distance(Bert == 0)

df = pd.read_csv('../babel_outputs/output_with_berts.csv')

jaccard_bert0 = []
jaccard_bert1 = []
edit_bert0 = []
edit_bert1 = []

lenth = 432*432
i = 0

for index, row in df.iterrows():
    if int(row['Bert']) == 0:
        jaccard_bert0.append(row['Jaccard distance'])
        edit_bert0.append(row['Levenshtein distance'])

    elif int(row['Bert']) == 1:
        jaccard_bert1.append(row['Jaccard distance'])
        edit_bert1.append(row['Levenshtein distance'])
    i += 1
    print(i/lenth)
'''    if i >=500:
        break'''

print("writing...")
# write to result
with open("../babel_outputs/mwUtest_data/J_bert0.txt", "w") as txt:
    txt.write(str(jaccard_bert0))
txt.close()
with open("../babel_outputs/mwUtest_data/J_bert1.txt", "w") as txt:
    txt.write(str(jaccard_bert1))
txt.close()
with open("../babel_outputs/mwUtest_data/E_bert0.txt", "w") as txt:
    txt.write(str(edit_bert0))
txt.close()
with open("../babel_outputs/mwUtest_data/E_bert1.txt", "w") as txt:
    txt.write(str(edit_bert1))
txt.close()

print("Writing done")

