import ChictopiaDownloader
import time
import cv2
import normalization
import numpy as np

# img = cv2.imread("Photos/dress/1174677.jpg")
img = cv2.imread("Photos/dress/1174990.jpg")
# img = cv2.imread("Photos/cara.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    print("x:" + str(x))
    print("y:" + str(y))
    print("w:" + str(w))
    print("h:" + str(h))
    roi_gray = gray[y:y + h, x:x + w]
    eye_zone = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        print("ex:" + str(ex))
        print("ey:" + str(ey))
        print("ew:" + str(ew))
        print("eh:" + str(eh))
        cv2.rectangle(eye_zone, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)


"""
def tiempo():
    return int(round(time.time() * 1000))


tiempo_empezar = tiempo()
ChictopiaDownloader.ChictopiaDownloader(1, 5)
tiempo_final = tiempo()

print(tiempo_final - tiempo_empezar)


## ejemplo de uso
# points = dec.predict_points(imagen, roi[0])
# r = dec.calculate_centroide(points, range(42, 48))
# i = dec.calculate_centroide(points, range(36, 42))
gray_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
normalizator = normalization.Normalization()
normalizator.normalize_gray_img(gray_image, i[0], i[1], r[0],
                                r[1], normalization.Kind_wraping.HS)
cv2.imwrite('normaHS.jpeg', normalizator.norm_image)
print(str(normalizator.angle_eyes) + ' ' + str(normalizator.dist_eyes) + '\n')
normalizator.normalize_gray_img(gray_image, normalization.i[0], normalization.i[1], normalization.r[0],
                                normalization.r[1], normalization.Kind_wraping.FACE)
cv2.imwrite('normaface.jpeg', normalizator.norm_image)
print(str(normalizator.angle_eyes) + ' ' + str(normalizator.dist_eyes) + '\n')
"""
