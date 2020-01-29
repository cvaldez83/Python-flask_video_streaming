import RPi.GPIO as GPIO
import os
from time import sleep

PIN_DISPENSE = 4
SERVO_TILT = 2 # GPIO PIN 18
SERVO_PAN = 6 # GPIO PIN 24

# servoblaster limits: Units: 100 = 1ms
hilim_tilt_pos = 200.0   # full down (full down limit = 230)
lolim_tilt_pos = 100.0   # full up (full up limit = 70)

hilim_pan_pos = 230.0   # left limit (full left limit = 250)
lolim_pan_pos = 60.0   # right limit (full right limit = 50)

init_tilt_pos = 150   # Full Up: 100, Full Down: 200
init_pan_pos = 145    # Full Left: 10 , Full Right: 3

SERVO_DELAY = .1
PAN_INCREMENT = 34
TILT_INCREMENT = 20

def setServo(servoChannel, position):
    servoStr ="%u=%u" % (servoChannel, position)
    print("echo " + servoStr + " > /dev/servoblaster")
    os.system("sudo " + os.environ['HOME'] + "/PiBits/ServoBlaster/user/servod")
    os.system("echo " + servoStr + " > /dev/servoblaster")
    sleep(SERVO_DELAY)

class PiThing(object):
    '''RPi internet thing'''
    def __init__(self):
        # Setup
        print('__init__: Starting setup')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_DISPENSE, GPIO.OUT, initial=GPIO.LOW) #Dispense pin as output
        # Start servoblaster
        os.system("sudo " + os.environ['HOME'] + "/PiBits/ServoBlaster/user/servod")
        print('__init__: Set init_tilt_pos', init_tilt_pos)
        self.tilt = init_tilt_pos
        # setServo(SERVO_TILT, init_tilt_pos)
        self.pan = init_pan_pos
        print('__init__: Set init_pan_pos', init_pan_pos)
        # setServo(SERVO_PAN, init_pan_pos)

    @property
    def tilt(self):
        return self._tilt

    @tilt.setter
    def tilt(self, dc):
        #servo limit logic
        if lolim_tilt_pos <= dc <= hilim_tilt_pos:
            self._tilt = dc
            print('def tilt.setter: dc set to:', dc)
            print('def tilt.setter: Setting tilt...')
            setServo(SERVO_TILT, self._tilt)
        else:
            raise ValueError("Servo limit reached!")

    @property
    def pan(self):
        return self._pan

    @pan.setter
    def pan(self, dc):
        #servo limit logic
        if lolim_pan_pos <= dc <= hilim_pan_pos:
            self._pan = dc
            print('def pan.setter: dc set to:', dc)
            print('def pan.setter: Setting pan...')
            setServo(SERVO_PAN, self._pan)
        else:
            raise ValueError("Servo limit reached!")

    def dispense_treat(self):
        '''set dispense pin to on for a specific time'''
        GPIO.output(PIN_DISPENSE, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(PIN_DISPENSE, GPIO.LOW)

    def camera_up(self):
        '''Tilts camera up by set amount'''
        curr_pos = self.tilt
        print('def camera_up: curr_pos: ', curr_pos)
        new_pos = self.tilt - TILT_INCREMENT
        print('def camera_up: new_pos: ', new_pos)
        self.tilt = new_pos
        sleep(SERVO_DELAY)
        return None

    def camera_down(self):
        '''Tilts camera down by set amount'''
        curr_pos = self.tilt
        print('def camera_down: curr_pos: ', curr_pos)
        new_pos = self.tilt + TILT_INCREMENT
        print('def camera_down: new_pos: ', new_pos)
        self.tilt = new_pos
        sleep(SERVO_DELAY)
        return None

    def camera_left(self):
        '''Tilts camera left by set amount'''
        curr_pos = self.pan
        print('def camera_left: curr_pos: ', curr_pos)
        new_pos = self.pan + PAN_INCREMENT
        print('def camera_up: new_pos: ', new_pos)
        self.pan = new_pos
        sleep(SERVO_DELAY)
        return None

    def camera_right(self):
        '''Tilts camera right by set amount'''
        curr_pos = self.pan
        print('def camera_right: curr_pos: ', curr_pos)
        new_pos = self.pan - PAN_INCREMENT
        print('def camera_up: new_pos: ', new_pos)
        self.pan = new_pos
        sleep(SERVO_DELAY)
        return None
    
    def servo_stop(self):
        os.system("echo 2=0 > /dev/servoblaster")
        os.system("echo 6=0 > /dev/servoblaster")
        
