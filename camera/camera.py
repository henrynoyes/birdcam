import time
import io
from libcamera import Transform, controls
from picamera2 import Picamera2
from datetime import datetime


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
        