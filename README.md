# Work in progress...

This forked version of Miguel Grinberg's flask-video-streaming repo has been modified to allow the use of two servos to pan and tilt the picamera.  Servos are controlled from client's web browser.

Software Requirements:
- Python 3.5 or greater
- servoblaster (https://github.com/richardghirst/PiBits/tree/master/ServoBlaster)

Hardware Requirements:
- Raspberry pi 3 or greater
- Raspberry pi camera module (example: https://www.raspberrypi.org/products/camera-module-v2/)
- Two 9gram servos of your choice
- tilt/pan servo bracket of your choice
- Small speaker of your choice
- USB-to-3.5mm jack adapter (example: https://www.amazon.com/Audio-Technica-ATR2USB-3-5mm-Audio-Adapter/dp/B00I6ILPPC)

Install steps:
- git clone this repo
- change directory by typing: cd Python-flask_video_streaming/
- run setup.sh from terminal by typing: . setup.sh
- create ssl files "key.pem" and "cert.pem" by typing: openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out cert.pem
- fill in the information to create the ssl files

Starting the app:
- Activate the python virtual environment by typing: . ae.sh
- Start the app by typing: . start.sh
