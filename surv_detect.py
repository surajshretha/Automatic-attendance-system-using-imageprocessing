from __future__ import division
import os
import numpy as np
import cv2
import datetime
import pygame
from pygame import mixer



from array import *

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0);
rec = cv2.createLBPHFaceRecognizer();
rec.load('compiled/compiled.yml')
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)
id = 0
b=[]
c=[]
while 1:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if (conf<100):
            if (id==1):
                id=1
                b.append(id)
                temp1=b.count(id)
                if temp1 in (20,40,60,80,100,120,140,160,180,200,220,240,260,280,300):
                    print "known"
                    sub_face = img[y:y+h, x:x+w]
                    time=datetime.datetime.now()
                    print time
                    FaceFileName = "known/face_" + str(time) + ".jpg"
                    cv2.imwrite(FaceFileName, sub_face)
                    
                    
        else:
            id = 0
            if (id==0):
                c.append(id)
                temp2=c.count(id)
                if temp2 in (20,40,60,80,100,120,140,160,180,200,220,240,260,280,300):
                    print "unknown"
                    sub_face = img[y:y+h, x:x+w]
                    time=datetime.datetime.now()
                    print time
                    FaceFileName = "unknown/face_" + str(time) + ".jpg"
                    cv2.imwrite(FaceFileName, sub_face)
                    if temp2 in (20,40,60,80,100,120,140,160,180,200,220,240,260,280,300):
                        mixer.init()
                        mixer.music.load('a.mp3')
                        mixer.music.play()

                    

        cv2.cv.PutText(cv2.cv.fromarray(img), str(id), (x, y + h), font, 255);

    cv2.imshow('img', img)
    if (cv2.waitKey(10) == ord('q')):
        break;

    
cap.release()
cv2.destroyAllWindows()

