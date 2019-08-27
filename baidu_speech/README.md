### 依赖
```bash
sudo pip install baidu_api
sudo pip install playsound
python -m pip install pyaudio
pip install python-vlc
```
### 语音合成

```bash
roslaunch baidu_speech simple_speaker.launch 

rostopic pub /speak_string std_msgs/String -- '小谷小谷'
```

### 语音识别

```bash

roslaunch baidu_speech simple_voice.launch

```

### 语音识别及合成
```bash
roslaunch baidu_speech simple_voice.launch

rosrun baidu_speech baidu_tts.py
```









