import cv2
import random
import numpy as np

img = cv2.imread('assets/image_3.jpg', 1)

#img = cv2.resize(img, (400, 400)) # resize
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate commands look up

tag = img[500:700, 600:900]#getting one part of the whole image
img[100:300, 650:950] = tag

""" convert some pixels into random black or white
for i in range(100):
    for j in range(img.shape[1]):
        pixel = random.randint(0,255)
        img[i][j] = pixel
"""
"""
cap = cv2.VideoCapture(0)#make this a video link in folder
while True:#make it so that a frame has 4 of itself
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    image[:height//2, :width//2] = smaller_frame

    image[:height//2:, :width//2] = smaller_frame

    image[:height//2, :width//2:] = smaller_frame

    image[:height//2:, :width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release

"""
width = 0
height = 500
img_line = cv2.line(img, (0,0), (width, height), [255, 0, 0], 1000)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Text on screen", (200, height -10), font, 4, [0,0,0], 5, cv2.LINE_AA)

#extracting specific colored pixels
rubix = cv2.imread('image_5.jpg', 1)
hsv = cv2.cvtColor(rubix,cv2.COLOR_BGR2HSV)
lower_blue = np.array([110, 50,50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
#this mask image will only show which pixels are in that color range
#its black and white though
result = cv2.bitwise_and(rubix, rubix, mask = mask)
#result makes it so that you get the original pic, just with the 
#requirements being in the mask
"""
cv2.imshow('Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#Corner detection
chess = cv2.imread('assets/chessboard.png', 1) 
chess = cv2.resize(chess, (0, 0), fx = 0.75, fy = 0.75) # resize
chess = cv2.cvtColor(chess, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(chess, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(chess, (x, y), 5, [255, 0, 0], -1)

cv2.imshow('Image',chess)
cv2.waitKey(0)
cv2.destroyAllWindows()