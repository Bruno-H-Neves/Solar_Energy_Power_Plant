import cv2
import numpy as np
import pickle
import os
import PySimpleGUI as sg
from Function_BN  import script,InverterAcDc,Transformer,Header

he=Header()
width,height=107,15
nb=900
colorR=(50,0,200)
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

auto= script()

if auto==1:
    posList=[]  
    y=50
    for i in range(22):
        if i!=0:
            y=y+height+10
        posList.append((100,y))
        posList.append((600,y))
    img=cv2.imread("workspace.jpg")
    scale=img.shape[0]/img.shape[1]
    img = cv2.resize(img,(nb,int(nb*scale)))
    he.leftH(image=img)

    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),colorR,2)
        cv2.line(img,(pos[0],pos[1]+int(height/2)),(pos[0]-50,pos[1]+int(height/2)),colorR,2)
    Inverter=InverterAcDc(img=img,colorInv=colorR,fpoint=(275,100))
    text1="PLANT 1"
    Inverter.draw(text1)
    cv2.line(img,(50,575+int(height/2)),(50,30),colorR,2)
    cv2.line(img,(50,30),(300,30),colorR,2)
    cv2.line(img,(300,30),(300,100),colorR,2)
    Inverter.draw(text1)
    text2="PLANT 2"
    cv2.line(img,(550,575+int(height/2)),(550,30),colorR,2)
    cv2.line(img,(550,30),(450,30),colorR,2)
    cv2.line(img,(450,30),(450,100),colorR,2)
    Inverter=InverterAcDc(img=img,colorInv=colorR,fpoint=(425,100))
    cv2.line(img,(450,125),(450,150),colorR,2)
    cv2.line(img,(450,150),(400,150),colorR,2)
    cv2.line(img,(400,150),(400,280),colorR,2)

    cv2.line(img,(300,125),(300,150),colorR,2)
    cv2.line(img,(300,150),(350,150),colorR,2)
    cv2.line(img,(350,150),(350,280),colorR,2)

    cv2.line(img,(325,280),(425,280),colorR,3)
    cv2.line(img,(375,280),(375,320),colorR,3)
    transf=Transformer()
    rad=int(30)
    transf.draw(img=img,point=(375,320),radius=rad,color=colorR)
    cv2.line(img,(375,int(320+(3.4*rad))),(375,int(320+(3.4*rad)+100)),colorR,2)




    Inverter.draw(text2)
    cv2.imshow("Image",img)
    while True:
        key = cv2.waitKey(1)   
        if key == 27 or key==ord('q'): 
            break

else:
    while True:
        img=cv2.imread("workspace.jpg")
        scale=img.shape[0]/img.shape[1]
        img = cv2.resize(img,(nb,int(nb*scale)))
        for pos in posList:
            cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),colorR,1)
        cv2.imshow("Image",img)
        cv2.setMouseCallback("Image",mouseClick)
        key = cv2.waitKey(1)   
        if key == 27 or key==ord('q'): 
            break
print(posList)
folder = sg.popup_get_folder('File Name','File Search')   
os.chdir(folder)
cv2.imwrite("Solar_Plant.jpg", img)
print(posList)
cv2.destroyAllWindows()
