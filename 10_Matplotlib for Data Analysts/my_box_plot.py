# used for outlier detection and to visualize the distribution of data

import matplotlib.pyplot as plt
import numpy as np  

data = np.random.randn(1000)  # generate 1000 random numbers from a normal distribution

plt.boxplot(data)
plt.title("Sample Box Plot")
plt.ylabel("Value")
plt.show()