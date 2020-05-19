#!/usr/bin/env python
# coding: utf-8


import cv2
import pandas as pd

df = pd.read_csv("colors_names_.csv")
img = None
while img is None:  # asks the user to input the path till the path is right
    img_in = input("Please provide the correct path of the picture: ")
    img = cv2.imread(img_in)  # reads the image from the given path


def name_of_color(xpoint, ypoint):
    """ Calculates the difference between the color from the database and the image's (xpoint, ypoint) color.
    Returns the most similar color's hue name from the database"""
    minimum = 1000  # the minimum difference between color of the point and the color from the database
    for i in range(len(df) - 1):  # checks each row of df
        # d is the difference of color values(r,g,b) between the point from image and the color from df
        d = sum(list(abs(img[ypoint, xpoint] - [df.loc[i, "b"], df.loc[i, "g"], df.loc[i, "r"]])))
        if d < minimum:  # checks if d is smaller than the minimum allowed difference and defines minimum as d
            minimum = d
            name = str(df["name"][i])  # hue name of the most similar color to point's color
    return name


def recog_color(event, x, y, flags, param):
    """ Recognizes the mouseclick on the image, gets the x,y parameter of the clicked part,
    provides the hue name of the clicked part"""
    global xpoint
    global ypoint
    if event == cv2.EVENT_LBUTTONDOWN:  # checks if the mouse click was done
        xpoint, ypoint = x, y
        text = name_of_color(xpoint, ypoint)  # gets the hue name of the (xpoint, ypoint) point and assigns to text
        cv2.rectangle(img, (0, 0), (500, 50), (150, 170, 200), -1)
        cv2.putText(img, f"color:{text}", (7, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                    1)  # shows the name on the image


cv2.namedWindow('my_img')
cv2.setMouseCallback('my_img', recog_color)  # connects the mouse callback to "my_img" windows
while True:  # shows the image on "my_img" windows
    cv2.imshow("my_img", img)
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        cv2.destroyAllWindows()
        break
