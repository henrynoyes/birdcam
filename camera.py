import time
import io
from datetime import datetime
import cv2 
from libcamera import Transform, controls
from picamera2 import Picamera2
import numpy as np
from pushover import Pushover
from pathlib import Path

class VideoCamera(object):
    def __init__(self, file_type=".jpg", photo_string="stream_photo"):
        tune = Picamera2.load_tuning_file("/usr/share/libcamera/ipa/raspberrypi/imx219_noir.json")
        self.vs = Picamera2(tuning=tune)
        self.capture_config = self.vs.create_still_configuration()
        self.vs.configure(self.vs.create_preview_configuration({"size": (800, 600)}, transform=Transform(hflip=True, vflip=True)))
        self.vs.start()
        self.file_type = file_type
        self.photo_string = photo_string
        time.sleep(2.0)

    def __del__(self):
        print("STOP")

    def get_frame(self):
        jpeg = io.BytesIO()
        try:
            self.vs.capture_file(jpeg, format='jpeg')
        except RuntimeError:
            jpeg = self.previous_frame
        self.previous_frame = jpeg
        return jpeg.getbuffer()

    # Take a photo, called by camera button
    def take_picture(self):
        today_date = datetime.now().strftime("capture-%m%d-%H%M%S")
        print(self.vs.capture_file(today_date+self.file_type))
        
    def clip(self):
        date = datetime.now().strftime("%m%d%Y-%H%M%S")

def push_msg():
    app_key = Path('push/app_key.txt').read_text()
    user_key = Path('push/user_key.txt').read_text()
    ts = datetime.now().strftime('%I:%M %p')

    po = Pushover(app_key)
    po.user(user_key)

    msg = po.msg(f'Motion Detected at {ts}\nhttp://10.0.0.240:8000')
    msg.set('title', 'BirdCam Alert!')
    po.send(msg)
    print('sent push notification')

def push_img():
    pass
    # app_key = Path('push/app_key.txt').read_text()
    # user_key = Path('push/user_key.txt').read_text()
    # ts = datetime.now().strftime('%I:%M %p')

    # po = Pushover(app_key)
    # po.user(user_key)

    # msg = po.msg(f'Motion Detected at {ts}\nhttp://10.0.0.240:8000')
    # msg.set('title', 'BirdCam Alert!')
    # po.send(msg)
    # print('sent push notification')

def light(curr_img, prev_img, buffer):
    mse = np.square(np.subtract(curr_img, prev_img)).mean()
    if mse > 50 and buffer > 3600:
        print(mse, buffer)
        # push_msg()
        push_img
        buffer = 0
    buffer += 1
    return buffer