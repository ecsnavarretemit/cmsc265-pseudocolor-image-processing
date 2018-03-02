#!/usr/bin/env python

# rgb-transformation.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.1

import os
import cv2
import sys
import glob
import numpy as np
from shutil import rmtree

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

  a = 255
  b = (2 * np.pi) / 255
  c= np.pi / 5

  # create empty numpy array needed by the lookup tables
  reds = np.array([])
  greens = np.array([])
  blues = np.array([])

  # pre-compute and assign computed values in the lookup table for each channel
  for i in np.arange(0, 256):
    bx = b * i

    # perform transformation on the r channel: R = a | sin(bx) |
    red = a * np.absolute(np.sin(bx))

    # perform transformation on the g channel: G = a | sin(bx + c) |
    green = a * np.absolute(np.sin(bx + c))

    # perform transformation on the b channel: B = a | sin(bx + 2c) |
    blue = a * np.absolute(np.sin(bx + (2 * c)))

    # append to the numpy array
    reds = np.append(reds, [red])
    greens = np.append(greens, [green])
    blues = np.append(blues, [blue])

  # iterate all found images and colorize them then write to the filesystem
  for image in images:
    basename = os.path.basename(image)
    filename, _ = os.path.splitext(basename)

    # read image in grayscale
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # apply lookup table each matrix: red, green and blue
    r_channel = cv2.LUT(image.copy(), reds)
    g_channel = cv2.LUT(image.copy(), greens)
    b_channel = cv2.LUT(image.copy(), blues)

    # merge the channels
    colored = cv2.merge([
      b_channel,
      g_channel,
      r_channel
    ])

    # write to the filesystem
    cv2.imwrite(f"{out_path}/{filename}.jpg", colored)

  print("Done processing images.")

# execute the main function
if __name__ == "__main__":
  rgb_color_transformation()


