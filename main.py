from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera, det_motion
import cv2
import os
import numpy as np

# Establish stream
pi_camera = VideoCamera()

app = Flask(__name__, static_folder='./static/')

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    # Establish video stream
    mog = cv2.createBackgroundSubtractorMOG2()
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        print('yielded')
        img = cv2.imdecode(np.frombuffer(frame, np.uint8), 1)
        det_motion(img, mog)
        # push phone

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
