#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import urllib
import json
from aip import AipSpeech
from playsound import playsound
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def listener():
    rospy.Subscriber("Rog_result", String, callback)
    rospy.spin()

def callback(data):
    words=data.data

    # 百度语音APP ID
    APP_ID = '17089547'
    API_KEY = 'b76MGFLcxqXZh6qqiFGs3OpC'
    SECRET_KEY = 'QWcAlCeWFzsGAZSYTgQFedRbcvxIYX12'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    ip = 'www.baidu.com'

    if words !='识别错误':
        s=get_ans(words) 
        print s

        # 合成语音并播放出来
        if os.system('ping -c 1 -w 1 %s' %ip):
            print '语音识别未通过，请重新输入！'
        else:
            result  = client.synthesis(s, 'zh', 1, {'vol': 5,})
            playSound(result)

def playSound(res):
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(res, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(res)
    playsound("auido.mp3")


def get_ans(info):
    key = '0dd3488916f64d4eb3356308c7c20823'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    request = api + info
    response = getHtml(request)
    dic_json = json.loads(response)
    result = dic_json['text']
    return result

if __name__ == '__main__':
    rospy.init_node("Main")
    rospy.loginfo('进入聊天模式')
    pub = rospy.Publisher('speak_string', String, queue_size=10)

    # str=raw_input("press to publish")
    listener()   
