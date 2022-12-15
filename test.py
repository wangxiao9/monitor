# __author:EstherWang
# time:03/03/2021


import os, sys
from PIL import Image

image_size = [512, 256, 144, 140, 128, 120, 108, 100, 88, 72, 48, 32, 28]


def create_icon():
    for size in image_size:
        pri_image = Image.open("线性春.png", 'r')
        pri_image.resize((size, size), Image.ANTIALIAS).save("icom_%d.ico" % (size))


if __name__ == "__main__":
    create_icon()