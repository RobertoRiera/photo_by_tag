import ChictopiaDownloader
import time
import cv2

print(cv2.__version__)

image = cv2.imread("Photos/bag/1174677.jpg")

cv2.imshow("Bag", image)
cv2.waitKey(0)

"""
def tiempo():
    return int(round(time.time() * 1000))

tiempo_empezar = tiempo()
ChictopiaDownloader.ChictopiaDownloader(1, 2)
tiempo_final = tiempo()

print(tiempo_final-tiempo_empezar)
"""