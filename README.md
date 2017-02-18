# X9-Core
All of X9's core software for the 2016-2017 Purdue ROV team.

###To install python and Flask app:
1. install core packages and dependencies:
 sudo apt-get install gcc-4.7 python python-dev python-pip virtualenv python-smbus libffi-dev

2. install virtualenv (again?)
 sudo pip install virtualenv

3. create new virtualenv to manage python packages (creates folder 'venv'):
 virtualenv venv

4. activate virtual environment:
 . venv/bin/activate

5. install python packages:
 pip install -r requirements.txt

6. apply sudo to pip installation if any fail due to permissions

7. make sure all packages are installed and flask runs with:
 export FLASK_APP=application.py
 flask run --host=0.0.0.0

8. stop using virtual environment with:
 deactivate

###To install mjpg-streamer:
1. install dependencies with
 sudo apt-get install libjpeg8-dev imagemagick libv4l-dev cmake

2. create symbolic link of video.h with
 sudo ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h

3. inside mjpg-streamer run
 sudo make
 AND
 sudo make install

4. create environment variable to installed .so files (could insert it into .bashrc):
 export LD_LIBRARY_PATH=/usr/local/lib/

5. If problems persist, make .so files in /usr/local/lib have all permissions:
 sudo chmod 777 *.so (when in /usr/local/lib/mjpg-streamer/ directory)

6. Stick an iframe in html: <iframe src="http://10.42.0.?:8080/?action=stream" width="1024" height="768" scrolling="no" frameborder="no" marginheight="0px" position"absolute" css="right=0; top=0;"></iframe>

###To install i2c for Pi:
1. install dependencies with
 sudo apt-get install python-smbus i2c-tools

2. edit /boot/config.txt (may need sudo) adding the line (if not already there and uncommented):
 device_tree_param=i2c_arm=on

3. edit /boot/cmdline.txt (may need sudo) adding the line (if not already there and uncommented):
 bcm2708.vc_i2c_override=1

4. edit /etc/modules-load.d/raspberrypi.conf (may need sudo) adding the lines (if not already there and uncommented):
 i2c-bcm2708
 i2c-dev

5. reboot Pi with:
 sudo reboot

6. test with (should print out i2c addresses of devices attached to the i2c line):
 i2cdetect -y 1

###To install node and Vue:
1. it looks like npm needs a library provided by adafruit, so run: _curl -sLS https://apt.adafruit.com/add | sudo bash_

2. The vue we're using is a node module, so just run: _sudo apt-get install nodejs npm_

3. now, navigate to _X9-Core/frontend/_ and run _npm install_

4. once that's done, just run _npm run build_ to condense the files for the webpage
