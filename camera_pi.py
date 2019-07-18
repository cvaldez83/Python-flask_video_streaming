import io
import time
import picamera
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            camera.rotation = 180         #CV: added
            camera.resolution = (640, 360) #CV: added
            # camera.resolution = (1280, 720) #CV: added
            # camera.framerate = 10          #CV: added
            #camera.brightness = 60         #CV: added
            #camera.contrast =  50          #CV: added
            camera.exposure_mode = 'night'
            # a=time.time()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                # print(time.time()-a)
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
