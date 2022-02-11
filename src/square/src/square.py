#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
pi =3.1415

def openLoop():
	rospy.init_node('robotMoveOpenLoop', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	velocity = Twist()
	i = 0
	
	#Taking User Input
	print("Enter the following parameters to draw a square")
	speed = float(input("Enter the linear speed:"))
	angular_speed = float(input("Enter the angular speed:"))
	distance = float(input("Enter the distance:"))
	forward = float(input("Confirm if turtle is moving forward?:"))
	angle = float(input("Enter the angle of rotation:"))
	clockwise = float(input("Confirm if  the turtle is moving in clockwise direction?"))
	
	
	turtle_angle = angular_speed*pi/180
	turtle_omega = angle*pi/180
	
	
	
	velocity.linear.y = 0
	velocity.linear.z = 0
	velocity.angular.x = 0
	velocity.angular.y = 0
	velocity.angular.z = 0
	
	while (i<4):
		
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		
		while(current_distance<distance):
			if(forward):
				velocity.linear.x = abs(speed)
			else:
				velocity.linear.x = -abs(speed)

			
				
			pub.publish(velocity)
			t1 = rospy.Time.now().to_sec()
			current_distance = speed*(t1-t0)
		velocity.linear.x = 0
		pub.publish(velocity)
		
		if(clockwise):
			velocity.angular.z = -abs(turtle_angle)
		else:
			velocity.angular.z = abs(turtle_angle)
		
		velocity.linear.x = 0
		velocity.linear.y = 0
		velocity.linear.z = 0
		velocity.angular.x = 0
		velocity.angular.y = 0
		
		t02 = rospy.Time.now().to_sec()

		current_angle = 0
		while(current_angle<turtle_omega):
			pub.publish(velocity)
			t12 = rospy.Time.now().to_sec()
			current_angle = turtle_angle*(t12-t02)
	
		
		velocity.angular.z = 0
		pub.publish(velocity)
		#rospy.spin()
		i=i+1

if __name__ == '__main__':
	try:
		openLoop()
	except rospy.ROSInterruptException: pass




		
			
