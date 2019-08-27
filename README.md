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



### pocketsphinx
pocketsphinx文件目录如下：
```bash
pocketsphinx
├── CMakeLists.txt
├── deb
│   ├── gstreamer0.10-pocketsphinx_0.8-5_amd64.deb
│   ├── libpocketsphinx1_0.8-5_amd64.deb
│   ├── libsphinxbase1_0.8-6_amd64.deb
│   └── pocketsphinx-hmm-en-tidigits_0.8-5_all.deb
├── demo
│   ├── robocup.corpus
│   ├── robocup.dic
│   ├── robocup.launch
│   ├── robocup.lm
│   ├── robocup_r1.launch
│   ├── robocup_r2.launch
│   ├── turtlebot_voice_cmd.launch
│   ├── voice_cmd.corpus
│   ├── voice_cmd.dic
│   ├── voice_cmd.launch
│   └── voice_cmd.lm
├── model
│   ├── hmm
│   │   └── en
│   │       └── tidigits
│   │           ├── feat.params
│   │           ├── mdef
│   │           ├── means
│   │           ├── sendump
│   │           ├── transition_matrices
│   │           └── variances
│   └── lm
│       └── en
│           ├── tidigits.dic
│           ├── tidigits.DMP
│           └── tidigits.fsg
├── package.xml
├── README.md
└── scripts
    ├── recognizer.py
    └── voice_cmd_vel.py
```

##### 安装依赖
```bash
sudo apt-get install ros-kinetic-audio-common
sudo apt-get install libasound2
sudo apt-get install gstreamer0.10-*
sudo apt-get install python-gst0.10
```

```bash
svn co https://github.com/GJXS1980/voice_interaction.git
cd deb/
sudo dpkg -i *.deb
cd  model
sudo cp /usr/share/pocketsphinx/model/* ~/catkin_ws/src/pocketsphinx/model -r

```

##### 编译
```
cd ~/catkin_ws/
catkin_make
```

##### 测试pocketsphinx的语音识别功能

```bash
roslaunch pocketsphinx robocup.launch
```





