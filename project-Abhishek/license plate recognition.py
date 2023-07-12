from tkinter import Frame
import cv2
import numpy as np
import easyocr




capture = cv2.VideoCapture("projectvideo.mp4")
dataset = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

while True:

    ret,frame = capture.read()

    plates = dataset.detectMultiScale(frame,1.515)
    print(plates)
    for x,y,w,h in plates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 4)
    cv2.imshow('Output',frame)
    k = cv2.waitKey(8)
    if k == 27:
        break



capture.release()
cv2.destroyAllWindows()
