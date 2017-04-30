#!/usr/bin/env python

# run.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.0

import os
import cv2
import glob
import numpy as np
from math import pi
from shutil import rmtree

#=====================================================
# [Color Map] ::start
#=====================================================

def color_map():
  image_dir_path = os.path.join(os.getcwd(), "assets/img")
  out_path = os.path.join(os.getcwd(), "out/color-map")
  ext = "jpg"

  # find all images in the directory
  images = glob.glob(f"{image_dir_path}/*.{ext}")

  # get all colormap flags available in opencv
  colormap_flag_prefix = 'COLORMAP_'
  colormap_flags = [i for i in dir(cv2) if i.startswith(colormap_flag_prefix)]

  # assemble the dictionary of color maps
  colormaps = {}
  for colormap_flag in colormap_flags:
    colormap_key = colormap_flag[len(colormap_flag_prefix):].lower()

    colormaps[colormap_key] = getattr(cv2, colormap_flag)

  # delete the folder to make sure we are create new files
  if os.path.exists(out_path):
    rmtree(out_path)

  # create the output folder if not exists
  if not os.path.exists(out_path):
    os.makedirs(out_path)

  # iterate all found images
  for image in images:
    basename = os.path.basename(image)
    filename, _ = os.path.splitext(basename)
    im_gray = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # resolve the output folder for each image
    final_out_path = os.path.join(out_path, filename)
    if not os.path.exists(final_out_path):
      os.makedirs(final_out_path)

    # apply the colormap to the grayscaled image and write it to the filesystem
    for color_name, color_val in colormaps.items():
      im_color = cv2.applyColorMap(im_gray, color_val)

      cv2.imwrite(f"{final_out_path}/{color_name}.jpg", im_color)

#=====================================================
# [Color Map] ::end
#=====================================================


#=====================================================
# [RGB Color Transformation] ::start
#=====================================================

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

    # R = a | sin(bx + c) |
    return self.a * np.absolute(np.sin((self.b * im) + self.c))

  def b_transform(self):
    im = self.image.copy()

    # R = a | sin(bx + 2c) |
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

  # delete the folder to make sure we are create new files
  if os.path.exists(out_path):
    rmtree(out_path)

  # create the output folder if not exists
  if not os.path.exists(out_path):
    os.makedirs(out_path)

  image = images[0]

  # iterate all found images
  for image in images:
    basename = os.path.basename(image)
    filename, _ = os.path.splitext(basename)

    false_rgb = FalseRGB(image)

    cv2.imwrite(f"{out_path}/{filename}.jpg", false_rgb.get_rgb_image())

#=====================================================
# [RGB Color Transformation] ::end
#=====================================================

# execute the main function
if __name__ == "__main__":
  pass


