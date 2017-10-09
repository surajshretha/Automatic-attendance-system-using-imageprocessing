from __future__ import division
import numpy as np
import os
import cv2
import pymysql
import time

from array import *

timeout=time.time() + 60*1

conn = pymysql.connect(host='localhost',database='major',user='root',password='7777')
a = conn.cursor()
i= raw_input('enter day :')
s=[]
e=[]
r=[]
sql='UPDATE atnd SET {} = "1" WHERE Id IN %s'
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer()
rec.load('recognizer/trainingdata.yml')
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,4,1,0,2)
id= [0]
b=[]

while 1:

    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,255))
    cv2.imshow('img',img)
    b.append(id)
    if(cv2.waitKey(1) == ord('q')):
        break;
    else:
        if time.time()> timeout:
            break;

cap.release()
cv2.destroyAllWindows()

for j in b:
       if j not in s:
          s.append(j)

lft=400
for m in s:
    temp=b.count(m)
    if temp >= 100:
        percent=(temp/lft)*100
        e.append(m)
        r.append(percent)
#print s
print b.count(1)
print b.count(2)
print e
print('accuracy')
print r
args=[e]
a.execute(sql.format(str(i)),args)
conn.commit()
conn.close()



