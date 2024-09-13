import matplotlib.pyplot as plt
import numpy as np

# Sample data
main_fields = ['Field 1', 'Field 2', 'Field 3']
sub_fields = ['Subfield 1', 'Subfield 2', 'Subfield 3']
percentages = np.random.randint(0, 100, size=(3, 3))  # Random percentages for illustration

# Define colors for each subfield
colors = ['red', 'blue', 'green']

# Set bar height
bar_height = 0.25

# Create figure and axes
fig, ax = plt.subplots()

# Create bars for each subfield
for i, main_field in enumerate(main_fields):
    for j, sub_field in enumerate(sub_fields):
        ax.barh(i + j * bar_height, percentages[i][j], bar_height, label=sub_field, color=colors[j])

# Set labels and title
ax.set_ylabel('Main Fields')
ax.set_xlabel('Percentage of Map Discovered')
ax.set_title('Map Discovery by Main and Sub Fields')
ax.set_yticks(np.arange(len(main_fields)) + bar_height / 2)
ax.set_yticklabels(main_fields)
ax.legend()

# Show plot
plt.show()
