#!/usr/bin/env python3

#https://pyfai.readthedocs.io/en/master/man/pyFAI-average.html
#Author: Marco Vandone

import os
import sys
import glob
import subprocess

SUBDIR = './average/'

img_ext = "*.tiff"
method = 'mean'  #the method for pyFAI-average
ave_amount = 5
out_basename = "ave_"
print([arg for arg in sys.argv[:]])
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("The program read all the images with the user-specified format in the folder and it averages them in n groups, with n based on the number of images to be averaged together. User can also specify the pyfai averaging method (default is mean) and the amount of images to be aeraged (default 5) per each time")
    print("program takes the following arguments in the following formats:")
    print("<.extension of the images to integrate> </> -n <n of images to be averaged together(optional)> </> -m <averaging method (optional)>")
    sys.exit(1)


for i, arg in enumerate(sys.argv[:]):
    if arg == '-n':
        ave_amount = int(sys.argv[i+1])
    if arg == '-m':
        method = str(sys.argv[i+1])
        
img_ext = "*" + str(sys.argv[1])
out_ext = img_ext

read_img = glob.glob(img_ext)

if len(read_img) > 0:
    print(f"found {len(read_img)} images")

    try:
        os.mkdir(SUBDIR)
        print("subfolder created")
    except FileExistsError: print("subfolder already present")
    
    print("running pyFAI on found images ...")
    for i in range(0,int(len(read_img)/ave_amount)):
        print("averaging ...")
        file_string = ' '.join(read_img[i*ave_amount:i*ave_amount+ave_amount])   #compose the FILENAME argument for pyFAI-average
        # print(file_string)
        os.system("pyFAI-average " + file_string + '-d' + dark_string + ' -m ' + method + ' -o ' + out_basename+ str(ave_amount * i) + '-' + str(ave_amount * i+(ave_amount )) +out_ext)
        if i == int(len(read_img)/ave_amount) and len(read_img)%ave_amount != 0:
            file_string = ' '.join(read_img[:-len(read_img)%ave_amount])   #compose the FILENAME argument for pyFAI-average
            os.system("pyFAI-average " + file_string + ' -m ' + method + ' -o ' + out_basename+str(i)+out_ext)
            
else:
    print("0 imgs found")
