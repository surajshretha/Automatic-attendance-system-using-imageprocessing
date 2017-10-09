import os
import cv2
import numpy as np
from PIL import Image
recognizer = cv2.createLBPHFaceRecognizer()
path='surv_dataset'

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNP = np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNP)
        IDs.append(ID)
        cv2.imshow('training', faceNP)
        cv2.waitKey(10)
    return IDs, faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('compiled/compiled.yml')
cv2.destroyAllWindows()
