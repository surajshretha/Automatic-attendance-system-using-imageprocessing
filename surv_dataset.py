import numpy as np
import cv2
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
id = raw_input('enter your id')
sampleNum=0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sampleNum=sampleNum+1
        cv2.imwrite("surv_dataset/User."+str(id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

    cv2.imshow('surv_dataset',img)
    cv2.waitKey(1)
    if(sampleNum>100):
        break

cap.release()
cv2.destroyAllWindows()

