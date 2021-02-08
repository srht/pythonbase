#!/usr/bin/env python
# Batch thumbnail generation script using PIL

import sys
import glob
import os
from PIL import Image

scale_size = (1500)
imgArr=glob.glob("C:/Users/serhat/Downloads/BIBLIYOMETRI18-20181031T105101Z-001/BIBLIYOMETRI18/*.jpg")


# Loop through all provided arguments
for imgPath in imgArr:
    try:
        # Attempt to open an image file
        filepath = imgPath #sys.argv[i]
        image = Image.open(imgPath)
    except IOError as e:
        # Report error, and then skip to the next argument
        print ("Problem opening", filepath, ":", e)
        continue

    # Resize the image
    y = image.size
    ratio = (float(y[0]) / float(y[1]))
    image = image.resize((scale_size, int((scale_size / ratio)) ))


    # Split our original filename into name and extension
    (name, extension) = os.path.splitext(filepath)

    # Save the thumbnail as "(original_name)_small.(extension)"
    image.save(name + '_small.jpg')