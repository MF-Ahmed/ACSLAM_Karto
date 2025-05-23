import matplotlib.pyplot as plt

# Sample data for two graphs
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 25, 10, 20]

# Calculate the average values for each data point
average_values = [(y1_val + y2_val) / 2 for y1_val, y2_val in zip(y1, y2)]

# Calculate the confidence intervals (if needed)
# Replace the following with your own confidence interval calculations
confidence_interval_lower = [y - 1.96 for y in average_values]
confidence_interval_upper = [y + 1.96 for y in average_values]

# Create the plots for y1 and y2
#plt.plot(x, y1, label='Graph 1', color='b', marker='o', linestyle='-')
#plt.plot(x, y2, label='Graph 2', color='g', marker='s', linestyle='-')

# Create the plot for the average values
plt.plot(x, average_values, label='Average', color='r', linestyle='--', linewidth=2)

# Fill the area between confidence intervals
plt.fill_between(x, confidence_interval_lower, confidence_interval_upper, color='gray', alpha=0.2)

# Set the legend
plt.legend(loc='upper right', fontsize=12)

# Set the title and labels
plt.title('Graphs with Confidence Intervals', fontsize=16)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)

# Show the plot
plt.show()
