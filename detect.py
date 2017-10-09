from __future__ import division
import numpy as np
import cv2
import pymysql
import time

from array import *

timeout = time.time() + 60 * 1
conn = pymysql.connect(host='localhost', database='major', user='root', password='')
a = conn.cursor()
i = raw_input('enter day :')
s = []
e = []
r = []
sql = 'UPDATE atnd SET {} = "1" WHERE Id IN %s'

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0);
rec = cv2.createLBPHFaceRecognizer();
rec.load('recognizer/trainingdata.yml')
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)
id = 0
b = []

while 1:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if (conf<100):
            if id == 1:
                id = 1
            elif id == 2:
                id = 2
            elif id == 3:
                id = 3
            elif id == 4:
                id = 4
        else:
            id = 0
        cv2.cv.PutText(cv2.cv.fromarray(img), str(id), (x, y + h), font, 255);

        print id
        b.append(id)
    cv2.imshow('img', img)
    if (cv2.waitKey(10) == ord('q')):
        break;
    else:
        if time.time() > timeout:
            break;
cap.release()
cv2.destroyAllWindows()
for j in b:
    if j not in s:
        s.append(j)

lft = 450
for m in s:
    temp = b.count(m)
    if temp >= 100:
        percent = (temp / lft) * 100
        e.append(m)
        r.append(percent)
# print s
#print b.count(1)
#print b.count(0)
print e
print('accuracy')
print r
args = [e]
a.execute(sql.format(str(i)), args)
conn.commit()
conn.close()
