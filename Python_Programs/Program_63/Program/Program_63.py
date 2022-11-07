# importing pandas
import pandas as pd

record = {
'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
'Percentage': [88, 92, 95, 70, 65, 78]}

# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print("Given Dataframe :\n", dataframe)

options = ['Math', 'Science']

# selecting rows based on condition
rslt_df = dataframe.loc[(dataframe['Age'] == 21) &
			dataframe['Stream'].isin(options)]

print('\nResult dataframe :\n', rslt_df)