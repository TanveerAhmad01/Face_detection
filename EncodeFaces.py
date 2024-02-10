import cv2

import os
import pickle

#     import Faces
floderFacesPath = 'Resources/Faces'
facePathList = os.listdir(floderFacesPath)
faceList = []
FacesIds = []
for path in facePathList:
    faceList.append(cv2.imread(os.path.join(floderFacesPath,path)))
    remove_text = os.path.splitext(path)[0]
    FacesIds.append(remove_text)
    print(FacesIds)
print(len(faceList))