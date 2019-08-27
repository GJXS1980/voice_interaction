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
cd ~/catkin_ws/src
svn co https://github.com/GJXS1980/voice_interaction/trunk/pocketsphinx
cd voice_interaction/pocketsphinx/deb/
sudo dpkg -i *.deb
cd ../model
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

### sound_play功能包语音合成
sound_play功能包目录如下：
```bash
audio_common
├── audio_capture
│   ├── CMakeLists.txt
│   ├── launch
│   │   ├── capture.launch
│   │   ├── capture_to_file.launch
│   │   └── capture_wave.launch
│   ├── mainpage.dox
│   ├── package.xml
│   └── src
│       └── audio_capture.cpp
├── audio_common
│   ├── CHANGELOG.rst
│   ├── CMakeLists.txt
│   └── package.xml
├── audio_common_msgs
│   ├── CMakeLists.txt
│   ├── mainpage.dox
│   ├── msg
│   │   └── AudioData.msg
│   └── package.xml
├── audio_play
│   ├── CMakeLists.txt
│   ├── launch
│   │   └── play.launch
│   ├── mainpage.dox
│   ├── package.xml
│   └── src
│       └── audio_play.cpp
└── sound_play
    ├── action
    │   └── SoundRequest.action
    ├── CMakeLists.txt
    ├── include
    │   └── sound_play
    │       └── sound_play.h
    ├── mainpage.dox
    ├── msg
    │   └── SoundRequest.msg
    ├── package.xml
    ├── README.md
    ├── scripts
    │   ├── playbuiltin.py
    │   ├── playpackage.py
    │   ├── play.py
    │   ├── say.py
    │   ├── shutup.py
    │   ├── soundclient_example.py
    │   ├── soundplay_node.py
    │   ├── test
    │   │   └── test_sound_client.py
    │   ├── test_actionlib_client.py
    │   └── test.py
    ├── setup.py
    ├── soundplay_node.launch
    ├── sounds
    │   ├── BACKINGUP.ogg
    │   ├── NEEDS_PLUGGING_BADLY.ogg
    │   ├── NEEDS_PLUGGING.ogg
    │   ├── NEEDS_UNPLUGGING_BADLY.ogg
    │   ├── NEEDS_UNPLUGGING.ogg
    │   └── say-beep.wav
    ├── src
    │   └── sound_play
    │       ├── __init__.py
    │       ├── libsoundplay.py
    │       └── libsoundplay.pyc
    ├── test
    │   ├── CMakeLists.txt
    │   └── test.cpp
    └── test.launch
```

##### 安装audio-common和相关依赖库
```bash
#sudo apt-get install ros-kinetic-audio-common
sudo apt-get install libasound2 \
                     mplayer festvox-don \
                     libgstreamer1.0-dev \
                     libgstreamer-plugins-base1.0-dev \
                     gstreamer1.0 \
                     gstreamer1.0-plugins-base \
                     gstreamer1.0-plugins-good \
                     gstreamer1.0-plugins-ugly \
                     python-gi \
                     festival
```

如果出现错误，执行下面命令：<br>
(1)先安装gstreamer1.0会遇到依赖的库缺失
```bash
sudo apt-get install libmedia1:i386
```
(2)此时又会出错
```bash
sudo apt-get install libhybris-common1:i386
```
(3)依旧会出错
```bash
sudo apt-get install libandroid-properties1:i386
```
(4)这时libandroid-porperties1:i386安装成功，记下来一次安装上面出错的库
```bash
sudo apt-get install libandroid-properties1:i386
sudo apt-get install libhybris-common1:i386
sudo apt-get install libmedia1:i386
sudo apt-get install gstreamer1.0
```
然后重新安装上面的依赖。


##### 下载源码、编译
```bash
cd ~/catkin_ws/src
svn co https://github.com/GJXS1980/voice_interaction/trunk/audio_common
cd ~/catkin_ws/
catkin_make

```

##### 测试
```bash
roscore
rosrun sound_play soundplay_node.py
rosrun sound_play say.py "Hello World."

# 或者换一个人说话
roscore
rosrun sound_play soundplay_node.py
rosrun sound_play say.py "Welcome to my home" voice_don_diphone
```


### AIML的使用
AIML功能包目录如下：
```bash
ros_aiml
├── CMakeLists.txt
├── data
│   ├── ai.aiml
│   ├── alice.aiml
│   ├── astrology.aiml
│   ├── atomic.aiml
│   ├── badanswer.aiml
│   ├── biography.aiml
│   ├── bot.aiml
│   ├── bot_profile.aiml
│   ├── client.aiml
│   ├── client_profile.aiml
│   ├── computers.aiml
│   ├── continuation.aiml
│   ├── date.aiml
│   ├── default.aiml
│   ├── drugs.aiml
│   ├── emotion.aiml
│   ├── food.aiml
│   ├── geography.aiml
│   ├── gossip.aiml
│   ├── history.aiml
│   ├── humor.aiml
│   ├── imponderables.aiml
│   ├── inquiry.aiml
│   ├── interjection.aiml
│   ├── iu.aiml
│   ├── junktest.text
│   ├── knowledge.aiml
│   ├── literature.aiml
│   ├── loebner10.aiml
│   ├── money.aiml
│   ├── movies.aiml
│   ├── mp0.aiml
│   ├── mp1.aiml
│   ├── mp2.aiml
│   ├── mp3.aiml
│   ├── mp4.aiml
│   ├── mp5.aiml
│   ├── mp6.aiml
│   ├── music.aiml
│   ├── numbers.aiml
│   ├── personality.aiml
│   ├── phone.aiml
│   ├── pickup.aiml
│   ├── politics.aiml
│   ├── primeminister.aiml
│   ├── primitive-math.aiml
│   ├── psychology.aiml
│   ├── pyschology.aiml
│   ├── reduction0.safe.aiml
│   ├── reduction1.safe.aiml
│   ├── reduction2.safe.aiml
│   ├── reduction3.safe.aiml
│   ├── reduction4.safe.aiml
│   ├── reduction.names.aiml
│   ├── reductions-update.aiml
│   ├── religion.aiml
│   ├── salutations.aiml
│   ├── science.aiml
│   ├── sex.aiml
│   ├── sports.aiml
│   ├── stack.aiml
│   ├── standard.brn
│   ├── startup.xml
│   ├── startup.xml~
│   ├── stories.aiml
│   ├── that.aiml
│   ├── update1.aiml
│   ├── update_mccormick.aiml
│   ├── wallace.aiml
│   └── xfind.aiml
├── launch
│   ├── start_chat.launch
│   ├── start_speech_chat.launch
│   └── start_tts_chat.launch
├── package.xml
└── scripts
    ├── aiml_client.py
    ├── aiml_server.py
    ├── aiml_speech_recog_client.py
    └── aiml_tts_client.py
```



##### 安装PyAIML
```bash
sudo apt-get install python-aiml

```

##### 测试是否安装成功
```bash
python

# 进入python环境之后输入下面程序
>>> import aiml

```
当没有出现任何错误信息的时候，说明已经安装成功了。

### 测试功能
使用下面命令于AIML解释器进行交互
```bash
roslaunch ros_aiml start_chat.launch
```
使用下面命令于AIML解释器进行交互,答复将转换为语音：
```bash
roslaunch ros_aiml start_tts_chat.launch
```
启动语音识别和TTS：
```bash
roslaunch ros_aiml start_speech_chat.launch 
```
手动输入语音测试：
```bash
rostopic pub /recognizer/output std_msgs/String "data: 'Hello'"
```







