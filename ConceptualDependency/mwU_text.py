import scipy.stats as stats
import ast

j0 = []
with open('../outputs/mwUtest_data/J_bert0.txt') as file:
    j0 = file.read()
    j0 = ast.literal_eval(j0)
file.close()

j1 = []
with open('../outputs/mwUtest_data/J_bert1.txt') as file:
    j1 = file.read()
    j1 = ast.literal_eval(j1)
file.close()

# Calculate u and probability of a difference

u_statistic_j, pVal_j = stats.mannwhitneyu(j0, j1)

# Print results
print('J statistics:')
print(u_statistic_j)

print('P value:')
print(pVal_j)
