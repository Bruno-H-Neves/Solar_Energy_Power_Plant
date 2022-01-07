import cv2
import numpy as np
import pickle
import os
import PySimpleGUI as sg

width,height=107,15

try:
    with open('Solar_Plant','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1= pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('Solar_Plant','wb') as f:
        pickle.dump(posList,f)

nb=900
while True:
    img=cv2.imread("workspace.jpg")
    scale=img.shape[0]/img.shape[1]
    img = cv2.resize(img,(nb,int(nb*scale)))
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width, pos[1]+height), (50,0,200),2)
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)
    key = cv2.waitKey(1)   
    if key == 27 or key==ord('q'): 
        break
folder = sg.popup_get_folder('File Name','File Search')   #4
os.chdir(folder)
cv2.imwrite("Solar_Plant.jpg", img)
print(posList)
cv2.destroyAllWindows()
