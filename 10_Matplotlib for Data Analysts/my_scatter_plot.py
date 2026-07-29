import matplotlib.pyplot as plt
import numpy as np  

x = [1, 2, 3, 4, 5]
y = [22, 13, 15, 12, 11]

plt.scatter(x, y, s=100, color = "blue", marker = "o",alpha = 0.5)  # s is the size of the point
# alpha is the transparency of the point
plt.title("Sample Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()