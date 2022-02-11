#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys

def circle_move(radius):
	rospy.init_node('turtlecircle', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

	rate = rospy.Rate(10)
	velocity = Twist()

	while not rospy.is_shutdown():
		velocity.linear.x = radius
		velocity.linear.y = 0
		velocity.linear.z = 0
		velocity.angular.x = 0
		velocity.angular.y = 0
		velocity.angular.z = 1

		rospy.loginfo("Radius = %f", radius)
		pub.publish(velocity)
		rate.sleep()

if __name__ == '__main__':
    try:
        circle_move(float(1.5))
    except rospy.ROSInterruptException:
        pass 
