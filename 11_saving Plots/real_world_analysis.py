import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 11)  # Days from 1 to 10
# Simulated data for two different metrics
sales_in_cr = np.array([2.5, 3.0, 4.2, 5.1, 6.0, 7.5, 8.0, 9.1, 10.5, 11.0])  # Sales in crores 
plt.figure(figsize=(10,5))
plt.plot(days, sales_in_cr, marker='o', color='b', label='Sales in Crores')
plt.title('Sales Over 10 Days')
plt.xlabel('Days')
plt.ylabel('Sales (in Crores)')

plt.grid(True)
plt.legend() # legend for the plot
plt.savefig('sales_plot.png')  # Save the plot as a PNG file                
plt.show()