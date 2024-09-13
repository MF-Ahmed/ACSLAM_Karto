#!/usr/bin/env python3

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from std_msgs.msg import Header

def send_goal():
    # Initialize the ROS node
    rospy.init_node('send_goal_node', anonymous=False)

    # Create a publisher for the MoveBaseActionGoal message
    #goal_publisher = rospy.Publisher("/move_base_simple/goal", MoveBaseActionGoal, queue_size=10)
    goal_publisher = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)

    # Create a MoveBaseActionGoal message
    goal = PoseStamped()
    goal.header.frame_id = 'map'
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 0.5
    goal.pose.position.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
 
    rate = rospy.Rate(0.5)  # 1 Hz

    while not rospy.is_shutdown():
        # Publish the goal message
        goal_publisher.publish(goal)
        rospy.loginfo("Published a goal.")
        rate.sleep()

if __name__ == '__main__':
    try:
        send_goal()
    except rospy.ROSInterruptException:
        pass
