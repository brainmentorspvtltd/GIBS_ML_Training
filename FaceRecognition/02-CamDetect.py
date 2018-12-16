import cv2

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    if ret:
        # print("Camera working")
        gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
        faces = data.detectMultiScale(gray, 1.2)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

        cv2.imshow('img', img)
        # cv2.imshow('img', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break

    else:
        print("Camera not working")

cv2.destroyAllWindows()
cam.release()