# %%
import pandas as pd
from random import shuffle

incident_df = pd.read_csv('../filtered_data/Filtered_Incident_Report2.csv')

# Population and Population density
population_df = pd.read_csv('../filtered_data/nbr_population.csv')
nbr_incident_df = incident_df['neighborhood_adjusted'].value_counts().to_frame().reset_index()
nbr_incident_df.columns = ['neighborhood', 'theft_count']
# %%
def permutation_test(series1, series2, no_iter=1000):
    r = series1.corr(series2)
    count = 1
    for _ in range(no_iter-1):
        shuffle(series2)
        if series1.corr(series2) >= r:
            count += 1
    pval = count/no_iter
    return r, pval

# %%
merged_df = nbr_incident_df.merge(population_df)
r, pval = permutation_test(merged_df['theft_count'], merged_df['population'])
print('Correlation b/w neighborhood population and vehicle theft count:')
print('Pearson r: {:.2f}'.format(r))
print('Empirical p-val: {:.4f}'.format(pval))
# %%
'''
merged_df = nbr_incident_df.merge(population_df)...
Correlation b/w neighborhood population and vehicle theft count:
Pearson r: 0.68
Empirical p-val: 0.0001
'''
