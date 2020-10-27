#coding=utf-8
#图片修复

import cv2
import numpy as np

path = "./target.jpg"

img = cv2.imread(path)
hight, width, depth = img.shape[0:3]

#图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
#thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
#thresh = cv2.inRange(img, np.array([175, 175, 175]), np.array([255, 255, 255]))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,180,255,cv2.THRESH_BINARY)
#创建形状和尺寸的结构元素
kernel = np.ones((3, 3), np.uint8)

#扩张待修复区域
hi_mask = cv2.dilate(thresh, kernel, iterations=1)
specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)


size = 3
cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(width / size), int(hight / size))
cv2.imshow("Image", img)

cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(width / size), int(hight / size))
cv2.imshow("newImage", specular)

cv2.namedWindow("二值化图片",0)
cv2.resizeWindow("二值化图片", int(width / size), int(hight / size))
cv2.imshow("二值化图片",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()