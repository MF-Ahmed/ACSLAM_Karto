#!/usr/bin/python3
#
# Julio Placed. University of Zaragoza. 2022.
# jplaced@unizar.es

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sys,os
import time
import pandas as pd
from scipy.signal import butter, filtfilt
from scipy.signal import savgol_filter
import warnings
from optparse import OptionParser
from weighted_pose_graph_class import weighted_pose_graph
import utils as ut

# Get the absolute path of the current directory
current_directory = os.path.abspath(os.getcwd())

# File name
file_name = "/graph_0.g2o"

# Construct the absolute path to the file
file_path = os.path.join(current_directory, file_name)

base_file_path = current_directory
#base_file_path = '/home/usr/data/catkin_ws/src/aslam_rosbot/validation/test/'

from pandas import DataFrame

python_version = sys.version_info[0]
if python_version < 3:
    warnings.warn("Careful, using python version 2")

if __name__ == '__main__':
    try:
        fig_id = 0
        parser = OptionParser()
        parser.add_option("--graph", dest="graph_name", default="aloo")
        parser.add_option("--initial_nodes", dest="initial_nodes", default=base_file_path+file_name+"_nodes.txt")
        parser.add_option("--initial_edges", dest="initial_edges", default=base_file_path+file_name+"_edges.txt")
        parser.add_option("--optimized_nodes", dest="optimized_nodes", default=base_file_path+file_name+"_nodes.txt")
        parser.add_option("--optimized_edges", dest="optimized_edges", default=base_file_path+file_name+"_edges.txt")
        filepath_opti = os.path.join(os.getcwd(), 'd-opt.txt')
        plt.rcParams.update({'xtick.labelsize': 16, 'ytick.labelsize': 16})
        (options, args) = parser.parse_args()

        [nodes_i, edges_i, nodes_o, edges_o] = ut.read_graph(options, args)
        G_i = weighted_pose_graph(nodes_i, edges_i)

        with open(filepath_opti, 'r') as file:
            data = np.array(np.loadtxt(filepath_opti))  # Read data from file
            data = data/np.max(data) # normalize
            
        G_o = weighted_pose_graph(nodes_o, edges_o)

        with open(filepath_opti, 'r') as file:
            data = np.array(np.loadtxt(filepath_opti))  # Read data from file
            data = data/np.max(data) # normalize
            #plt.xlim(0,len(edges))  # Set x-axis range
            # Convert the list to a pandas Series
            data = pd.Series(data)
            plt.ylim(0, np.max(data))  # Set x-axis range
            plt.grid(True)
            #plt.plot(data)
            # Calculate the running average
      
            #content = file.readlines()
            #print("Opti-content = {}".format(content))

        G_t = weighted_pose_graph(nodes_i, edges_i, 't_opt')
        G_d = weighted_pose_graph(nodes_i, edges_i, 'd_opt')
        G_e = weighted_pose_graph(nodes_i, edges_i, 'e_opt')
        G_te = weighted_pose_graph(nodes_i, edges_i, 'tilde_opt')
        print('Pose graph plot.')
        ###ut.wait_enterKey()
        fig_id += 1
        plt.figure(fig_id)
        ax = plt.gca()
        #G_i.plot_graph('Trajectory', 'blue', False)
        G_o.plot_graph_rot('', 'red', True, rotate_90_cw=True)
        #plt.suptitle('Pose graph trajectory', fontsize=14)
        plt.xlabel('X (m)', fontsize=14)
        plt.ylabel('Y (m)', fontsize=14)
        plt.axis('equal')
        plt.legend(fontsize=14)
        plt.grid(True)
        plt.show(block=1)
      
        print('Computation of spectral properties of the full graph.')
        #ut.wait_enterKey()
        avg = 2 * G_i.get_no_edges() / G_i.get_no_nodes()
        eigv_2 = G_i.compute_algcon() # compute the algebric connectivity, the second smallest eigenvalue of the Laplacian matrix of the graph
        L_anch = G_i.compute_anchored_L()
        # sign and the natural logarithm of the determinant of a given square matrix.
        sign, logdet = np.linalg.slogdet(L_anch.todense())
        if sign == 1:
            spann = logdet / ((G_i.get_no_nodes() - 2) * np.log(G_i.get_no_nodes())) # this is the traditional way for finding the spanning trees
        else:
            print("WARNING. Check slogdet, signed below or equal to zero.")
            spann = 0
        print('Average Degree (d): ' + format(avg))
        print('Algebraic Connectivity (lambda_2): ' + format(eigv_2))
        print('Normalized Tree connectivity = log(t)/log(n)*n-2: ' + format(spann))
       

    except KeyboardInterrupt:
        plt.close('all')
        print('\n Exit requested.')
        sys.exit()
    def moving_average(data, window_size):
        window = np.ones(window_size) / window_size
        return np.convolve(data, window, mode='same')
