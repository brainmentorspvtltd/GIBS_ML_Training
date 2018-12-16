import cv2
import numpy as np

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
faceData = []
while True:
    ret, img = cam.read()
    if ret:
        # print("Camera working")
        gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
        faces = data.detectMultiScale(gray, 1.2)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

            face = img[y:y+h, x:x+h, :]
            face = cv2.resize(face, (50,50))

            if len(faceData) < 100:
                faceData.append(face)

        print(len(faceData))
        cv2.imshow('img', img)
        # cv2.imshow('img', gray)
        if cv2.waitKey(10) & 0xFF == 27 or len(faceData) >= 100:
            break

    else:
        print("Camera not working")

faceData = np.asarray(faceData)
np.save('user_1.npy', faceData)

cv2.destroyAllWindows()
cam.release()
