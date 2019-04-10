# 15-1 Cubes

import matplotlib.pyplot as plt

x_values = list(range(5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=40)

# Set chart title and label axes
plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axis
plt.axis([1, 5000, 0, 125_000_000_000])

plt.show()
