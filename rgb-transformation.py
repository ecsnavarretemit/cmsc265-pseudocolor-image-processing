#!/usr/bin/env python

# rgb-transformation.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.0

import os
import cv2
import sys
import glob
import numpy as np
from math import pi
from shutil import rmtree

class FalseRGB(object):

  def __init__(self, image):
    self.a = 255
    self.b = 2 * pi / 255
    self.c = pi / 5
    self.image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

  def r_transform(self):
    im = self.image.copy()

    # R = a | sin(bx) |
    return self.a * np.absolute(np.sin(self.b * im))

  def g_transform(self):
    im = self.image.copy()

    # G = a | sin(bx + c) |
    return self.a * np.absolute(np.sin((self.b * im) + self.c))

  def b_transform(self):
    im = self.image.copy()

    # B = a | sin(bx + 2c) |
    return self.a * np.absolute(np.sin((self.b * im) + (2 * self.c)))

  def get_rgb_image(self):
    # perform color channel transformation, merge it and return the result
    return cv2.merge([
      self.b_transform(),
      self.g_transform(),
      self.r_transform()
    ])

def rgb_color_transformation():
  image_dir_path = os.path.join(os.getcwd(), "assets/img")
  out_path = os.path.join(os.getcwd(), "out/rgb-color-transformation")
  ext = "jpg"

  # find all images in the directory
  images = glob.glob(f"{image_dir_path}/*.{ext}")

  # exit immediately when there are no images present on the folder
  num_images = len(images)
  if num_images == 0:
    print(f"No images present on the directory: {image_dir_path}")
    sys.exit(1)

  print(f"Reading all images from the directory: {image_dir_path}")
  print(f"Output will be saved in: {out_path}")

  # delete the folder to make sure we are create new files
  if os.path.exists(out_path):
    rmtree(out_path)

  # create the output folder if not exists
  if not os.path.exists(out_path):
    os.makedirs(out_path)

  # iterate all found images and colorize them
  for image in images:
    basename = os.path.basename(image)
    filename, _ = os.path.splitext(basename)

    false_rgb = FalseRGB(image)

    cv2.imwrite(f"{out_path}/{filename}.jpg", false_rgb.get_rgb_image())

# execute the main function
if __name__ == "__main__":
  rgb_color_transformation()


