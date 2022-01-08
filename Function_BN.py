import PySimpleGUI as sg
import cv2
import datetime
import pytz
import psutil

def script():
    sg.theme('DarkGrey7')
    menu_def = [['&File', ['E&xit',]],
                ['&Help',['&Help','&About Us']]]
    layout = [[sg.Menu(menu_def, tearoff=True)],
              [sg.Button('Exit', size=(7, 1), font='Helvetica 14')],
              [sg.Radio('Manual', "RADIO1", key='-manual-', default=True, size=(5,1)), sg.Radio('Auto', "RADIO1",key='-auto-', size=(5,1))]]
    window = sg.Window('Select', layout, no_titlebar=True, location=(250,200),size=(500,200))

    while True:
        event , values = window.read(timeout=0)
        if event in ('Exit', None):
            break
        if values['-manual-']== True:
            auto=0
        elif values['-auto-']== True:
            auto=1 
    return auto

def sourceKey(posList,source_key,img,colorR,colorB,width,height):
    for idx,pos in enumerate(posList):
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),colorR,cv2.FILLED)
        cv2.line(img,(pos[0],pos[1]+int(height/2)),(pos[0]-50,pos[1]+int(height/2)),colorR,2)
        cv2.putText(img,source_key[idx],(pos[0]+5,pos[1]+height-5),cv2.FONT_HERSHEY_SIMPLEX,0.3,colorB,1)
    return img

class InverterAcDc():
    def __init__(self,img,fpoint,colorInv=(50,0,200)):
        self.img=img
        self.scalex=50
        self.scaley=25
        self.fpoint=fpoint
        self.lpoint=(int(self.fpoint[0]+(self.scalex)),int(self.fpoint[1]+self.scaley))   #(325,125)
        self. colorInv=colorInv

    def draw(self,text):
        cv2.rectangle(self.img,self.fpoint,self.lpoint,self.colorInv,2)
        cv2.line(self.img,self.fpoint,self.lpoint,self.colorInv,2)
        cv2.line(self.img,(self.lpoint[0]-15,self.fpoint[1]+5),(self.lpoint[0]-5,self.fpoint[1]+5),self.colorInv,1)
        cv2.line(self.img,(self.lpoint[0]-15,self.fpoint[1]+8),(self.lpoint[0]-5,self.fpoint[1]+8),self.colorInv,1)
        cv2.putText(self.img,'~',(self.fpoint[0]+3,122),cv2.FONT_HERSHEY_COMPLEX,0.5,self.colorInv,1)
        cv2.putText(self.img,text,(self.fpoint[0]-50,self.fpoint[1]+17),cv2.FONT_HERSHEY_SIMPLEX,0.35,self.colorInv,1)

class Transformer():
    def __init__(self):
        pass
    def draw(self,img,point,radius,color):
        center=(point[0],point[1]+radius)
        center2=(center[0],center[1]+int(radius*(1.4)))
        cv2.circle(img,center,radius,color,2)
        cv2.circle(img,center2,radius,color,2)

class Header():
    def __init__(self):
        pass

    def leftH(self,image, color=(0,0,0)):
        row=image.shape[1]
        col=image.shape[0]
        dt_now = datetime.datetime.now(tz= pytz.UTC)
        date=r'%s-%s-%s' %(dt_now.day,dt_now.month,dt_now.year)
        hour=r'%s:%s:%s' %(dt_now.hour,dt_now.minute,dt_now.second) 
        used_ram='Ram: %s'%(str(psutil.virtual_memory().used))
        battery = psutil.sensors_battery()
        bat_percent ='Bat: %s '%(str(battery.percent))
        cv2.rectangle(image,(int(row*0.8),0),(int(row),20),(100,100,100),cv2.FILLED)
        cv2.rectangle(image,(int(row*0.6),0),(int(row*0.8),20),(0,0,0),cv2.FILLED)
        cv2.rectangle(image,(int(row*0.29),0),(int(row*0.6),20),(250,100,150),cv2.FILLED)
        cv2.rectangle(image,(0,0),(int(row*0.29),20),(100,100,100),cv2.FILLED)
        cv2.putText(image,date,(int(row*0.615),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,255,50),1)
        cv2.putText(image,hour,(int(row*0.85),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,255,50),1)
        cv2.putText(image,used_ram,(int(row*0.295),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,0,50),1)
        cv2.putText(image,bat_percent,(0,15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,0,50),1)

