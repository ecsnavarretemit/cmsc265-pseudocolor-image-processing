#!/usr/bin/env python

# run.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.0

import os
import cv2
import glob
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

  # create a dictionary of colormaps
  color_maps = {
    'autumn': cv2.COLORMAP_AUTUMN,
    'bone': cv2.COLORMAP_BONE,
    'jet': cv2.COLORMAP_JET,
    'winter': cv2.COLORMAP_WINTER,
    'rainbow': cv2.COLORMAP_RAINBOW,
    'ocean': cv2.COLORMAP_OCEAN,
    'summer': cv2.COLORMAP_SUMMER,
    'spring': cv2.COLORMAP_SPRING,
    'cool': cv2.COLORMAP_COOL,
    'hsv': cv2.COLORMAP_HSV,
    'pink': cv2.COLORMAP_PINK,
    'hot': cv2.COLORMAP_HOT,
  }

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
    for color_name, color_val in color_maps.items():
      im_color = cv2.applyColorMap(im_gray, color_val)

      cv2.imwrite(f"{final_out_path}/{color_name}.jpg", im_color)

#=====================================================
# [Color Map] ::end
#=====================================================


#=====================================================
# [RGB Color Transformation] ::start
#=====================================================

def rgb_color_transformation():
  pass

#=====================================================
# [RGB Color Transformation] ::end
#=====================================================

# execute the main function
if __name__ == "__main__":
  pass


