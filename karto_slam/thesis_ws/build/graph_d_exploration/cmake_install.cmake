# Install script for directory: /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install" TYPE PROGRAM FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install" TYPE PROGRAM FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/setup.bash;/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/setup.bash"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/setup.sh;/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/setup.sh"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/setup.zsh;/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/setup.zsh"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/install" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/.rosinstall")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/msg" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration/msg/Point2D.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration/msg/PointArray.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration/msg/InfoMatrix.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/action" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration/action/MergePoints.action"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration/action/ChooseGoal.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/msg" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsAction.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsActionGoal.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsActionResult.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsActionFeedback.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsGoal.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsResult.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/MergePointsFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/msg" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalAction.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalActionGoal.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalActionResult.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalActionFeedback.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalGoal.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalResult.msg"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/graph_d_exploration/msg/ChooseGoalFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/cmake" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/graph_d_exploration-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/include/graph_d_exploration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/roseus/ros/graph_d_exploration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/common-lisp/ros/graph_d_exploration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/share/gennodejs/ros/graph_d_exploration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/lib/python3/dist-packages/graph_d_exploration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/lib/python3/dist-packages/graph_d_exploration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/graph_d_exploration" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/include/graph_d_exploration/informationGainConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/graph_d_exploration" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/lib/python3/dist-packages/graph_d_exploration/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/lib/python3/dist-packages/graph_d_exploration/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/graph_d_exploration" TYPE DIRECTORY FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/graph_d_exploration/lib/python3/dist-packages/graph_d_exploration/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/graph_d_exploration.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/cmake" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/graph_d_exploration-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration/cmake" TYPE FILE FILES
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/graph_d_explorationConfig.cmake"
    "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/catkin_generated/installspace/graph_d_explorationConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graph_d_exploration" TYPE FILE FILES "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/graph_d_exploration/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/graph_d_exploration/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
