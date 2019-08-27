### 依赖
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

### 编译
```
cd ~/catkin_ws/
catkin_make
```


### 测试pocketsphinx的语音识别功能

```bash
roslaunch pocketsphinx robocup.launch
```
