from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera, det_motion, light, push_img
import cv2
import numpy as np

# Establish stream
pi_camera = VideoCamera()

app = Flask(__name__, static_folder='./static/')

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    # Establish video stream
    prev_img = None
    buffer = 2900
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        curr_img = cv2.imdecode(np.frombuffer(frame, np.uint8), 0)
        if type(prev_img) != np.ndarray:
            prev_img = curr_img #first frame
        # buffer = light(curr_img, prev_img, buffer)
        if buffer % 500 == 0:
            push_img(frame)
        prev_img = curr_img
        buffer += 1

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
