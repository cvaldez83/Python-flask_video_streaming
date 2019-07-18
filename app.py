#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from flask_basicauth import BasicAuth
from main import PiThing
import time #CV
import credentials

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera #CV: uncommented this
# from camera_opencv import Camera #CV: use this for usb camera 

# Create flask app and pi thing
app = Flask(__name__)
pi_thing = PiThing()

app.config['BASIC_AUTH_USERNAME'] = credentials.login_u
app.config['BASIC_AUTH_PASSWORD'] = credentials.login_p
app.config['BASIC_AUTH_FORCE'] = True #protects entire site
basic_auth = BasicAuth(app)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/dispense', methods=['POST'])
def dispense():
    print("Dispensing...")
    pi_thing.dispense_treat()
    return ('', 204)

@app.route('/up', methods=['POST'])
def camera_up():
    pi_thing.camera_up()
    return ('', 204)

@app.route('/down', methods=['POST'])
def camera_down():
    pi_thing.camera_down()
    return ('', 204)

@app.route('/right', methods=['POST'])
def camera_right():
    pi_thing.camera_right()
    return ('', 204)

@app.route('/left', methods=['POST'])
def camera_left():
    pi_thing.camera_left()
    return ('', 204)

@app.route('/servo_stop', methods=['POST'])
def servo_stop():
    pi_thing.servo_stop()
    return ('', 204)

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=False)