#! /usr/bin/python3

import rospy
from std_msgs.msg import String


class Talker:
    def __init__(self):
        self.pub = rospy.Publisher("chatter", String, queue_size=10)
        self.rate = rospy.Rate(10)

    def run(self):
        hello_string = "hello world {}".format(rospy.get_time())
        rospy.loginfo(hello_string)
        self.pub.publish(hello_string)
        self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node("talker")

    talker = Talker()

    try:
        while not rospy.is_shutdown():
            talker.run()
    except rospy.ROSInterruptException:
        pass
