#!/usr/bin/env python

# color-map.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.0

import os
import cv2
import glob
from shutil import rmtree

def color_map():
  image_dir_path = os.path.join(os.getcwd(), "assets/img")
  out_path = os.path.join(os.getcwd(), "out/color-map")
  ext = "jpg"

  print(f"Reading all images from the directory: {image_dir_path}")
  print(f"Output will be saved in: {out_path}")

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

# execute the main function
if __name__ == "__main__":
  color_map()


