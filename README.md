# voice_interaction
### 百度语音
文件目录如下：
```bash
baidu_speech
├── CMakeLists.txt
├── launch
│   ├── simple_speaker.launch
│   ├── simple_voice.launch
│   └── warning_speaker.launch
├── msg
│   └── TTS_message.msg
├── package.xml
├── README.md
└── scripts
    ├── auido.mp3
    ├── baidu_tts.py
    ├── node_main.py
    ├── ParamSetting.py
    ├── simple_speek.py
    ├── voice_node.py
    └── 请让一下.mp3
```

##### 依赖
```bash
sudo pip install baidu_api
sudo pip install playsound
python -m pip install pyaudio
pip install python-vlc
sudo apt-get install python-pip portaudio19-dev vlc libvlc-dev
```
##### 语音合成

```bash
roslaunch baidu_speech simple_speaker.launch 

rostopic pub /speak_string std_msgs/String -- '小谷小谷'
```

##### 语音识别

```bash

roslaunch baidu_speech simple_voice.launch

```

##### 语音识别及合成
```bash
roslaunch baidu_speech simple_voice.launch

rosrun baidu_speech baidu_tts.py
```







