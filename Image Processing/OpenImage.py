from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image
from skimage import io, img_as_float, img_as_ubyte
import cv2

def showImg(nparray): 
    plt.imshow(nparray)
    plt.show()

##################################################################
# img = Image.open('./cell.jpg')
# print(type(img))

# img = np.asarray(img)
# print(type(img))

# plt.imshow(img)
# print(img.shape)
# plt.colorbar()
# plt.show()

#############################################################
# img = image.imread('./cell.jpg')
# plt.imshow(img)
# plt.colorbar()
# plt.show()

##############################################################


# img = io.imread('./cell.jpg')
# print(img)
# imgAsFloat = img_as_float(img)
# plt.imshow(imgAsFloat)
# plt.show()                                   # astype remains the value...just keep a point agter the value same but "img_as_float" make it between 0 and 1 (value/255)                       
# print(imgAsFloat)
# print(img.astype(np.float32))

###############################################################

img = cv2.imread('./cell.jpg', 1)
cv2.imshow('gray', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()