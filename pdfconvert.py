
import sys
import glob
import os
from PIL import Image


def makePdf():
        imageDir="E:/Custom Documents/TahR/"
        SaveToDir="E:/Custom Documents/TahR/PDF/"
        os.chdir(imageDir)
        try:
            for j in os.listdir(os.getcwd()):
                os.chdir(imageDir)
                fname, fext = os.path.splitext(j)
                newfilename = fname + ".pdf"
                im = Image.open(fname + fext)
                if im.mode == "RGBA":
                    im = im.convert("RGB")
                os.chdir(SaveToDir)
                if not os.path.exists(newfilename):
                    im.save(newfilename, "PDF", resolution=100.0)
        except Exception as e:
            print(e)


makePdf()