# Efficient Frontier Management for Collaborative Active SLAM

In this implementation, we present the work described in our paper cited below. In autonomous robotics, a critical challenge lies
in developing robust solutions for Active Collaborative SLAM,
wherein multiple robots collaboratively explore and map an
unknown environment while intelligently coordinating their
movements and sensor data acquisitions. In this article, we
present an efficient centralized frontier sharing approach that
maximizes exploration by taking into account information gain
in the merged map, distance, and reward computation among
frontier candidates and encourages the spread of agents into
the environment. Eventually, our method efficiently spreads
the robots for maximum exploration while keeping SLAM
uncertainty low. Additionally, we also present two coordination
approaches, synchronous and asynchronous to prioritize robot
goal assignments by the central server. The proposed method
is implemented in ROS and evaluated through simulation and
experiments on publicly available datasets and similar methods,
rendering promising results.

**M. F. Ahmed, M. Maragliano, V. Frémont, C. T. Recchiuto and A. Sgorbissa, "Efficient Frontier Management for Collaborative Active SLAM," 2024 IEEE International Conference on Multisensor Fusion and Integration for Intelligent Systems (MFI), Pilsen, Czech Republic, 2024, pp. 1-7, doi: 10.1109/MFI62651.2024.10705778. **

Kindly cite this paper if you use this implementation.

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
