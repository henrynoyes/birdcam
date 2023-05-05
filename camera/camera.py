import time
import io
from datetime import datetime
import cv2 
# from libcamera import Transform, controls
# from picamera2 import Picamera2


# class VideoCamera(object):
#     def __init__(self, file_type=".jpg", photo_string="stream_photo"):
#         tune = Picamera2.load_tuning_file("/usr/share/libcamera/ipa/raspberrypi/imx219_noir.json")
#         self.vs = Picamera2(tuning=tune)
#         self.capture_config = self.vs.create_still_configuration()
#         self.vs.configure(self.vs.create_preview_configuration({"size": (800, 600)}, transform=Transform(hflip=True, vflip=True)))
#         self.vs.start()
#         self.file_type = file_type
#         self.photo_string = photo_string
#         time.sleep(2.0)

#     def __del__(self):
#         print("STOP")

#     def get_frame(self):
#         jpeg = io.BytesIO()
#         try:
#             self.vs.capture_file(jpeg, format='jpeg')
#         except RuntimeError:
#             jpeg = self.previous_frame
#         self.previous_frame = jpeg
#         return jpeg.getbuffer()

#     # Take a photo, called by camera button
#     def take_picture(self):
#         today_date = datetime.now().strftime("%m%d%Y-%H%M%S")
#         print(self.vs.capture_file(today_date+self.file_type))
        
#     def clip(self):
#         date = datetime.now().strftime("%m%d%Y-%H%M%S")

def det_motion(img, mog):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fgmask = mog.apply(gray)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask, kernel, iterations=1)
    
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        
        x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # print(x,y,w,h)
        