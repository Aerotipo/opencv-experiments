""" 
Create a checkerboard of 200px x 200px consisting of four equal squares (100 x 100) with the following arrangement of colours in unit8 format:
  upper-left: blue    (255,0,0) #bgr
  upper-right: red    (0,0,255) #bgr
  lower-left: green   (0,255,0) #bgr
  lower-right: yellow (0,255,255) #bgr
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

w = 200 #width in pixels
h = 200 #height in pixels
img_array = np.ones([w, h, 3])

#blue
img_array[:int(h/2),:int(w/2),0] = 255
img_array[:int(h/2),:int(w/2),1] = 0
img_array[:int(h/2),:int(w/2),2] = 0
#red
img_array[:int(h/2),int(w/2):w,0] = 0
img_array[:int(h/2),int(w/2):w,1] = 0
img_array[:int(h/2),int(w/2):w,2] = 255

#green
img_array[int(h/2):h,:int(w/2),0] = 0
img_array[int(h/2):h,:int(w/2),1] = 255
img_array[int(h/2):h,:int(w/2),2] = 0

#yellow
img_array[int(h/2):h,int(w/2):w,0] = 0
img_array[int(h/2):h,int(w/2):w,1] = 255
img_array[int(h/2):h,int(w/2):w,2] = 255

#ploting with cv2 imshow
cv2.imshow("Checkecboard pattern",img_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plotting with matplotlib
plt.figure(figsize=[10,10])
plt.imshow(img_array[:,:,::-1])
plt.show()

cv2.imwrite("image_checkerboard_4.jpg", img_array)

#check output
img = cv2.imread('image_checkerboard_4.jpg')
h, w = img.shape[:2]
print(h, w)
output = img[int(h/2):h, int(w/2):w]
cv2.imwrite('cropped.jpg', output)
cv2.imshow('Cropped Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()