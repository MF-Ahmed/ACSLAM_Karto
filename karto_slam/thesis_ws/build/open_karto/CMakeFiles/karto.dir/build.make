# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto

# Include any dependencies generated for this target.
include CMakeFiles/karto.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/karto.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/karto.dir/flags.make

CMakeFiles/karto.dir/src/Karto.cpp.o: CMakeFiles/karto.dir/flags.make
CMakeFiles/karto.dir/src/Karto.cpp.o: /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Karto.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/karto.dir/src/Karto.cpp.o"
	/usr/lib/ccache/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/karto.dir/src/Karto.cpp.o -c /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Karto.cpp

CMakeFiles/karto.dir/src/Karto.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/karto.dir/src/Karto.cpp.i"
	/usr/lib/ccache/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Karto.cpp > CMakeFiles/karto.dir/src/Karto.cpp.i

CMakeFiles/karto.dir/src/Karto.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/karto.dir/src/Karto.cpp.s"
	/usr/lib/ccache/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Karto.cpp -o CMakeFiles/karto.dir/src/Karto.cpp.s

CMakeFiles/karto.dir/src/Mapper.cpp.o: CMakeFiles/karto.dir/flags.make
CMakeFiles/karto.dir/src/Mapper.cpp.o: /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Mapper.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/karto.dir/src/Mapper.cpp.o"
	/usr/lib/ccache/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/karto.dir/src/Mapper.cpp.o -c /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Mapper.cpp

CMakeFiles/karto.dir/src/Mapper.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/karto.dir/src/Mapper.cpp.i"
	/usr/lib/ccache/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Mapper.cpp > CMakeFiles/karto.dir/src/Mapper.cpp.i

CMakeFiles/karto.dir/src/Mapper.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/karto.dir/src/Mapper.cpp.s"
	/usr/lib/ccache/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto/src/Mapper.cpp -o CMakeFiles/karto.dir/src/Mapper.cpp.s

# Object files for target karto
karto_OBJECTS = \
"CMakeFiles/karto.dir/src/Karto.cpp.o" \
"CMakeFiles/karto.dir/src/Mapper.cpp.o"

# External object files for target karto
karto_EXTERNAL_OBJECTS =

/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so: CMakeFiles/karto.dir/src/Karto.cpp.o
/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so: CMakeFiles/karto.dir/src/Mapper.cpp.o
/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so: CMakeFiles/karto.dir/build.make
/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so: /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.71.0
/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so: /usr/lib/x86_64-linux-gnu/libboost_atomic.so.1.71.0
/home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so: CMakeFiles/karto.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared library /home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/karto.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/karto.dir/build: /home/usr/data/matteo_thesis/karto_slam/thesis_ws/devel/.private/open_karto/lib/libkarto.so

.PHONY : CMakeFiles/karto.dir/build

CMakeFiles/karto.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/karto.dir/cmake_clean.cmake
.PHONY : CMakeFiles/karto.dir/clean

CMakeFiles/karto.dir/depend:
	cd /home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto /home/usr/data/matteo_thesis/karto_slam/thesis_ws/src/3dParty/open_karto /home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto /home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto /home/usr/data/matteo_thesis/karto_slam/thesis_ws/build/open_karto/CMakeFiles/karto.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/karto.dir/depend

