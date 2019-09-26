from IPython.display import display, Image
import numpy as np
import cv2

path1 = './logo.png'
path2 = './logo.png'

for path in path1, path2:
    img = Image(path)
    display(img)
    print(img.data)
    im_pillow = np.array(img.data)
    cv2.imshow('a', im_pillow)
    cv2.waitKey(0)

