import cv2
import numpy as np
import os
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "../libs/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

_from = os.path.join('data', 'from')
_to = os.path.join('data', 'to')

_id = int(input("Enter Person Id to Identify : "))
_from = input("Path of Source folder (DEFAULT: ./data/from ") or _from
_to = input("Path of Destinamtion folder (DEFAULT: ./data/to ") or _to

files = [f for f in os.listdir(_from)]
for file in files:
    img = cv2.imread(os.path.join(_from, file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100),
    )

    for(x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if (confidence < 100):
            if(id == _id):
                print('[ match found ] ', file)
                cv2.imwrite(os.path.join(_to, file), img)
            else:
                print('[ not this ]    ', file)
        else:
            print('[ unknown ]     ', file)
