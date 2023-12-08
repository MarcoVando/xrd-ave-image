#!/usr/bin/env python3

#https://pyfai.readthedocs.io/en/master/man/pyFAI-average.html
#Author: Marco Vandone

import os
import sys
import glob
import subprocess

IMG_EXT = "*.tiff"
SUBDIR = './average/'

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("The program read all the images with the user-specified format in the folder and it averages them. User can also specify the pyfai averaging method (default is mean)")
    print("program takes the following arguments in the following formats:")
    print("<.extension of the images to integrate> </> <averaging method>")
    sys.exit(1)
    
read_img = glob.glob(IMG_EXT)

print(f"found {len(read_img)} images")
for x in read_img:
   print(x)

file_string = ' '.join(read_img)   #compose the FILENAME argument for pyFAI-average

method = 'mean'  #the method for pyFAI-average

try:
   os.mkdir(SUBDIR)
   print("subfolder created")
except FileExistsError: print("subfolder already present")

print("running pyFAI on found images ...")
os.system("pyFAI-average " + file_string + ' -m ' + method)
