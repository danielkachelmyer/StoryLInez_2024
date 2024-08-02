import cv2
import numpy as np
from matplotlib import pyplot as plt
back = 'assets/Rubix.jpg'
def resize(image, width, height, display):
    resized_image = cv2.resize(image, (width, height))
    if display:
        cv2.imshow('Result Image', resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return resized_image

image_bgr = cv2.imread(back)
image_bgr = resize(image_bgr, 1000, 1000, False)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
#(x, y , width, height)
rectangle = (300, 300, 700, 780)
# 600, 550, 1150, 2000
mask = np.zeros(image_rgb.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cv2.grabCut(image_rgb, mask, rectangle, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask_2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

image_rgd_nobg = image_rgb * mask_2[:, :, np.newaxis]

plt.imshow(image_rgd_nobg), plt.axis('off')
plt.show()

