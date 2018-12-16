import cv2
import numpy as np

face_1 = np.load('user_1.npy').reshape(100, 50 * 50 * 3)
face_2 = np.load('user_1.npy').reshape(100, 50 * 50 * 3)

font = cv2.FONT_HERSHEY_COMPLEX

users = {
    0 : "Ravi",
    1 : "Unknown"
}

labels = np.zeros((200,1))
labels[0:100, :] = 0.0
labels[100:, :] = 1.0

data = np.concatenate([face_1, face_2])

def dist(x2, x1):
    return np.sqrt(sum((x2 - x1) ** 2))

def knn(x, train, k = 5):
    n = train.shape[0]
    distance = []
    for i in range(n):
        distance.append(dist(x,train[i]))

    distance = np.asarray(distance)
    index = np.argsort(distance)[:k]
    sortedLabels = labels[index]

    count = np.unique(sortedLabels, return_counts=True)
    return count[0][np.argmax(count[1])]

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    if ret:
        # print("Camera working")
        gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.2)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

            face = img[y:y+h, x:x+h, :]
            face = cv2.resize(face, (50,50))
            lab = knn(face.flatten(), data)
            user = users[int(lab)]
            cv2.putText(img, user, (x,y), font, 2, (0,0,255), 2)

        cv2.imshow('img', img)
        if cv2.waitKey(10) & 0xFF == 27:
            break

    else:
        print("Camera not working")

cv2.destroyAllWindows()
cam.release()







