# Work in progress...

This forked version of Miguel Grinberg's flask-video-streaming repo has been modified to allow the use of two servos to pan and tilt the picamera.  Servos are controlled from client's web browser.  In addition, this repo also uses Miguel's socketio audio example (https://github.com/miguelgrinberg/socketio-examples/tree/master/audio) to allow one to transmit audio from client browser's microphone to raspberry pi.


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
