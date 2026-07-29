import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
values = [22, 13, 15, 12]

plt.bar(categories, values, color = "green")
plt.title("Sample Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()