import os
import time
import subprocess
import signal
simtime  = 21*60 # 20 mins

# Set the paths to the ROS1 and ROS2 installations
ros1_path_setup_distro = "/opt/ros/noetic"
ros1_path_setup_ws = "~/data/matteo_thesis/MAGS/thesis_ws/devel"

ros2_path_setup_distro = "/opt/ros/foxy"
ros2_path_setup_ws = "~/data/ros2_ws/install"

# Define ROS1 commands
ros1_roscore_cmd = "roscore"
ros1_simulation_cmd = "roslaunch graph_d_exploration file.launch "
ros1_karto_cmd = "roslaunch graph_d_exploration multiple.launch"
ros1_centralised = "roslaunch graph_d_exploration servers.launch"

run_plotter = "rosrun plotting plot.py"

ros1_killplotnode = "rosnode kill /plotter_node"  
ros1_mapsaver = "rosrun map_server map_saver -f ~/data/matteo_thesis/MAGS/thesis_ws/results/simulation/willowgarage/$map_$(date +'%Y%m%d_%H%M%S')"

# Define ROS2 commands
ros2_bridge_cmd = "ros2 run ros1_bridge dynamic_bridge"
ros2_map_merge_cmd = "ros2 launch merge_map merge_map_launch.py num_robots:=2"

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
        f"gnome-terminal {title_option} --window -- bash -c 'source {setup_distro_path}/setup.bash; source {setup_ws_path}/setup.bash; {cmd}; exec bash'")


def main():
    # Launch terminals and store the process objects
    launch_terminal(ros1_roscore_cmd, "ROSCORE", ros1=True)
    time.sleep(2) 
    launch_terminal(run_plotter, "plotter-started", ros1=True)
    print("Plotter started...")
    print("")
    print("")
    print("[IMPORTANT] run plotting data collector before")
    #input("Press to start the simulation [Enter]: ")

    launch_terminal(ros1_simulation_cmd, "ROS1 SIMULATION", ros1=True)
    print("Simulation starting ...")
    
    # Wait for user input to kill all processes
    print("")
    print("")
    #time.sleep(50)
    #time.sleep(20)
    time.sleep(5)
    #input("Press to start the ROS bridge, the map merger node and the servers [Enter]: ")

    launch_terminal(ros2_bridge_cmd, "ROS2 BRIDGE", ros1=False)
    print("")
    print("ROS bridge starting ...")

    launch_terminal(ros2_map_merge_cmd, "ROS2 MAP MERGE", ros1=False)
    print("")
    print("Map merge starting ...")
    launch_terminal(ros1_centralised, "ROS1 CENTRALISED SERVER", ros1=True)
    print("")
    print("Servers starting ...")
    
    print("")
    print("")
    # Wait for user input to kill all processes
    #input("Start the controller nodes [Enter]: ")
    time.sleep(5) 

    launch_terminal(ros1_karto_cmd, "ROS1 CONTROLLER", ros1=True)
    print("Servers starting ...")

    print("")
    print("")
    time.sleep(5) 

    # Wait for user input to kill all processes
    #print("[IMPORTANT] Stop the data collector before")
    #input("Kill all plotiing node  [Enter]: ")
    #launch_terminal(ros1_killplotnode, "plotiing node kill", ros1=True)
    #print("killing plotter node ")
    #time.sleep(10)  

    #input("Kill all processes [Enter]: ")

    # Close all terminals
    # Kill all processes containing "gnome-terminal" in the name
    #os.system("pkill -f gnome-terminal")

if __name__ == "__main__":
    for i in range(13):
        main()
        time.sleep(simtime)    
        print("Saving the Map before Exiting ...")
        launch_terminal(ros1_mapsaver, "Save to Merged Map", ros1=True)
        time.sleep(70)
        launch_terminal(ros1_killplotnode, "plotiing node kill", ros1=True)
        time.sleep(10)  
        os.system("pkill -f gnome-terminal")
        time.sleep(20)

