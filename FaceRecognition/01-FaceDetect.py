import cv2

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('image_1.jpg', cv2.COLOR_BGR2GRAY)
# print(img)
faces = data.detectMultiScale(img,1.3)
# print(faces)

for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)

cv2.imwrite('result.jpg',img)