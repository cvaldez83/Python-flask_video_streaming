#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from flask_basicauth import BasicAuth
from main import PiThing
import time #CV
import credentials
import wave
import pyaudio #CV added
chunk = 1024

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
app.config['FILEDIR'] = 'static/_files/' #CV added

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
        # print(time.time())
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# @socketio.on('play-recording', namespace='/audio')
# def play_recording():
#     '''stream audio to server''' #CV
#     print('FUNCTION play_recording STARTED')
#     wf = wave.open(current_app.config['FILEDIR'] + session['wavename'], 'rb')
#     print('OPENED WAVE FILE')
#     print('NUMBER OF FRAMES')
#     print(wf.getnframes())
#     p = pyaudio.PyAudio() #CV
#     print('CREATED PY AUDIO OBJECT P')
#     stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), #CV
#                 channels = wf.getnchannels(),   #CV
#                 rate = 48000,   #CV
#                 output = True)  #CV

#     print('CREATED STREAM')
#     data = wf.readframes(chunk) #CV
#     print('CREATED DATA')

#     #Play audio data
#     while data != b'':              #CV
#         stream.write(data)          #CV
#         data = wf.readframes(chunk) #CV
#     print('PLAYED AUDIO DATA')
    

#     #Closing statements
#     print('DELETING WAV FILE: ' + session['wavename'])
#     os.remove(current_app.config['FILEDIR'] + session['wavename'])
#     wf.close()
#     print('CLOSED WAVE')
#     stream.close()  #CV
#     print('CLOSED STREAM')
#     p.terminate()   #CV
#     print('TERMINATED AUDIO OBJECT P')
#     del session['wavename']
#     print('DELETED SESSION')



if __name__ == '__main__':
    cf = 'cert.pem'
    kf = 'key.pem'
    # app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
    app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=(cf, kf))
    # socketio.run(app, host='0.0.0.0', port=443, certfile=cf, keyfile=kf)