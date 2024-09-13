#!/usr/bin/env python3

# s4636216@studenti.unige.it
# 2023, Università degli Studi di Genova, LS2N Ecole Centrale de Nantes

import rospy
import numpy as np

from copy import copy
from graph_d_exploration.msg import InfoMatrix, PointArray, MergePointsResult, ChooseGoalResult
from geometry_msgs.msg import Point
from std_msgs.msg import Bool, Float32, Int32
from client_merge import MergePointsClient
from client_choose import ChooseGoalClient

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Callbacks~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Prototype of the callbacks used in an iterative way


def cncallback0(data, robot_id):
    global c, recc
    if not recc[robot_id]:
        c[robot_id] = []
        for point in data.points:
            c[robot_id].append(np.array([point.x, point.y]))
        recc[robot_id] = True


def cncallback1(data, robot_id):
    global m, recr
    if not recr[robot_id]:
        m[robot_id] = np.array(data.data).reshape(data.rows, 3)
        recr[robot_id] = True


def cncallback2(data, robot_id):
    global closer_goal_ack
    closer_goal_ack[robot_id] = data.data
    print(closer_goal_ack)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function to create callbacks in a iterative way
# depending on the number of robots used
def create_callbacks(num_robots, cb):
    callbacks = []
    for i in range(num_robots):

        # Choosing the callback type
        if cb == 0:
            def callback(data, i=i): return cncallback0(data, i)
        elif cb == 1:
            def callback(data, i=i): return cncallback1(data, i)
        elif cb == 2:
            def callback(data, i=i): return cncallback2(data, i)

        callbacks.append(callback)

    return callbacks


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Node~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def node():
    global c, m, recc, recr, closer_goal_ack

    rospy.init_node('manager', anonymous=False)
    rospy.loginfo('Started node')

    # Retrieve the number of agents as paramter
    num_robots = rospy.get_param('~num_robots')

    # Creating the callbacks and the subcribers
    callbacks0 = create_callbacks(num_robots, 0)
    callbacks1 = create_callbacks(num_robots, 1)
    callbacks2 = create_callbacks(num_robots, 2)

    # Create empty lists to store the point data for each robot
    c = [[] for _ in range(num_robots)]

    # Create empty numpy arrays to store the matrix data for each robot
    m = [np.zeros((1, 3)) for _ in range(num_robots)]

    # Create boolean variables to keep track of whether the point and matrix data have been received for each robot
    recc = [False] * num_robots
    recr = [False] * num_robots
    closer_goal_ack = [True] * num_robots

    # Create variables to keep track of the number of rows in the matrix data for each robot
    rows = [0] * num_robots

    # Create subscribers for each robot
    for i in range(num_robots):
        topic_name = f"robot_{i}/agent_centroid"
        message_type = PointArray
        rospy.Subscriber(topic_name, message_type, callbacks0[i])

    # Create subscribers for each robot
    for i in range(num_robots):
        topic_name = f"robot_{i}/reward_information"
        message_type = InfoMatrix
        rospy.Subscriber(topic_name, message_type, callbacks1[i])

    # Create subscribers for each robot
    for i in range(num_robots):
        topic_name = f"robot_{i}/closer_goal"
        message_type = Bool
        rospy.Subscriber(topic_name, message_type, callbacks2[i])

    client_mergeCentroids = MergePointsClient('merge_client')
    client_choosePoints = ChooseGoalClient('choose_client')

    merged_centroids_pub = rospy.Publisher(
        'merged_centroids', PointArray, queue_size=10)

    chosen_points_pub = rospy.Publisher(
        'chosen_points', PointArray, queue_size=10)
    
    received_list_points_publisher = rospy.Publisher(
        'list_points', Int32, queue_size=10)
    
    # Publisher for the radius value
    radius_value_publisher = rospy.Publisher(
        'radius_value', Float32, queue_size=10)
    
    # Publisher for the percentage value
    percentage_value_publisher = rospy.Publisher(
        'percentage_value', Float32, queue_size=10)

    rate = 0.25

    # This flags avoid the code to be stuck
    # Flag to check if the merged points have already been processed
    first_second = False
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while not rospy.is_shutdown():
        if not first_second:

            rospy.loginfo(
                'Waiting for all agents to publish detected points ...')

            # Wait until all the agents published the frontiers
            while not all(recc):
                continue

            rospy.loginfo('Sending goal for merging')

            # Send goal and store the result
            result = MergePointsResult()
            c_all = []
            for i in range(num_robots):
                c_all.extend(c[i])
            
            msg = Int32()
            if c_all != []:
                msg = len(c_all)
            else:
                msg = 0
            received_list_points_publisher.publish(msg)
            result = client_mergeCentroids.send_goal(c_all)

            tempPointArray = PointArray()

            # Publish the result back to the assigner nodes
            for i in range(len(result.merged_points)):
                tempPoint = Point()
                tempPoint.z = 0.0
                tempPoint.x = result.merged_points[i].x
                tempPoint.y = result.merged_points[i].y
                tempPointArray.points.append(copy(tempPoint))

            # Handle of the case the graph did not start
            if not any(element for element in closer_goal_ack):
                first_second = True
            else:
                rospy.logwarn('One or more agent needed to be moved. Waiting ...')
                #closer_goal_ack = [False] * num_robots
                first_second = False

            # Print log
            rospy.loginfo('Publishing result')
            merged_centroids_pub.publish(tempPointArray.points)
            percentage_value_publisher.publish(result.percentage_used)
            radius_value_publisher.publish(result.radius_used)

            # Reset the flags
            recc = [False] * num_robots

        elif first_second:

            rospy.loginfo(
                'Waiting for all agents to publish [Reward, X, Y] information ...')

            # Wait until all the agents published the matrix
            while not all(recr):
                continue

            # Send goal and store the result
            result = ChooseGoalResult()

            # Form a unique matrix
            concatenated_matrix = m[0]
            for i in range(1, num_robots):
                concatenated_matrix = np.vstack((concatenated_matrix, m[i]))

            # Store the number of rows for each matrix
            rows = [m[i].shape[0] for i in range(num_robots)]
            # Print log
            rospy.loginfo('Sending goal')
            # Pass the goal
            result = client_choosePoints.send_goal(
                concatenated_matrix.flatten().tolist(), rows)

            # Publish the result back to the assigner nodes
            # Form the PointArray structure to publish
            tempPointArray = PointArray()
            tempPoint = Point()
            tempPoint.z = 0.0

            for i in result.goals:
                tempPoint.x = i.x
                tempPoint.y = i.y
                tempPointArray.points.append(copy(tempPoint))

            first_second = False

            chosen_points_pub.publish(tempPointArray)
            rospy.loginfo('Published goals for the agents')

            # Reset the flags
            recr = [False] * num_robots

        rospy.sleep(rate)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
