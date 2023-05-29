from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera, light, push_img
import cv2
import numpy as np

# Establish stream
pi_camera = VideoCamera()

app = Flask(__name__, static_folder='./static/')

@app.route('/')
def main_page():
    return render_template('main.html')

def gen(camera):
    # Establish video stream
    # prev_img = None
    # buffer = 150
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        # curr_img = cv2.imdecode(np.frombuffer(frame, np.uint8), 0)
        # if type(prev_img) != np.ndarray:
        #     prev_img = curr_img #first frame
        # buffer = light(prev_img, curr_img, buffer, frame)
        # prev_img = curr_img

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/motion')
# def modec_page():
#     return render_template('motion.html')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
