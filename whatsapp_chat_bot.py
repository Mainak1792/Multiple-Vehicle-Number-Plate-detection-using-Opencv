# import pywhatkit
# pywhatkit.sendwhatmsg('+8910255787','ola', 16,35)

import numpy as np
import cv2
# import imutils
import os

import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
try:
   for root, dirs, files in os.walk("D:\projects\computer_vision\images", topdown=False):
      for name in files:
         x = os.path.join(root, name)
         img = cv2.imread(x)
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         # plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
         # plt.show()
         bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
         edged = cv2.Canny(bfilter, 30, 200)  # Edge detection
         # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
         # plt.show()
         keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find_contours
         contours = imutils.grab_contours(keypoints)
         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

         location = 0
         for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
               location = approx
               break

         if type(location) == int:
            pass
         else:
            print(type(location))
            mask = np.zeros(gray.shape, np.uint8)
            print(mask)

            new_image = cv2.drawContours(mask, [location], 0, 255, -1)
            print(new_image)
            new_image = cv2.bitwise_and(img, img, mask=mask)

            (x, y) = np.where(mask == 255)
            (x1, y1) = (np.min(x), np.min(y))
            (x2, y2) = (np.max(x), np.max(y))
            cropped_image = gray[x1:x2 + 1, y1:y2 + 1]

            text = []
            reader = easyocr.Reader(['en'])
            print(reader.readtext(cropped_image))

except:
   pass

#for name in dirs:
#print(os.path.join(root, name))
