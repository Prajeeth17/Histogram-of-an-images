# Histogram of an image
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:

### Step1:
Read the gray and color image using imread()
### Step2:
Print the image using imshow().
### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.

## Program:
```python
# Developed By: Prajeeth K T
# Register Number: 212222110034

import cv2
import matplotlib.pyplot as plt

# Histogram for Gray scale and Color image
 
gray_image = cv2.imread('grayscale.jpeg')
color_image = cv2.imread('color.jpeg')
plt.imshow(gray_image)
plt.show()
plt.imshow(color_image)
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



# Equalized Image
import cv2
Gray_image=cv2.imread('gray.jpeg',0)
equ = cv2.equalizeHist(Gray_image)
cv2.imshow('Gray Image',Gray_image)
cv2.imshow('Equalized Image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
## Output:

### Input Grayscale Image and Color Image
Grayscale Image

![resized_image](https://github.com/user-attachments/assets/22d141e9-f8ac-40fe-b414-ff3f20196de7)


Color Image

![resized_image2](https://github.com/user-attachments/assets/02d375be-edd9-4ed0-b0dc-4dcc9ec385d2)



### Histogram of Grayscale Image and any channel of Color Image
Grayscale Image

![image](https://github.com/user-attachments/assets/31172b18-3d81-42e0-847e-f5c2a218d1b4)

![image](https://github.com/user-attachments/assets/cd0658d3-0b9e-4997-8e60-3a07955e5373)

Color Image

![image](https://github.com/user-attachments/assets/c1343d6d-31a4-4103-8792-c902c5bdea7c)

![image](https://github.com/user-attachments/assets/ccb7a3c1-89fa-4f72-96de-a11254fbe620)

### Histogram Equalization of Grayscale Image.
![image](https://github.com/user-attachments/assets/4862be51-28b4-4cfd-9fc4-91949337f0ca)

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
