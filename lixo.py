import cv2

img=cv2.imread("workspace.jpg")
print(img.shape)
scale=img.shape[0]/img.shape[1]
nb=900
imgResize = cv2.resize(img,(nb,int(nb*scale))) 
print(imgResize.shape)