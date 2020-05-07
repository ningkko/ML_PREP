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


# ============== Edit Distance ============================

e0 = []
with open('../outputs/mwUtest_data/E_bert0.txt') as file:
    e0 = file.read()
    e0 = ast.literal_eval(e0)
file.close()

e1 = []
with open('../outputs/mwUtest_data/E_bert1.txt') as file:
    e1 = file.read()
    e1 = ast.literal_eval(e1)
file.close()

# Calculate u and probability of a difference

u_statistic_e, pVal_e = stats.mannwhitneyu(e0, e1)

# Print results
print('E statistics:')
print(u_statistic_e)

print('P value:')
print(pVal_e)