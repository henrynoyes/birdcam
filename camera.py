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
        today_date = datetime.now().strftime("%m%d%Y-%H%M%S")
        print(self.vs.capture_file(today_date+self.file_type))
        
    def clip(self):
        date = datetime.now().strftime("%m%d%Y-%H%M%S")

def push_phone():
    app_key = Path('push/app_key.txt').read_text()
    user_key = Path('push/user_key.txt').read_text()
    ts = datetime.now().strftime('%H:%M %p')

    po = Pushover(app_key)
    po.user(user_key)

    msg = po.msg(f'Motion Detected at {ts}\nhttps://10.0.0.240:8000')
    msg.set('title', 'BirdCam Alert!')
    po.send(msg)
    print('sent push notification')

def det_motion(curr_img, prev_img, buffer):
    curr_gray = cv2.cvtColor(curr_img, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.cvtColor(prev_img, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(curr_gray, prev_gray)
    diff = cv2.dilate(diff, np.ones((5,5)), 1)
    
    thresh = cv2.threshold(diff, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if any(cv2.contourArea(contour) > 3000 for contour in contours) and buffer > 120:
        print(f'Motion Detected! | {buffer}')
        #TODO push phone
        # push_phone()
        # x, y, w, h = cv2.boundingRect(contour)
        # print(x,y,w,h)
        buffer = 0
    buffer += 1
    return buffer


