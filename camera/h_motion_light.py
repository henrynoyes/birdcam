import cv2
import numpy as np

# def gen(camera):
#     # Establish video stream
#     prev_img = None
#     # buffer = 121
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#         curr_img = cv2.imdecode(np.frombuffer(frame, np.uint8), 1)
#         if type(prev_img) != np.ndarray:
#             prev_img = curr_img #first frame
#         # buffer = det_motion(curr_img, prev_img, buffer)
#         prev_img = curr_img

def det_motion(curr_img, prev_img, buffer):
    curr_grey = cv2.cvtColor(curr_img, cv2.COLOR_BGR2GRAY)
    prev_grey = cv2.cvtColor(prev_img, cv2.COLOR_BGR2GRAY)

    mse = np.square(np.subtract(curr_grey, prev_grey)).mean()
    if mse > 10 and buffer > 120:
        print(mse, buffer)
        buffer = 0
    buffer += 1
    return buffer

    # diff = cv2.absdiff(curr_grey, prev_grey)
    # diff = cv2.dilate(diff, np.ones((5,5)), 1)
    
    # thresh = cv2.threshold(diff, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
    # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # if any(cv2.contourArea(contour) > 3000 for contour in contours) and buffer > 120:
    #     print(f'Motion Detected! | {buffer}')
    #     #TODO push phone
    #     # push_phone()
    #     # x, y, w, h = cv2.boundingRect(contour)
    #     # print(x,y,w,h)
    #     buffer = 0
    # buffer += 1
    # return buffer


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    prev_img = None
    buffer = 121
    while True:
        ret, curr_img = cap.read()
        if type(prev_img) != np.ndarray:
            prev_img = curr_img
        buffer = det_motion(prev_img, curr_img, buffer)
        prev_img = curr_img

    cap.release()