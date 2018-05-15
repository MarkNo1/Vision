import cv2
import numpy as np
import matplotlib.pyplot as plt

# WebCam
camera = 0
video_file = 'video.avi'
cap = cv2.VideoCapture(camera)  # or videofile
# Codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280, 720))

input = []
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('Gray', gray)
    input.append(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
