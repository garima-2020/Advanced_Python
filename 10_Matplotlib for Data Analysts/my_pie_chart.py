import matplotlib.pyplot as plt
import numpy as np  

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

# plt.style.use('ggplot2')  # set the style of the plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'orange'])
# autopct is used to display the percentage of each slice
# "%d%%" means display the percentage with 1 decimal place
plt.title("Sample Pie Chart")   
plt.show()

