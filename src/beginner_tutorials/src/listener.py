#! /usr/bin/python3

import rospy
from std_msgs.msg import String


class Listener:
    def __init__(self):
        rospy.Subscriber("chatter", String, self.callback)

    def callback(self, data):
        string = "{} I heard {}".format(rospy.get_caller_id(), data.data)
        rospy.loginfo(string)


if __name__ == '__main__':
    listener = Listener()

    rospy.init_node("listener")

    rospy.spin()
