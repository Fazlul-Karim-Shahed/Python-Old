from PIL import Image


def show_from_pil(img):
    from matplotlib import pyplot as plt
    import numpy as np
    img = np.asarray(img)
    plt.imshow(img)
    plt.show()


img = Image.open('./cell.jpg')

# print(img.size)

# resize_img = img.resize((500, 300))

# show_from_pil(img)
# show_from_pil(resize_img)
# crop_img = img.crop((0, 0, 200, 200))
# show_from_pil(crop_img)
###########################################################

# image_1 = Image.open('./cell.jpg')
# image_2 = Image.open('./bacteria1.jpg')
# image_2 = image_2.resize((200, 200))

# # print(image_1.size)
# # print(image_2.size)

# image_1.paste(image_2, (50, 50))
# show_from_pil(image_1)

############################################

# img = Image.open('./cell.jpg')

# show_from_pil(img)

# img = img.rotate(45, expand=True)

# show_from_pil(img)
#####################################################

# img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# show_from_pil(img)