import os
import time
import subprocess
import signal
import pyautogui
import yaml
import shutil
from datetime import datetime


simtime  = 3*60 # 45 mins
# Set the paths to the ROS1 and ROS2 installations
ros1_path_setup_distro = "/opt/ros/noetic"
ros1_path_setup_ws = "~/data/ros1_ws/devel"
ros2_path_setup_distro = "/opt/ros/foxy"
ros2_path_setup_ws = "~/data/ros2_ws/install"

# Define ROS1 commands
ros1_roscore_cmd = "roscore"
ros1_simulation_cmd = "roslaunch graph_d_exploration file_hos.launch"
ros1_karto_cmd = "roslaunch graph_d_exploration multiple.launch"
ros1_centralised = "roslaunch graph_d_exploration servers.launch"
ros1_plottingNode = "rosrun plotting plot.py"
ros1_killplotnode = "rosnode kill /plotter_node"

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "HOS_config.yaml")


with open(config_path, 'r') as file:
    config = yaml.safe_load(file)


# Extract values
num_robots = config['num_robots']
ros1_mapsaver = config['paths']['map_saver_command']
maps_dir = config['paths']['maps_dir']
g2o_dir = config['paths']['g2o_dir']
plotting_dir = config['paths']['plotting_dir']
plot_g2o_src = config['paths']['plot_g2o_dir']


# Define ROS2 commands
ros2_bridge_cmd = "ros2 run ros1_bridge dynamic_bridge"
ros2_map_merge_cmd = f"ros2 launch merge_map merge_map_launch.py num_robots:={num_robots}"

def take_screenshots_and_save(folder_path):
    screenshot1 = pyautogui.screenshot()  # Fullscreen screenshot
    screenshot1.save(os.path.join(folder_path, "full_screen.png"))

    # Optionally, take region-specific screenshots if needed
    # region = (x, y, width, height)
    # screenshot2 = pyautogui.screenshot(region=(100, 100, 800, 600))
    # screenshot2.save(os.path.join(folder_path, "plotting_window.png"))

def copy_latest_map_files(map_dir, dest_folder):
    files = sorted(
        [os.path.join(map_dir, f) for f in os.listdir(map_dir) if f.endswith('.pgm') or f.endswith('.yaml')],
        key=os.path.getmtime,
        reverse=True
    )
    for file in files[:2]:  # assuming the latest .pgm and .yaml
        shutil.copy(file, dest_folder)

def copy_latest_g2o_files(map_dir, dest_folder):
    extensions = ('.g2o')
    files = sorted(
        [os.path.join(map_dir, f) for f in os.listdir(map_dir) if f.endswith(extensions)],
        key=os.path.getmtime,
        reverse=True
    )
    for file in files[:3]:  # Copy the 5 most recent relevant files
        shutil.copy(file, dest_folder)

def copy_latest_plotting_files(map_dir, dest_folder):
    extensions = ('.npy')
    files = sorted(
        [os.path.join(map_dir, f) for f in os.listdir(map_dir) if f.endswith(extensions)],
        key=os.path.getmtime,
        reverse=True
    )
    for file in files[:1]:  # Copy the 5 most recent relevant files
        shutil.copy(file, dest_folder)

def copy_plot_g2o_files(src_folder, dest_folder):
    for file_name in os.listdir(src_folder):
        full_file_path = os.path.join(src_folder, file_name)
        if os.path.isfile(full_file_path):
            shutil.copy(full_file_path, dest_folder)        



# Function to run each terminal
def launch_terminal(cmd, title=None, ros1=True):
    title_option = f'--title="{title}"' if title else ''
    if ros1:
        setup_distro_path = ros1_path_setup_distro
        setup_ws_path = ros1_path_setup_ws
    else:
        setup_distro_path = ros2_path_setup_distro
        setup_ws_path = ros2_path_setup_ws

    os.system(
        f"gnome-terminal {title_option} --window -- zsh -c 'source {setup_distro_path}/setup.zsh; source {setup_ws_path}/setup.zsh; {cmd}; exec zsh'")


def main():
    # Launch terminals and store the process objects
    launch_terminal(ros1_roscore_cmd, "ROSCORE", ros1=True) 
    time.sleep(5)

    print("[IMPORTANT] Plotting Node Started")
    launch_terminal(ros1_plottingNode, "Plotting Node Started", ros1=True) 
    
    time.sleep(5)
    #input("Press to start the simulation [Enter]: ")

    launch_terminal(ros1_simulation_cmd, "ROS1 SIMULATION", ros1=True)
    print("Simulation starting ...")
    time.sleep(10)
    time.sleep(10)
    time.sleep(10)

     # Wait for user input to kill all processes
    print("")
    print("")
    #input("Press to start the ROS bridge, the map merger node and the servers [Enter]: ")

    launch_terminal(ros2_bridge_cmd, "ROS2 BRIDGE", ros1=False)
    print("")
    print("ROS bridge starting ...")
    time.sleep(5)
    launch_terminal(ros2_map_merge_cmd, "ROS2 MAP MERGE", ros1=False)
    print("")
    print("Map merge starting ...")
    time.sleep(5)
    launch_terminal(ros1_centralised, "ROS1 CENTRALISED SERVER", ros1=True)
    print("")
    print("Servers starting ...")
    
    print("")
    print("")
    # Wait for user input to kill all processes
    #input("Start the controller nodes [Enter]: ")
    time.sleep(10)
    launch_terminal(ros1_karto_cmd, "ROS1 CONTROLLER", ros1=True)
    #print("Servers starting ...")
    #print("")
    #print("")
    # Wait for user input to kill all processes
    time.sleep(10)
    print("[IMPORTANT] Stop the data collector before")
    #input("Kill all processes [Enter]: ")
    #os.system("pkill -f gnome-terminal")
    #Close all terminals
    #Kill all processes containing "gnome-terminal" in the name
    #input("Kill all processes [Enter]: ")   



if __name__ == "__main__":
    for i in range(1):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_folder = f"/home/farhan/data/ros1_ws/src/thesis_ws/results/simulation/Hospital/run_{timestamp}_{num_robots}_robots"
        os.makedirs(result_folder, exist_ok=True)
        main()  
        time.sleep(simtime)    
        print("Saving the Map before Exiting ...")
        launch_terminal(ros1_mapsaver, "Save to Merged Map", ros1=True)
        time.sleep(20)
        launch_terminal(ros1_killplotnode, "plotiing node kill", ros1=True)
        time.sleep(10)  

        print("Taking screenshots before saving the map...")
        take_screenshots_and_save(result_folder)
        time.sleep(1)  
        copy_latest_map_files(maps_dir, result_folder)
        time.sleep(1)  
        copy_latest_g2o_files(g2o_dir, result_folder)
        time.sleep(1)  
        copy_latest_plotting_files(plotting_dir, result_folder)
        time.sleep(1)       
        copy_plot_g2o_files(plot_g2o_src, result_folder)   

        time.sleep(10)  
        os.system("pkill -f gnome-terminal")
        time.sleep(20)


    

        


