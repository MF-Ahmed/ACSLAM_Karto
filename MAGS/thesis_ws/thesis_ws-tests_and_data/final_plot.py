import numpy as np
import matplotlib.pyplot as plt
import os
import ptitprince as pt
import seaborn as sns

# Define the directory where the data files are located
file_path = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(file_path, 'data_to_plot')

# Get a list of all the data files in the directory and sort them based on the simulation number
data_files = sorted([file for file in os.listdir(data_directory) if file.startswith('data-simulation')], key=lambda x: int(x.split("_")[1]))

# Initialize lists to store the data from each simulation
merged_x_list = []
merged_y_list = []
generated_map_area_list = []
cpu_time_list = []
cpu_percentages_list = []
gpu_time_list = []
gpu_percentages_list = []
gpu_memory_list = []
num_robots_list = []
num_goals_list = []
total_num_points_list = []
actual_num_points_list = []
radius_values_list = []
percentage_values_list = []

num_simulations = 0

# Iterate over the data files
for file in data_files:

    num_simulations += 1
    # Load the data from the file
    data = np.load(os.path.join(data_directory, file), allow_pickle=True).item()

    # Extract the required data from the simulation
    merged_x = data['merged_x']
    merged_y = data['merged_y']
    generated_map_area = data['generated_map_area']
    cpu_time = data['cpu_time']
    cpu_percentages = data['cpu_percentages']
    gpu_time = data['gpu_time']
    gpu_percentages = data['gpu_percentages']
    gpu_memory = data['gpu_memory']
    num_goals = data['num_goals']
    total_num_points = data['total_num_points']
    actual_num_points = data['actual_num_points']
    radius_values = data['radius_values']
    percentage_values = data['percentage_values']

    # Extract the number of robots from the file name
    num_robots = int(file.split('_')[2].split('.')[0])
    num_robots_list.append(num_robots)

    # Append the data to the respective lists
    merged_x_list.append(merged_x)
    merged_y_list.append(merged_y)
    generated_map_area_list.append(generated_map_area)
    cpu_time_list.append(cpu_time)
    cpu_percentages_list.append(cpu_percentages)
    gpu_time_list.append(gpu_time)
    gpu_percentages_list.append(gpu_percentages)
    gpu_memory_list.append(gpu_memory)
    num_goals_list.append(num_goals)
    total_num_points_list.append(total_num_points)
    actual_num_points_list.append(actual_num_points)
    radius_values_list.append(radius_values)
    percentage_values_list.append(percentage_values)

################################## MAP OCCUPATION ##################################
# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

# Plot the merged map occupation over time for each simulation
for i in range(num_simulations):
    _simulation_number = int(data_files[i].split("_")[1])
    plt.plot(np.array(merged_x_list[i]) - merged_x_list[i][0], (merged_y_list[i] / generated_map_area_list[i]) * 100,
             label=f'Simulation {_simulation_number} - {num_robots_list[i]} Robots')

plt.xlabel('Time [s]')
plt.ylabel('Percentage map discovered')
plt.legend()
plt.title('Merged map occupation over time')
plt.grid(True)

# Since the plot concern a percentage the graph will be from 0 to 100
plt.ylim(0, 100)
#plt.xlim(0, 1200)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()

################################## NUM POINTS USED ##################################
# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

# Create a colormap with a sufficient number of distinct colors
colormap = plt.cm.get_cmap('tab10', num_simulations)

# Plot total and actual points with assigned colors
for i, (goals, total_points) in enumerate(zip(num_goals_list, total_num_points_list)):
    _simulation_number = int(data_files[i].split("_")[1])
    color = colormap(i)  # Get color from the colormap based on the simulation index
    plt.scatter(goals, total_points, marker='.', linewidths=10,
                label=f'Simulation {_simulation_number} - Total Number of Points Detected',
                color=color)
    plt.scatter(goals, actual_num_points_list[i], marker='+', linewidths=10,
                label=f'Simulation {_simulation_number} - Actual Number of Points Used',
                color=color)
plt.xlabel('Number of goals')
plt.ylabel('Number of points')
plt.yticks(range(0, np.max([np.max(y) for y in total_num_points_list])+1, 1))
plt.legend()
plt.title('Total and Actual number of points used')
plt.grid(True)

# Min and max for plot
min_y = np.min([np.min(y) for y in actual_num_points_list])  # Minimum value over all simulations
max_y = np.max([np.max(y) for y in total_num_points_list])  # Maximum value over all simulations

plt.ylim(min_y - 0.5, max_y + 0.5)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()

plt.figure(figsize=(16, 9))

# Lists to store data for box plots
total_points_data = []
actual_points_data = []
num_robots_list = []

# Process data to prepare for box plots
for i, (_, total_points) in enumerate(zip(num_goals_list, total_num_points_list)):
    # Append data to the corresponding lists for box plots
    total_points_data.append(total_points)
    actual_points_data.append(actual_num_points_list[i])

    # Extract the number of robots from the file name
    num_robots = int(data_files[i].split("_")[2])
    num_robots_list.append(num_robots)

# Create box plots with consistent styles for each simulation

boxprops = dict(linewidth=2, color='black')  # Style for the box outline
whiskerprops = dict(linewidth=2, color='black')  # Style for the whiskers
medianprops = dict(linewidth=2, color='red')  # Style for the median line

# Calculate the x-axis positions for the boxes
x_positions_total = np.arange(1, len(total_points_data) * 4 + 1, 4)
x_positions_actual = np.arange(2, len(actual_points_data) * 4 + 2, 4)

# Create the box plots and get the artists
total_boxes = plt.boxplot(total_points_data, positions=x_positions_total,
                         patch_artist=True, boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops)

actual_boxes = plt.boxplot(actual_points_data, positions=x_positions_actual,
                          patch_artist=True, boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops)

# Set the colors of the box plots
for box in total_boxes['boxes']:
    box.set_facecolor('lightblue')
for box in actual_boxes['boxes']:
    box.set_facecolor('lightgreen')

# Set the labels for the x-axis based on the simulation number and number of robots
x_labels = []
for i, num_robots in enumerate(num_robots_list):
    simulation_label = f'Simulation {int(data_files[i].split("_")[1])}'
    x_labels.append(f'{simulation_label}\n({num_robots} Robots)')

mean_line = plt.Line2D([], [], color='red', marker='', linestyle='-', markersize=0, label='Mean Value')
plt.xticks(np.mean([x_positions_total, x_positions_actual], axis=0), x_labels)

# Create custom artists for the legend
total_patch = plt.Line2D([], [], color='lightblue', marker='o', markersize=10, label='Total Number of Points Detected')
actual_patch = plt.Line2D([], [], color='lightgreen', marker='o', markersize=10, label='Actual Number of Points Used')

# Set the legend with the custom artists and mean line
plt.legend(handles=[total_patch, actual_patch, mean_line])

plt.xlabel('Simulations')
plt.ylabel('Number of points')
plt.title('Box plots for Total and Actual number of points used')
plt.grid(True)

# Show the plot
plt.show()

################################## RADIUS VALUES USED ##################################
# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

plt.hlines(1.0, xmin=num_goals[0], xmax=num_goals[-1], color='r', label='First value of radius')
for i, (goals, radius_values) in enumerate(zip(num_goals_list, radius_values_list)):
    _simulation_number = int(data_files[i].split("_")[1])
    plt.scatter(goals, radius_values, marker='x', s=50,
                   label=f'Simulation {_simulation_number} - Radius Values')

plt.xlabel('Number of goals')
plt.ylabel('Radius Values')
plt.legend()
plt.title('Radius Values Used')
plt.grid(True)

# Min and max for plot
min_y = np.min([np.min(y) for y in radius_values])  # Minimum value over all simulations
max_y = np.max([np.max(y) for y in radius_values])  # Maximum value over all simulations

plt.ylim(min_y - 0.25, max_y + 0.25)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()

plt.figure(figsize=(16, 9))

# Lists to store data for violin plots
radius_values_data = []
num_robots_list = []

# Process data to prepare for violin plots
for i, (_, radius_values) in enumerate(zip(num_goals_list, radius_values_list)):
    # Append data to the corresponding lists for violin plots
    radius_values_data.append(radius_values)

    # Extract the number of robots from the file name
    num_robots = int(data_files[i].split("_")[2])
    num_robots_list.append(num_robots)

# Calculate the x-axis positions for the violin plots
x_positions = np.arange(1, len(radius_values_data) * 2 + 1, 2)

# Create the violin plots and get the artists
violins = []
for i, radius_values in enumerate(radius_values_data):
    violin = plt.violinplot(radius_values, positions=[x_positions[i]], showmedians=True)
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians'):
        vp = violin[partname]
        vp.set_edgecolor('black')
        vp.set_linewidth(1.5)
    for pc in violin['bodies']:
        pc.set_facecolor(plt.cm.tab10(i))
        pc.set_edgecolor('black')
        pc.set_alpha(0.7)
    violins.append(violin)

# Set the labels for the x-axis based on the simulation number and number of robots
x_labels = []
for i, num_robots in enumerate(num_robots_list):
    simulation_label = f'Simulation {int(data_files[i].split("_")[1])}'
    x_labels.append(f'{simulation_label}\n({num_robots} Robots)')

plt.xticks(x_positions, x_labels, rotation=45, ha='right')

plt.xlabel('Simulations')
plt.ylabel('Radius Values')
plt.title('Radius Values Used')
plt.grid(True)

# Create custom artists for the legend
legend_elements = [plt.Line2D([], [], marker='o', color='w', markerfacecolor=plt.cm.tab10(i),
                              markersize=10, label=f'Simulation {int(data_files[i].split("_")[1])}')
                   for i in range(len(radius_values_data))]

# Set the legend with the custom artists
plt.legend(handles=legend_elements)

# Show the plot
plt.tight_layout()
plt.show()

# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

# Process data to prepare for line plot
for i, (goals, radius_values) in enumerate(zip(num_goals_list, radius_values_list)):
    _simulation_number = int(data_files[i].split("_")[1])
    plt.plot(goals, radius_values, marker='x', label=f'Simulation {_simulation_number}')

plt.xlabel('Number of goals')
plt.ylabel('Radius Values')
plt.legend()
plt.title('Radius Values Used')
plt.grid(True)

# Min and max for plot
min_y = np.min([np.min(y) for y in radius_values_list])  # Minimum value over all simulations
max_y = np.max([np.max(y) for y in radius_values_list])  # Maximum value over all simulations

plt.ylim(min_y - 0.25, max_y + 0.25)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()
################################## PERCENTAGE VALUES USED ##################################
# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

plt.hlines(60.0, xmin=num_goals[0], xmax=num_goals[-1], color='r', label='First value of radius')
for i, (goals, percentage_values) in enumerate(zip(num_goals_list, percentage_values_list)):
    _simulation_number = int(data_files[i].split("_")[1])
    plt.scatter(goals, percentage_values, marker='x', s=50,
                   label=f'Simulation {_simulation_number} - Percentage Values')

plt.xlabel('Number of goals')
plt.ylabel('Percentage Values')
plt.legend()
plt.title('Percentage Values Used')
plt.grid(True)

# Min and max for plot
min_y = np.min([np.min(y) for y in percentage_values])  # Minimum value over all simulations
max_y = np.max([np.max(y) for y in percentage_values])  # Maximum value over all simulations

plt.ylim(min_y - 0.5, max_y + 0.5)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()

plt.figure(figsize=(16, 9))

# Lists to store data for violin plots
percentage_values_data = []
num_robots_list = []

# Process data to prepare for violin plots
for i, (_, percentage_values) in enumerate(zip(num_goals_list, percentage_values_list)):
    # Append data to the corresponding lists for violin plots
    percentage_values_data.append(percentage_values)

    # Extract the number of robots from the file name
    num_robots = int(data_files[i].split("_")[2])
    num_robots_list.append(num_robots)

# Calculate the x-axis positions for the violin plots
x_positions = np.arange(1, len(percentage_values_data) * 2 + 1, 2)

# Create the violin plots and get the artists
violins = []
for i, percentage_values in enumerate(percentage_values_data):
    violin = plt.violinplot(percentage_values, positions=[x_positions[i]], showmedians=True)
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians'):
        vp = violin[partname]
        vp.set_edgecolor('black')
        vp.set_linewidth(1.5)
    for pc in violin['bodies']:
        pc.set_facecolor(plt.cm.tab10(i))
        pc.set_edgecolor('black')
        pc.set_alpha(0.7)
    violins.append(violin)

# Set the labels for the x-axis based on the simulation number and number of robots
x_labels = []
for i, num_robots in enumerate(num_robots_list):
    simulation_label = f'Simulation {int(data_files[i].split("_")[1])}'
    x_labels.append(f'{simulation_label}\n({num_robots} Robots)')

plt.xticks(x_positions, x_labels, rotation=45, ha='right')

plt.xlabel('Simulations')
plt.ylabel('Percentage Values')
plt.title('Percentage Values Used')
plt.grid(True)

# Create custom artists for the legend
legend_elements = [plt.Line2D([], [], marker='o', color='w', markerfacecolor=plt.cm.tab10(i),
                              markersize=10, label=f'Simulation {int(data_files[i].split("_")[1])}')
                   for i in range(len(percentage_values_data))]

# Set the legend with the custom artists
plt.legend(handles=legend_elements)

# Show the plot
plt.tight_layout()
plt.show()


# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

# Process data to prepare for grouped bar chart
percentage_values_data = np.array(percentage_values_list)
num_simulations = len(percentage_values_data)

# Calculate the width for each bar group
bar_width = 0.2
bar_positions = np.arange(len(percentage_values_data[0]))

# Create the grouped bar chart for each simulation
for i in range(num_simulations):
    offset = (i - (num_simulations - 1) / 2) * bar_width
    plt.bar(bar_positions + offset, percentage_values_data[i], width=bar_width,
            label=f'Simulation {i + 1}')

plt.xlabel('Number of goals')
plt.ylabel('Percentage Values')
plt.legend()
plt.title('Percentage Values Used')
plt.grid(True)

# Min and max for plot
min_y = 0
max_y = 100

plt.ylim(min_y, max_y)
plt.xticks(bar_positions, num_goals_list)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()

################################## CPU USAGE ##################################
# Plotting the data for the map occupancy
plt.figure(figsize=(16, 9))

# Plot the merged map occupation over time for each simulation
for i in range(num_simulations):
    _simulation_number = int(data_files[i].split("_")[1])
    plt.plot(np.array(cpu_time_list[i]) - cpu_time_list[i][0], cpu_percentages_list[i],
             label=f'Simulation {_simulation_number} - CPU Usage over time with {num_robots_list[i]} Robots')

plt.xlabel('Time [s]')
plt.ylabel('Percentage CPU used')
plt.legend()
plt.title('CPU Usage')
plt.grid(True)

plt.ylim(0, 100)

# Adjust the figure
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

# Show the plot
plt.show()

################################## GPU USAGE ##################################
if gpu_time != []:
    # Plotting the data for the map occupancy
    plt.figure(figsize=(16, 9))

    # Plot the merged map occupation over time for each simulation
    for i in range(num_simulations):
        _simulation_number = int(data_files[i].split("_")[1])
        plt.plot(np.array(gpu_time_list[i]) - gpu_time_list[i][0], gpu_percentages_list[i],
                label=f'Simulation {_simulation_number} - GPU Usage over time with {num_robots_list[i]} Robots')
        plt.plot(np.array(gpu_time_list[i]) - gpu_time_list[i][0], gpu_memory_list[i],
                label=f'Simulation {_simulation_number} - GPU Memory Usage over time with {num_robots_list[i]} Robots')

    plt.xlabel('Time [s]')
    plt.ylabel('Percentage GPU used')
    plt.legend()
    plt.title('GPU Usage')
    plt.grid(True)

    plt.ylim(0, 100)

    # Adjust the figure
    plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.2, hspace=0.4)

    # Show the plot
    plt.show()

# Function to create raincloud plot
def create_raincloud_plot(data, color, label):
    pt.RainCloud(data, bw=.2, alpha=0.6, orient='h', palette=[color], box_showfliers=False, label=label)

# Plotting the data for the radius points
radius_values_data = np.array(radius_values_list)

# Create separate raincloud plot for each simulation
for i, data in enumerate(radius_values_data):
    plt.figure(figsize=(10, 6))
    color = plt.cm.tab10(i)
    create_raincloud_plot(data, color, f'Simulation {i + 1}')
    plt.title(f'Raincloud Plot for Radius Values - Simulation {i + 1}')
    plt.legend()
    plt.grid(True)
    
    # Set appropriate y-axis limits
    min_y = np.min(data) - 0.25
    max_y = np.max(data) + 0.25
    plt.ylim(min_y, max_y)
    
    # Add KDE and Box Plot labels under corresponding graphs
    plt.text(0.25, -0.08, 'KDE', ha='center', va='center', transform=plt.gca().transAxes)
    plt.text(0.5, -0.08, 'Box Plot', ha='center', va='center', transform=plt.gca().transAxes)
    
    plt.show()


# Plotting the data for the percentage values
percentage_values_data = np.array(percentage_values_list)

# Create separate raincloud plot for each simulation
for i, data in enumerate(percentage_values_data):
    plt.figure(figsize=(10, 6))
    color = plt.cm.tab10(i)
    create_raincloud_plot(data, color, f'Simulation {i + 1}')
    plt.title(f'Raincloud Plot for Percentage Values - Simulation {i + 1}')
    plt.legend()
    plt.grid(True)
    
    # Set appropriate y-axis limits
    min_y = np.min(data) - 10
    max_y = np.max(data) + 10
    plt.ylim(min_y, max_y)
    
    # Add KDE and Box Plot labels under corresponding graphs
    plt.text(0.25, -0.08, 'KDE', ha='center', va='center', transform=plt.gca().transAxes)
    plt.text(0.5, -0.08, 'Box Plot', ha='center', va='center', transform=plt.gca().transAxes)
    
    plt.show()


# Get the default color cycle from matplotlib
default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Create a figure with size (16, 9) for radius_values
plt.figure(figsize=(16, 9))

# Boxplot data for radius_values
bp_radius = plt.boxplot(radius_values_list, patch_artist=True, vert=False)

# Change to the desired color and add transparency
for patch, color in zip(bp_radius['boxes'], default_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.4)

# Violinplot data for radius_values
vp_radius = plt.violinplot(radius_values_list, points=500,
                           showmeans=False, showextrema=False, showmedians=False, vert=False)

for idx, b in enumerate(vp_radius['bodies']):
    # Get the center of the plot
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # Modify it so we only see the upper half of the violin plot
    b.get_paths()[0].vertices[:, 1] = np.clip(b.get_paths()[0].vertices[:, 1], idx + 1, idx + 2)
    # Change to the desired color
    b.set_color(default_colors[idx])

# Scatterplot data for radius_values
for idx, radius_values in enumerate(radius_values_list):
    # Add jitter effect so the features do not overlap on the y-axis
    y = np.full(len(radius_values), idx + .8)
    idxs = np.arange(len(y))
    out = y.astype(float)
    out.flat[idxs] += np.random.uniform(low=-.05, high=.05, size=len(idxs))
    y = out
    plt.scatter(radius_values, y, s=.3, c=default_colors[idx], marker='o', label=f'Simulation {idx + 1}')

plt.yticks(np.arange(1, num_simulations + 1, 1), [f'Simulation {i}' for i in range(1, num_simulations + 1)])
plt.xlabel('Radius Values')
plt.title("Raincloud plot for Radius Values")
plt.legend(loc='upper right')


# Create a figure with size (16, 9) for percentage_values
plt.figure(figsize=(16, 9))

# Boxplot data for percentage_values
bp_percentage = plt.boxplot(percentage_values_list, patch_artist=True, vert=False)

# Change to the desired color and add transparency
for patch, color in zip(bp_percentage['boxes'], default_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.4)

# Violinplot data for percentage_values
vp_percentage = plt.violinplot(percentage_values_list, points=500,
                               showmeans=False, showextrema=False, showmedians=False, vert=False)

for idx, b in enumerate(vp_percentage['bodies']):
    # Get the center of the plot
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # Modify it so we only see the upper half of the violin plot
    b.get_paths()[0].vertices[:, 1] = np.clip(b.get_paths()[0].vertices[:, 1], idx + 1, idx + 2)
    # Change to the desired color
    b.set_color(default_colors[idx])

# Scatterplot data for percentage_values
for idx, percentage_values in enumerate(percentage_values_list):
    # Add jitter effect so the features do not overlap on the y-axis
    y = np.full(len(percentage_values), idx + .8)
    idxs = np.arange(len(y))
    out = y.astype(float)
    out.flat[idxs] += np.random.uniform(low=-.05, high=.05, size=len(idxs))
    y = out
    plt.scatter(percentage_values, y, s=.3, c=default_colors[idx], marker='s', label=f'Simulation {idx + 1}')

plt.yticks(np.arange(1, num_simulations + 1, 1), [f'Simulation {i}' for i in range(1, num_simulations + 1)])
plt.xlabel('Percentage Values')
plt.title("Raincloud plot for Percentage Values")
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()