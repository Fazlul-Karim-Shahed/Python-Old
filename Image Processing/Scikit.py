from skimage import io
from matplotlib import pyplot as plt
from skimage.transform import resize, rescale, downscale_local_mean
from skimage.filters import sobel, roberts, scharr, prewitt


def show_img(img):
    from matplotlib import pyplot as plt
    import numpy as np
    img = np.asarray(img)
    plt.imshow(img)
    plt.show()


img = io.imread('./cell.jpg', as_gray=False)

# show_img(img)

# print(img.size)
# rescale_image = rescale(img, 10, anti_aliasing=True)
# show_img(rescale_image)
# print(rescale_image.size)

# pr = prewitt(img)
# sb = sobel(img)
rb = roberts(image=img)
# sc = scharr(img)
show_img(rb)

# fig, axes = plt.subplots(nrows=2, ncols=2)
# ax = axes.ravel()
# print(ax)
# ax[0].imshow(pr)
# ax[1].imshow(sb)
# # ax[2].imshow(rb)
# ax[3].imshow(sc)
# plt.show()
