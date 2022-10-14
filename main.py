import time
import cv2
import cvzone
import streamlit as st
import HandTrackingModule as htm
import mediapipe as mp
st.title("snap dude")

camera = st.button("turn ON camera")
close=st.button("turn OFF camera")

filters = st.selectbox("Filters", ['sunglass','pirate','star','glasses','download','anny'])
detection = st.selectbox("Detection", ['detect_hands','detect_faces'])
FRAME_WINDOW = st.image([])
detector=htm.handDetector()

while camera:

    cam = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    overlay = cv2.imread(filters + '.png',cv2.IMREAD_UNCHANGED)
    while True:
        ret, frame = cam.read()

        #detector.findHands(frame)
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_scale)
        for (x, y, w, h) in faces:

            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if filters=="glasses":
                overlay_resize = cv2.resize(overlay, (w,h))
                frame = cvzone.overlayPNG(frame, overlay_resize,[x, y])
            if filters=="sunglass":
                overlay_resize = cv2.resize(overlay, (w,h))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x,y])
            if filters=="star":
                overlay_resize = cv2.resize(overlay, (w,h))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x,y])
            if filters=="anny":
                overlay_resize = cv2.resize(overlay, (w,h))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x,y])
            if detection=='detect_faces':
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if detection=='detect_hands':
                detector.findHands(frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        time.sleep(0)

