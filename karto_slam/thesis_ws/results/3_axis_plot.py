import numpy as np
import matplotlib.pyplot as plt

# Sample data
simulation_types = ['Type A', 'Type B', 'Type C', 'Type D', 'Type E', 'Type F', 'Type G']  # Types of simulations
subtype_labels = ['Subtype 1', 'Subtype 2', 'Subtype 3']  # Subtypes within each simulation type

# Number of simulations for each subtype and simulation type
num_simulations_subtypes = [
    [30, 40, 50, 60, 70, 80, 90],  # Subtype 1
    [20, 30, 40, 50, 60, 70, 80],  # Subtype 2
    [15, 25, 35, 45, 55, 65, 75]  # Subtype 3

]

# Percentage of map covered for each subtype and simulation type
percentage_map_covered_subtypes = [
    [10, 15, 20, 25, 30, 35, 40],  # Subtype 1
    [15, 20, 25, 30, 35, 40, 45],  # Subtype 2
    [20, 25, 30, 35, 40, 45, 50]  # Subtype 3

]

# Line plot colors for each subtype
line_colors = ['r', 'g', 'b']

# Create figure and axes
fig, ax = plt.subplots()

# Set the number of subtypes
num_subtypes = len(subtype_labels)

# Set the width of the bars
bar_width = 0.2

# X positions for the bars
x = np.arange(len(simulation_types))

# Plot bars for each subtype
for i in range(num_subtypes):
    ax.bar(x + (i - num_subtypes / 2 + 0.5) * bar_width, num_simulations_subtypes[i], bar_width, label=subtype_labels[i])

# Set x-axis ticks and labels
plt.xticks(x, simulation_types, rotation=45, ha='right')

# Set y-axis label for number of simulations
ax.set_ylabel('Number of Simulations')

# Create a twin Axes for the line plot with its own y-axis
ax2 = ax.twinx()

# Plot line plots for percentage of map covered for each subtype
for i in range(num_subtypes):
    ax2.plot(x + (i - num_subtypes / 2 + 0.5) * bar_width, percentage_map_covered_subtypes[i], linestyle='-', marker='o', color=line_colors[i], label=f'Percentage of Map Covered ({subtype_labels[i]})')

# Set y-axis label for percentage of map covered
ax2.set_ylabel('Percentage of Map Covered (%)')

# Combine legends
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='upper right')

# Set title
plt.title('Simulations and Map Coverage')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
