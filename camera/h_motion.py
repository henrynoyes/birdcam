import cv2
import numpy as np

cap = cv2.VideoCapture(0)
prev_img = None
while True:
    ret, curr_img = cap.read()
    cv_img = curr_img.copy()
    if type(prev_img) != np.ndarray:
        prev_img = curr_img
    
    curr_gray = cv2.cvtColor(curr_img, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.cvtColor(prev_img, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(curr_gray, prev_gray)
    diff = cv2.dilate(diff, np.ones((5,5)), 1)
    
    thresh = cv2.threshold(diff, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 2000:
            print('Motion Detected!')
            x, y, w, h = cv2.boundingRect(contour)
            print(x,y,w,h)
            cv2.rectangle(cv_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Motion Detection', cv_img)
    prev_img = curr_img

    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()