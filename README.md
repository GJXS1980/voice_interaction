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
sudo apt-get install python3-pip
pip install git+https://github.com/Baidu-AIP/python-sdk.git@master
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

##### 聊天机器人（百度语音加图灵机器人）
```bash
roslaunch baidu_speech voice_speech.launch

roslaunch baidu_speech Chat_Robot.launch
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
cd pocketsphinx/deb/
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


### 科大讯飞语音交互

##### 依赖安装
```bash
sudo apt-get update

sudo apt-get install libasound2-dev 
```

##### 源码下载及编译
```bash
cd xf-ros/xfei_asr/lib
sudo cp libmsc.so /usr/lib/

cd ~/catkin_ws
catkin_make
```
##### 语音唤醒




##### 语音采集
```bash
roslaunch audio_collect audio_collect.launch

# 调用服务
rosservice call /collect 1

# 播放录制的音频
cd /home/gjxs/.ros/source/AIUI/audio/1.wav
```

##### 语音识别
```bash
roscore 

rosrun xf_ros iat_publish

rostopic pub /voiceWakeup std_msgs/String "data: 'hello'"
```

##### 语义识别
```bash


roslaunch aiui_semantic aiui_semantic.launch 

rosservice call /aiui '/home/gjxs/.ros/source/AIUI/audio/tts.wav' 

```



##### 语音合成

```bash
roscore 

rosrun xf_ros tts_subscribe

rostopic pub /voiceWords std_msgs/String "data: 'hello'" 
```

```bash
# 替换speech_synthesis/libs/libmsc.so文件
# 修改speech_synthesis/src/tts_test.cpp文件的appid
roslaunch speech_synthesis speech_synthesis.launch 

rosservice call /tts "text: '广州天气'" 
```


##### 语音小助手
```bash
roscore 

rosrun xf_ros iat_publish

rosrun xf_ros voice_assistant

rostopic pub /voiceWakeup std_msgs/String "data: 'hello'"
```



### snowboy语音唤醒
安装依赖
```bash
sudo apt-get install python-pyaudio python3-pyaudio sox
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
sudo apt-get install libatlas-base-dev
pip install pyaudio
sudo apt-get install libpcre3 libpcre3-dev

```
安装swing
```bash
wget http://downloads.sourceforge.net/swig/swig-3.0.10.tar.gz

cd swig-3.0.10

./configure --prefix=/usr                  \
        --without-clisp                    \
        --without-maximum-compile-warnings &&
make
sudo make install &&
sudo install -v -m755 -d /usr/share/doc/swig-3.0.10 &&
sudo cp -v -R Doc/* /usr/share/doc/swig-3.0.10
```
安装atlas
```bash
sudo apt-get install libatlas-base-dev
```

输入下面命令测试是否正常录音：
```bash
# 录音
rec test.wav

# 播放
play test.wav

```
编译节点插件：
```bash
sudo apt-get install libmagic-dev libatlas-base-dev

npm install
./node_modules/node-pre-gyp/bin/node-pre-gyp clean configure build
```

下载源码
```bash
git clone https://github.com/Kitt-AI/snowboy.git

```

```bash
cd snowboy/swig/Python

# 编译引擎库
make

```
测试：
```bash
cd snowboy/examples/Python

python demo.py ./resources/models/snowboy.umdl
```

##### 自定义唤醒词
首先登陆到官网注册账号：https://snowboy.kitt.ai/


### hark
##### 安装hark
```bash
# 添加源码源
sudo bash -c 'echo -e "deb http://archive.hark.jp/harkrepos $(lsb_release -cs) non-free\ndeb-src http://archive.hark.jp/harkrepos $(lsb_release -cs) non-free" > /etc/apt/sources.list.d/hark.list'

# 设置GPG密钥
wget -q -O - http://archive.hark.jp/harkrepos/public.gpg | sudo apt-key add -

# node.js安装
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs

# 更新源
sudo apt update

# 安装hark
sudo apt install hark-base harkmw hark-core
sudo apt install hark-designer
sudo apt install harktool5 harktool5-gui
sudo apt install kaldidecoder-hark
```

[安装教程](https://www.hark.jp/install/linux/)

[HARK-ROS安装教程](https://www.hark.jp/packages/ros/turtlebot/)


##### HARK-ROS使用

[使用教程1](https://www.hark.jp/packages/ros/)

[使用教程2](https://www.hark.jp/packages/ros/hark-ros-tutorials/)

[HARK-ROS-IROS2018使用教程](https://www.hark.jp/hark-ros-iros2018-tutorials/)


### rospeex

##### 源码下载编译
```bash
git clone https://bitbucket.org/rospeex/rospeex.git
```
[源码地址](https://bitbucket.org/rospeex/rospeex/src/master/)


### 图灵机器人的使用




### pip版本更新

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# python2
python get-pip.py

# python3
python3 get-pip.py


which pip 

pip

type pip

hash -r

```



