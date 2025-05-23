import matplotlib.pyplot as plt

# Sample data for two graphs
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 25, 10, 20]

# Calculate the average values for each data point
average_values = [(y1_val + y2_val) / 2 for y1_val, y2_val in zip(y1, y2)]

# Create the plots for y1 and y2
plt.figure(figsize=(8, 6))  # Set the figure size
plt.plot(x, y1, label='Graph 1', color='b', marker='o', linestyle='-')
plt.plot(x, y2, label='Graph 2', color='g', marker='s', linestyle='-')

# Create the plot for the average values
plt.plot(x, average_values, label='Average', color='r', linestyle='--', linewidth=2)

# Set grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Set the background color
plt.gca().set_facecolor('#f7f7f7')

# Set the legend
plt.legend(loc='upper right', fontsize=12)

# Set the title and labels
plt.title('Graphs and Average Values', fontsize=16)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)

# Set the font size for tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Show the plot
plt.show()
