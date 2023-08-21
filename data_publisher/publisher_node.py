#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def main():
    # Инициализация узла ROS
    rospy.init_node('data_publisher_node', anonymous=True)

    # Создание паблишера для публикации данных в топик /received_data
    pub = rospy.Publisher('/received_data', String, queue_size=10)

    # Цикл публикации данных
    rate = rospy.Rate(1) # 1 сообщение в секунду
    while not rospy.is_shutdown():
        data = "random data"  # Ваши данные

        # Публикация данных в топик /received_data
        pub.publish(data)

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
