# line plot example

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [22, 13, 15, 12, 11]

plt.plot(x, y, color = "red", marker = "o", linestyle = "dashed", linewidth = 2, markersize = 12)  # marker = o means the point will be o
plt.title("Sample Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()