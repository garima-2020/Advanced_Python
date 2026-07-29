import matplotlib.pyplot as plt
import numpy as np  

data = np.random.randn(1000)  # generate 1000 random numbers from a normal distribution
print(data)

plt.hist(data, bins=30, color = "purple", alpha = 0.7, edgecolor = "black") # alpha is the transparency of the bars
plt.title("Sample Histogram")   
plt.xlabel("Value")
plt.ylabel("Frequency") 
plt.show()