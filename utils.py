import cv2
import math
import os
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def get_gaussian_background(height, width):
    """Create a background with Gaussian noise"""
    image = np.ones((height, width)).astype('uint8')*255
    cv2.randn(image, 240, 15)
    return Image.fromarray(image).convert("RGB")

def get_white_background(height, width):
    """Create a plain white background"""
    return Image.new("L", (width, height), 255).convert("RGB")

def get_color_background(height, width, color):
    """Create a background with the given color"""
    return Image.new("RGB", (width, height), color)

def get_bgr_image(height, width, bgr_dir):
    """Create a background with a image"""
    bgr_list = os.listdir(bgr_dir)
    bgrfile = rnd.choice(bgr_list)
    bgr = Image.open(os.path.join(bgr_dir, bgrfile))

    if bgr.size[0] < width:
        bgr = bgr.resize([width, int(bgr.size[1] * (width / bgr.size[0]))], Image.ANTIALIAS)
    if bgr.size[1] < height:
        bgr = bgr.resize([int(bgr.size[0] * (height / bgr.size[1])), height], Image.ANTIALIAS)

    x=0 if bgr.size[0] == width else rnd.randint(0, bgr.size[0] - width)
    y=0 if bgr.size[1] == height else rnd.randint(0, bgr.size[1] - height)
    return bgr.crop((x, y, x + width, y + height))

def rotate(image, skewby_angle):
    """Add skewness to the image"""
    random_angle = rnd.randint(0 - skewby_angle, skewby_angle)
    return image.rotate(random_angle)

def shear(image, shearby_pixels):
    """Shear the image"""
    (H,W,C) = image.shape
    pts1 = np.float32([[10,5],[20,5],[10,20]])
    pts2 = np.float32([[10+shearby_pixels,5],[20+shearby_pixels,5],[10,20]])
    M = cv2.getAffineTransform(pts1,pts2)
    return Image.fromarray(cv2.warpAffine(image, M, (W, H)))

def mirror_leftright(image):
    """flip left-right"""
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def mirror_upside(image):
    """flip top-bottom"""
    return image.traspose(Image.FLIP_TOP_BOTTOM)

def orientation_vertical(image):
    """Rotate image by 90 degrees"""
    return image.transpose(Image.ROTATE_90)

def blur(image, blur_parameter):
    """Blur the image"""
    random_blur = rnd.randint(0, blur_parameter)
    blur_filter = ImageFilter.GaussianBlur(radius=random_blur)
    return image.filter(blur_filter)

if __name__=="__main__":
    #img = gaussian_noise(32,32)
    currency_dict = {
        "yen" : "\u00a5",
        "rupee" : "\u20b9",
        "baht" : "\u0e3f",
        "dollar" : "\u0024",
        "euro" : "\u20ac",
        "pound" : "\u00a3",
        "bitcoin" : "\u20bf"
    }

    img = get_color_background(32, 32, (0,255,0))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/Lato-Black.ttf", 30)
    draw.text((6, -3),currency_dict["yen"],(255,0,0),font=font)

    #img = shear(np.asarray(img).astype(np.uint8), 2)
    img = blur(img, 1)

    plt.imshow(img)
    plt.show()