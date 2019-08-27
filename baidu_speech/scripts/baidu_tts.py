#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from aip import AipSpeech
from playsound import playsound
import os

class BaiduSpeech:
    def __init__(self):
        #rospy.on_shutdown(self.cleanup);

        # 初始化ROS节点
        rospy.init_node("baidu_tts", anonymous=True)
        
        rate = rospy.Rate(10) # 发布频率为10hz

        #   订阅语音识别的话题
        rospy.Subscriber("/Rog_result", String, self.getTTS)

        rospy.spin()


    #   把识别出来的文字播放出来
    def getTTS(self,data):
        self.get_word = data.data
        print self.get_word

        # 百度语音APP ID
        self.APP_ID = '17089547'
        self.API_KEY = 'b76MGFLcxqXZh6qqiFGs3OpC'
        self.SECRET_KEY = 'QWcAlCeWFzsGAZSYTgQFedRbcvxIYX12'
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.ip = 'www.baidu.com'
        if os.system('ping -c 1 -w 1 %s' %self.ip):
            print '语音识别未通过，请重新输入！'
        else:
            result  = self.client.synthesis(self.get_word, 'zh', 1, {'vol': 5,})
            self.playSound(result)

    def playSound(self, res):
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(res, dict):
            with open('auido.mp3', 'wb') as f:
                f.write(res)
        playsound("auido.mp3")

################################################################################            
if __name__== '__main__' :
    try:
        BaiduSpeech()
	#rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("baidu speech.")
    #rospy.sleep(5)
    #rospy.spin()
