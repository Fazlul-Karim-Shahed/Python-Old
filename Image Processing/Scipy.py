from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np

def show_img(img):
    from matplotlib import pyplot as plt
    import numpy as np
    img = np.asarray(img)
    plt.imshow(img)
    plt.show()

img = img_as_ubyte(io.imread('./cell.jpg', as_gray=False))


# show_img(img)
# print(img.mean(), img.max(), img.min())

#################################################

# flippedLR = np.flipud(img)
# show_img(flippedLR)

###################################################

# uniform_filter = ndimage.uniform_filter(img, size=2)
# show_img(uniform_filter)
# gaussian_filter = ndimage.gaussian_filter(img, 4)
# show_img(gaussian_filter)



