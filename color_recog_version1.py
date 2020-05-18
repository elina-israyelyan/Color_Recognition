#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import pandas as pd
import numpy as np
from statistics import mean

df= pd.read_csv(r"C:\Users\elina\Desktop\inch anel erb tane menak es\colors.csv", names=["name","Name","Number","r","g", "b"])
img = None
while img is None:
    img_in=input("Please provide the correct path of the picture: ")
    img = cv2.imread(img_in)
    
def recog_color(event,x,y,flags,param):
    global xpoint
    global ypoint
    if event == cv2.EVENT_LBUTTONDOWN:
        xpoint, ypoint = x,y
        start=np.array([0, 0, 0])
        result=None
        minim=[50,50,50]
        for i in range(5):
            for k in range(5):
                start = start+img[ypoint : ypoint+5 , xpoint : xpoint+5][i,k]
                result = start/25
        for i in range(len(df)-1):
            if list(abs(result - [df.iloc[i,3], df.iloc[i,4], df.iloc[i,5]]))<minim:
                minim = list(abs(result - [df.iloc[i,3], df.iloc[i,4], df.iloc[i,5]]))
                stringish=str(df["Name"][i])
        cv2.rectangle(img,(0,0),(400,50),(150,170,200),-1)
        cv2.putText(img, f"color:{stringish}" , (7,30), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 1)
        
cv2.namedWindow('my_img')
cv2.setMouseCallback('my_img', recog_color)
while True:
    cv2.imshow("my_img", img)
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        cv2.destroyAllWindows()
        break
        
                
        

