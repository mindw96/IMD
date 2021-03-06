import cv2
import numpy as np
from RetinaFace.retinaface import RetinaFace

gpuid = 0
# Road Face Detection Model
detector = RetinaFace('./model/R50', 0, gpuid, 'net3')

thresh = 0.8

sum_3 = 0
sum_4 = 0
sum_34 = 0

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Read Cam
while (True):
    ret, img = cap.read()
    #print(np.shape(img))
    faces, landmarks = detector.detect(img, thresh, scales=[1.0, 1.0], do_flip=True)

    if True:
        for i in range(faces.shape[0]):
            box = faces[i].astype(np.int)
            color = (0, 0, 255)

            # Mask detection based on landmarks
            if landmarks is not None:
                landmark5 = landmarks[i].astype(np.int)
                for l in range(landmark5.shape[0]):
                    if l == 3: # right
                        cv2.circle(img, (landmark5[l][0], landmark5[l][1]), 1, (0, 0, 255), 1)
                        rgb_3 = img[landmark5[l][0], landmark5[l][1]]
                        sum_3 = sum(rgb_3)
                        cv2.imshow('crop', faces)
                    elif l == 4: # left
                        cv2.circle(img, (landmark5[l][0], landmark5[l][1]), 1, (0, 0, 255), 1)
                        rgb_4 = img[landmark5[l][0], landmark5[l][1]]
                        sum_4 = sum(rgb_4)

                    sum_34 = sum_3 + sum_4

                    if sum_34 < 180:
                        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                        cv2.putText(img, 'Mask', (box[0], box[1] - 2), 0, 1, [0, 0, 0], thickness=3,
                                    lineType=cv2.FONT_HERSHEY_SIMPLEX)
                    else:
                        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)
                        cv2.putText(img, 'No Mask', (box[0], box[1] - 2), 0, 1, [0, 0, 0], thickness=3,
                                    lineType=cv2.FONT_HERSHEY_SIMPLEX)
            else:
                continue

    cv2.imshow('Face and Mask Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
