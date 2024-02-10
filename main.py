import os
import cv2
image_cap = cv2.VideoCapture(0)

image_cap.set(3,640)
image_cap.set(4,480)
background_Image = cv2.imread('Resources/Background.png')


#     import modes images into list
floderModePath = 'Resources/Modes'
modePathList = os.listdir(floderModePath)
imageModePath = []
for path in modePathList:
    imageModePath.append(cv2.imread(os.path.join(floderModePath,path)))


imageModePath_resized = cv2.resize(imageModePath[3], (414, 633))
while True:
    success, image_data = image_cap.read()
    background_Image[162:162+480, 55:55+640] = image_data
    background_Image[44:44+633, 804:804+414] = imageModePath_resized
    cv2.imshow("face detection", background_Image)
    if cv2.waitKey(1) == ord("a"):
        break

cv2.destroyAllWindows()
