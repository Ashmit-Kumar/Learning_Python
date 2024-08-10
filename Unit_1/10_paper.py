import matplotlib.pyplot as plt
import numpy as np

# Define the function y = 10x + 14
def linear_function(x):
    return 10 * x + 14

# Generate x values
x = np.linspace(-10, 10, 400) # Generates 400 points between -10 and 10

# Compute y values
y = linear_function(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 10x + 14', color='blue')

# Add title and labels
plt.title('Plot of the Linear Function y = 10x + 14')
plt.xlabel('x')
plt.ylabel('y')

# Add a grid
plt.grid()

# Add a legend
plt.legend()

# Display the plot
plt.show()
