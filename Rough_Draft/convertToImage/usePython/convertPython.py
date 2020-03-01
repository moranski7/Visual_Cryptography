#!/usr/bin/python3
# 
# Uses PIL (from Pillow) to convert a text file to an image file.
# To use must install Pillow using pip.
#
# This program takes in one text file as an arguement.
# The text file must contain at least one string consisting of 6 characters.
#
# when completed successfully, it should return a zero.
# If an error occurs, it should print a msg to stderr
#
#
import sys
import os
import logging
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

if __name__ == "__main__":
	logging.basicConfig(stream=sys.stderr, level=logging.INFO)

	#check for command line arguments
	if (len(sys.argv) == 1):
		print ("Usage: ./convertPython.py filename", file=sys.stderr)
		exit(1)
	elif (len(sys.argv) > 2):
		print ("Too many arguments", file=sys.stderr)
		exit(1)

	#Check to make sure file exist
	try:
		f = open (sys.argv[1], "r")
	except IOError:
		print ("File not accessible", file=sys.stderr)
		exit(1)

	#Check to make sure file is not empty.
	if os.stat(sys.argv[1]).st_size == 0:
		print ("File is empty", file=sys.stderr)
		exit (1)

	#Check to make sure line read is not empty.
	pswd = f.readline()
	if pswd.isspace():
		print ("First line of text file can't be empty.")
		exit (1)

	#Set up image objects and create image.
	img = Image.new ('RGB', (380,70), color='white')
	draw = ImageDraw.Draw (img)
	font = ImageFont.truetype("roman_font_7.ttf", 60)
	logging.info ("Line from file is %s", pswd)

	#Add text to file
	logging.info ("Adding Text...")
	draw.text((30,15), pswd, (0,0,0), font=font)
	logging.info ("Finished adding...")

	#Save image.
	logging.info ("Saving image...")
	img.save ('test.bmp')
	logging.info ("Exit...")
	exit (0)
