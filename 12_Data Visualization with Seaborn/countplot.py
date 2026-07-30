import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips') 
print(df.head())
sns.countplot(data=df, x='day', hue='sex')
plt.show()