import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample Plot')
plt.savefig('my_plot.png')  # Save the plot as a PNG file
plt.savefig('my_plot.pdf')  # Save the plot as a PDF file
plt.show()