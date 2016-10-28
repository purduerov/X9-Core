How to set up multiple USB camera streaming to a server.
1. Install dependancies with
 sudo apt-get install libjpeg8-dev imagemagick libv41-dev

2. create symbolic link of video.h with
sudo ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h

3. take file directory mjpg-streamer, place where you want it

4.inside mjpg_streamer run
make mjpeg_streamer input_uvc.so output_http.so

5. change your .bash_rc to have
export LD_LIBRARY_PATH=/usr/local/lib/
reload your bash

6.you will need to edit the camera script to be have the directory after the  -o flag to be the directory of the html file on your server. For each camera you will need to add an lideanticel line for each additional camera, with different video name and port 

7.remember to edit the ip adress inside of the html file to the opene assigned by the router
 
8.run camera script to begin stream

9. To access the camera, go to the ip of the raspberry pi, and navigate to the html page where you  embedded the video stream
