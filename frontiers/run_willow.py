import os
import time
import subprocess
import signal
import datetime
simtime  = 4*60 # 45 mins

# Set the paths to the ROS1 and ROS2 installations
ros1_path_setup_distro = "/opt/ros/noetic"
ros1_path_setup_ws = "/home/usr/data/matteo_thesis/frontiers/devel"

# Define ROS1 commands
ros1_roscore_cmd = "roscore"
ros1_simulation_cmd = "roslaunch aslam_turtlebot turtlebot_rviz_karto.launch"
ros1_karto_cmd = "roslaunch  aslam_turtlebot exploration.launch"
d_opti_plot = "rosrun aslam_turtlebot d_opti_plot.py"
ros1_plottingNode = "rosrun plotting_aslam_turtlebot_dopt plot.py"
ros1_mapsaver = "rosrun map_server map_saver -f /home/usr/data/catkin_ws/src/aslam_turtlebot/results/simulation/willowgarage/maps/$map_$(date +'%Y%m%d_%H%M%S')"

ros1_movebase_goal = "rosrun aslam_turtlebot init_goal.py"
ros1_killplotnode = "rosnode kill /plotter_node"
ros1_killgoalnode = "rosnode kill /send_goal_node"

copy_g2ofile = "cp /home/usr/data/catkin_ws/src/aslam_turtlebot/maps/posegraph_map.g2o /home/usr/data/catkin_ws/src/aslam_turtlebot/maps/PG_$(date +'%Y%m%d_%H%M%S').g2o"
copy_d_opti_file = "cp /home/usr/data/catkin_ws/src/aslam_turtlebot/results/d_opti_graph.png /home/usr/data/catkin_ws/src/aslam_turtlebot/results/d_opti_graph_$(date +'%Y%m%d_%H%M%S').png"


# Function to run each terminal
def launch_terminal(cmd, title=None, ros1=True):
    title_option = f'--title="{title}"' if title else ''
    if ros1:
        setup_distro_path = ros1_path_setup_distro
        setup_ws_path = ros1_path_setup_ws
    else:
        pass

    os.system(
        f"gnome-terminal {title_option} --window -- zsh -c 'source {setup_distro_path}/setup.zsh; source {setup_ws_path}/setup.zsh; {cmd}; exec zsh'")


def main():
    for i in range(2):
      # Launch terminals and store the process objects
      launch_terminal(ros1_roscore_cmd, "ROSCORE", ros1=True)
      time.sleep(2)

      launch_terminal(ros1_simulation_cmd, "RVIZ simulation", ros1=True)
      print("RVIZ Starting and Karto SLAM...")
      input("Kill all processes and save the Map [Enter]: ")
      # Wait for user input to kill all processes
      print("")
      print("")
      time.sleep(5) 
      launch_terminal(ros1_movebase_goal, "ROS1 CONTROLLER", ros1=True)
      time.sleep(10) 
      print("")
      print("")
      launch_terminal(ros1_killgoalnode, "ROS1 CONTROLLER", ros1=True)
      print("Killed Goal node")
      launch_terminal(ros1_karto_cmd, "ROS1 CONTROLLER", ros1=True)
      print("Exploration Starting...")

      time.sleep(5)
    
      print("")
      print("")
  
      launch_terminal(d_opti_plot, "d_opti_plot", ros1=True)
      print("Plot Started ...")
      print("")
      print("")   
      time.sleep(2)   
      
      launch_terminal(ros1_plottingNode, "ros1_plottingNode", ros1=True)
      print("Plotting node Started ...")
      print("")
      print("")   
      time.sleep(simtime)
      # Wait for user input to kill all processes
      #input("Kill all processes and save the Map [Enter]: ")
      launch_terminal(ros1_mapsaver, "map_saver", ros1=True)
      print("Map Saved...")
      time.sleep(5) # give some time to save the map 
      launch_terminal(ros1_killplotnode, "plotiing node kill", ros1=True)
      time.sleep(5)
      #launch_terminal(copy_g2ofile, "saving the g2o file ", ros1=True)
      #time.sleep(5)

      #launch_terminal(copy_d_opti_file, "saving the d_opti_file", ros1=True)
      #time.sleep(10)  
      input("Kill all processes and save the Map [Enter]: ")
      # Close all terminals
      # Kill all processes containing "gnome-terminal" in the name
      os.system("pkill -f gnome-terminal")  
      time.sleep(5) 
        

 

if __name__ == "__main__":
    main()
