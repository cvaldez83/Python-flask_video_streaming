# Work in progress...

This forked version of Miguel Grinberg's flask-video-streaming repo has been modified to allow the use of two servos to pan and tilt the picamera.  Servos are controlled from client's web browser.

## Hardware

Hardware Requirements:
- Raspberry pi 3 or greater
- Raspberry pi camera module (example: https://www.raspberrypi.org/products/camera-module-v2/)
- Two 9gram servos of your choice
- tilt/pan servo bracket of your choice
- Small speaker of your choice
- USB-to-3.5mm jack adapter (example: https://www.amazon.com/Audio-Technica-ATR2USB-3-5mm-Audio-Adapter/dp/B00I6ILPPC)

Setup of Camera Servos:
- Install servo pin for tilting to GPIO 18
- Install servo pin for panning to GPIO 24

Setup of treat dispensing servo (Optional):
- Install servo pin for treat dispensing to GPIO 4

## Software

Software Requirements:
- Python 3.5 or greater
- servoblaster 

Installation steps:
- Install servoblaster by following link: https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
- git clone this repo
- change directory by typing: cd Python-flask_video_streaming/
- use a text editor to edit the "credentials.py" file.  Change the "login_u" and "login_p" to whatever you like.
- run setup.sh from terminal by typing: . setup.sh
- create ssl files "key.pem" and "cert.pem" by typing: openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out cert.pem
- fill in the information to create the ssl files
- setup port forwarding on your router to forward traffic coming from port 443 to your raspberry pi's port 443

Starting the app:
- Activate the python virtual environment by typing: . ae.sh
- Start the app by typing: . start.sh
- Now type in your public IP in the browser and you should see the page


