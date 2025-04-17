# Efficient Frontier Management for Collaborative Active SLAM

This repository contains the implementation of the work described in the following publication:

**M. F. Ahmed, M. Maragliano, V. Frémont, C. T. Recchiuto, and A. Sgorbissa, "Efficient Frontier Management for Collaborative Active SLAM," *2024 IEEE International Conference on Multisensor Fusion and Integration for Intelligent Systems (MFI)*, Pilsen, Czech Republic, 2024, pp. 1–7. [doi: 10.1109/MFI62651.2024.10705778](https://doi.org/10.1109/MFI62651.2024.10705778)**

> **Note:** If you use this implementation in your work, please cite the above paper.

---

## Overview

In the field of autonomous robotics, a major challenge is enabling multiple robots to collaboratively explore and map an unknown environment while efficiently coordinating their actions and sensor data collection. This implementation presents a **centralized frontier-sharing strategy** designed to maximize exploration while minimizing SLAM uncertainty.

Our method computes rewards for frontier candidates based on:
- **Information gain**
- **Distance cost**
- **Spatial distribution of agents**

This encourages a well-balanced spread of robots across the environment. For robot-goal assignments, we propose two coordination strategies:
- **Synchronous coordination**
- **Asynchronous coordination**

The system is implemented using **ROS Noetic** and validated through simulations and experiments using publicly available datasets. Results demonstrate strong performance and scalability compared to baseline methods.

---

## Dependencies

### System Requirements
- **Ubuntu 20.04**  
- **ROS Noetic**  
  Follow the official instructions: [ROS Noetic installation](http://wiki.ros.org/noetic/Installation)

### Core Libraries and Tools
- **g2o**  
  Install from: [https://github.com/RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)

- **Open Karto**  
  Follow its official installation guide.

- **ROSbot 2**  
  Set up hardware and firmware as described in the [ROSbot 2 documentation](https://husarion.com/manuals/rosbot/)

- **Kobuki Plugins**  
  Required for compatibility with the Kobuki base.

- **Additional Libraries**
  ```bash
  sudo apt-get install libsuitesparse-dev

## Dependencies
- **ROS Noetic**: Follow the installation instructions [here](http://wiki.ros.org/noetic/Installation).
- **Ubuntu 20.04**: This project is designed for Ubuntu 20.04. Ensure you are using this version of Ubuntu.
- **g2o**: Install from the official repository at [g2o GitHub](https://github.com/RainerKuemmerle/g2o).
- **Open Karto**: Install Open Karto following its official instructions.
- **ROSbot 2**: Ensure the hardware and firmware are set up as per the ROSbot 2 documentation.
- **Kobuki Plugins**: Install necessary plugins for compatibility with the Kobuki base.
- **Libraries**: 
  ```bash
  sudo apt-get install libsuitesparse-dev
  ```
## ROS Specific Dependencies
 ```bash
    sudo apt-get install ros-noetic-grid-map
    sudo apt-get install ros-noetic-move-base
    sudo apt-get install ros-noetic-robot-localization
    sudo apt-get install ros-noetic-costmap-converter
    sudo apt-get install ros-noetic-open-karto
    sudo apt-get install ros-noetic-kobuki-core
