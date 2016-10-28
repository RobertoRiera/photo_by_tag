import ChictopiaDownloader
import time
import cv2
import numpy as np


img = cv2.imread("Photos/bag/1174677.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)
"""
compu

def tiempo():
    return int(round(time.time() * 1000))


tiempo_empezar = tiempo()
ChictopiaDownloader.ChictopiaDownloader(1, 5)
tiempo_final = tiempo()

print(tiempo_final - tiempo_empezar)
"""