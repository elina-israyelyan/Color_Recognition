#!/usr/bin/env python
# coding: utf-8

# In[28]:


import cv2
import pandas as pd

df = pd.read_csv(r"C:\Users\elina\Desktop\inch anel erb tane menak es\colors_names_.csv")
img = None
while img is None:
    img_in = input("Please provide the correct path of the picture: ")
    img = cv2.imread(img_in)


def simcolor(xpoint, ypoint):
    minim = 1000
    for i in range(len(df) - 1):
        d = sum(list(abs(img[ypoint, xpoint] - [df.loc[i, "b"], df.loc[i, "g"], df.loc[i, "r"]])))
        if d < minim:
            minim = d
            stringish = str(df["name"][i])
    return stringish


def recog_color(event, x, y, flags, param):
    global xpoint
    global ypoint
    if event == cv2.EVENT_LBUTTONDOWN:
        xpoint, ypoint = x, y
        stringish = simcolor(xpoint, ypoint)
        cv2.rectangle(img, (0, 0), (500, 50), (150, 170, 200), -1)
        cv2.putText(img, f"color:{stringish}", (7, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)


cv2.namedWindow('my_img')
cv2.setMouseCallback('my_img', recog_color)
while True:
    cv2.imshow("my_img", img)
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        cv2.destroyAllWindows()
        break





