import sys
sys.path.append('./camera/')
from flask import Flask, render_template, Response, request, send_from_directory
from camera import det_motion
import os
import cv2
from io import BytesIO
import numpy as np

# Vertically flip video stream
# pi_camerea = VideoCamera()

app = Flask(__name__, static_folder='./static/')

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    # Establish video stream
    mog = cv2.createBackgroundSubtractorMOG2()
    while True:
        # frame = camera.get_frame()
        with open('static/living_room.jpg','rb') as im:
            jpg = BytesIO(im.read())
        frame = jpg.getbuffer()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        img = cv2.imdecode(np.frombuffer(jpg.read(), np.uint8), 1)
        det_motion(img, mog)
        # push phone

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    # pi_camera.take_picture()
    return "None"

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=False)
    app.run(host='127.0.0.1', port=8000, debug=False)