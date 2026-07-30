import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('tips') #load_dataset means load the dataset from seaborn library. The dataset is called 'tips' which contains data about restaurant tips, their amounts, and other attributes.it can be anything like iris, tips, etc.
print(df.head())
sns.lineplot(data=df, x='size', y='tip', hue='sex')
plt.show() 