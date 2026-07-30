import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips') 
print(df.head())
sns.boxplot(data=df, x='day', y='total_bill')
plt.show()

# the middle line shows the median of the data, the box shows the interquartile range (IQR), and the whiskers show the range of the data. The points outside the whiskers are considered outliers. The boxplot is a great way to visualize the distribution of the data and to identify any outliers in the data.