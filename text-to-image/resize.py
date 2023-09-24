import sys

import cv2
from PIL import Image

if len(sys.argv) <= 1:
    raise Exception("You need to pass the image name!")

image_name = sys.argv[1]
img = cv2.imread(f'images/{image_name}', cv2.IMREAD_UNCHANGED)

width = 1920
height = 1080
dim = (width, height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)

Image.fromarray(resized).save(f"images/{image_name}_resized.png")
