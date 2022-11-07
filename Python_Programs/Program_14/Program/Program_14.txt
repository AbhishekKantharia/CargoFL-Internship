# Import pandas module using the import keyword
import pandas as pd
# Import pyplot from matplotlib module using the import keyword
from matplotlib import pyplot as pplot
# Import seaborn module using the import keyword
import seaborn as sns
# Pass some random CSV file to the read_csv() function of the pandas module 
# to read the given csv file
gvn_datafrme = pd.read_csv("demo.csv")
# Display the first 5 rows of the given csv file using the head() function
gvn_datafrme.head()
# Passing some random plot size(width, length) to the figure() function
pplot.figure(figsize=(10, 4))
pplot.subplot(1, 2, 1)
# Plot the graph of id, Salary columns in a given CSV file using the countplot() function
# of the seaborn module
sns.countplot('id', hue='Salary', data= gvn_datafrme)
# Plot the subplot by passing the arguments rows, columns and order of the plot to the 
# subplot() function
pplot.subplot(1, 2, 2)
# Plot the graph of id, Tax columns in a given CSV file using the countplot() function
# of the seaborn module
# Here we are plotting multiple plots in a single PDF file.
sns.countplot('id', hue='Tax', data= gvn_datafrme)
# Save the plots in a single PDF file by passing some random name to the savefig() function
pplot.savefig('Output.pdf')