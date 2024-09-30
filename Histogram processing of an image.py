#!/usr/bin/env python
# coding: utf-8

# In[1]:Write your code to find the histogram of gray scale image and color image channels


import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("gray image of flower.jpg")
color_image = cv2.imread()
cv2.imshow("Gray Image",gray_image)
cv2.imshow("Colour Image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:Display the histogram of gray scale image and any one channel histogram from color image


import matplotlib.pyplot as plt 
grayscale_image=cv2.imread("gray image of flower.jpg")
colourscale_image=cv2.imread("color image of flower.jpg")
hist=cv2.calcHist(grayscale_image,[0],None,[255],[0,255])
hist1=cv2.calcHist([color_image],[1],None,[256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel("")
plt.ylabel("pixel count")
plt.stem()
plt.show()
hist = cv2.calcHist([gray_image],[0],None,[256],[0,256])
hist1 = cv2.calcHist([color_image],[1],None,[256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel('GrayScaleValue')
plt.ylabel('PixelCount')
plt.stem(hist)
plt.show()
plt.figure()
plt.title("Histogram")
plt.xlabel('Intensity Value')
plt.ylabel('PixelCount')
plt.stem(hist1)
plt.show()


# In[3]:Write the code to perform histogram equalization of the image. 



import cv2
import matplotlib.pyplot as plt 
gi=cv2.imread("gray image of flower.jpg",0)
colorscale=cv2.imread("color image of flower.jpg")
g=cv2.resize(gi,(500,400))
equ=cv2.equalizeHist(gi)
cv2.imshow('Gray Image',Gray_image)
cv2.imshow('Equalized Image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()







