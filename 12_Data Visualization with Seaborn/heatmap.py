# heat map plots the values

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips') 
print(df.corr(numeric_only=True)) #corr is a function in pandas library that is used to calculate the correlation between the columns of the dataset. The numeric_only parameter is used to specify whether to include only numeric columns in the correlation calculation. The correlation is a measure of the linear relationship between two variables. It ranges from -1 to 1, where -1 indicates a perfect negative correlation, 0 indicates no correlation, and 1 indicates a perfect positive correlation.
sns.heatmap(df.corr(numeric_only=True), annot=True) # The annot parameter is used to specify the values inside the cells. The cmap parameter is used to specify the color map to be used for the plot.
plt.show()