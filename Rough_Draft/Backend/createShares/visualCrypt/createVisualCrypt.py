#!/usr/bin/python3
# Reference:
#
# 	https://www.codeproject.com/Questions/2336086/Python-code-for-visual-cryptography
#

import sys
import random
from PIL import Image

def addPixelPattern (outfile, x,y, pattern):
	"""
		Adds a pixels to the image in the following fashion:
		11 00		00 11
		11 00		00 11
		00 11		11 00
		00 11 or 	11 00
		where 0 = black pixel and 1 = white pixel

		Param:
		outfile 		- image file being written to
		x,y				- ror,col of file
		pattern 		- Chossen style of pattern. 0 for the one on the left, 1 for the right.
	"""
	if (pattern == 0):
		outfile.putpixel ((x, y), 255) #place white
		outfile.putpixel ((x+1, y), 255)
		outfile.putpixel ((x, y+1), 255)
		outfile.putpixel ((x+1, y+1), 255)

		outfile.putpixel ((x+2, y), 0) #place black
		outfile.putpixel ((x+3, y), 0)
		outfile.putpixel ((x+2, y+1), 0)
		outfile.putpixel ((x+3, y+1), 0)

		outfile.putpixel ((x, y+2), 0) #place black
		outfile.putpixel ((x+1, y+2), 0)
		outfile.putpixel ((x, y+3), 0)
		outfile.putpixel ((x+1, y+3), 0)

		outfile.putpixel ((x+2, y+2), 255) #place white
		outfile.putpixel ((x+3, y+2), 255)
		outfile.putpixel ((x+2, y+3), 255)
		outfile.putpixel ((x+3, y+3), 255)
	
	elif (pattern == 1):
		outfile.putpixel ((x, y), 0) #place black
		outfile.putpixel ((x+1, y), 0)
		outfile.putpixel ((x, y+1), 0)
		outfile.putpixel ((x+1, y+1), 0)

		outfile.putpixel ((x+2, y), 255) #place white
		outfile.putpixel ((x+3, y), 255)
		outfile.putpixel ((x+2, y+1), 255)
		outfile.putpixel ((x+3, y+1), 255)

		outfile.putpixel ((x, y+2), 255) #place white
		outfile.putpixel ((x+1, y+2), 255)
		outfile.putpixel ((x, y+3), 255)
		outfile.putpixel ((x+1, y+3), 255)

		outfile.putpixel ((x+2, y+2), 0) #place black
		outfile.putpixel ((x+3, y+2), 0)
		outfile.putpixel ((x+2, y+3), 0)
		outfile.putpixel ((x+3, y+3), 0)

def addMatchPair (outFile, x, y):
	"""Adds a black and white pixals to the image in the following fashion choosen at random:

		00 11		11 00
		00 11		11 00
		11 00		00 11
		11 00 	or  00 11
		where 0 = black pixel and 1 = whie pixel

	Param:
		outFile 	- Image file being written to
		x,y			- row, col location in file
	"""
	choosePixelPair = random.random ()

	if (choosePixelPair < 0.5):
		addPixelPattern (outFile, x,y, 0)
	else:
		addPixelPattern (outFile, x,y, 1)

def addComplementaryPair (outfile1, outfile2, x,y):
	"""
		Adds black and white pixels to the file.
		Files are given complementary pair of pixels.

		Param:
			outfile1, outfile2 		- images files that are being written to
			x,y	 					- row, col of the file.
	"""
	choosePixelPair = random.random ()

	if (choosePixelPair < 0.5):
		addPixelPattern (outfile1, x,y, 0)
		addPixelPattern (outfile2, x,y, 1)
	else:
		addPixelPattern (outfile1, x, y, 1)
		addPixelPattern (outfile2, x, y, 0)

############################End of Functions###########################################

#check Command line arguments
if (len(sys.argv) == 1):
	print ("Usage: ./createVisualCrypt.py imageFile")
	exit (1)
elif (len(sys.argv) > 2):
	print ("Too many arguements.")
	exit (1)

if (not (sys.argv[1].lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')))):
	print ("Command line argument must be a png, jpg, jpeg, or bmp file.")
	exit (1)

try:
	image = Image.open (sys.argv[1])
	image = image.convert ('1')	#convert file to black and white pixels.
except IOError:
		print ("File not accessible")
		exit(1)

#Create new image files
newSize = (image.size[0]*4, image.size[1]*4)
outfile1 = Image.new ("1", newSize)
outfile2 = Image.new ("1", newSize)

for x in range (0,image.size[0]):
	for y in range (0, image.size[1]):
		srcPxl = image.getpixel ((x,y))
		assert srcPxl in (0, 255) #Make sure it is in black and white.

		#if black pixel
		if (srcPxl == 0):
			addComplementaryPair (outfile1, outfile2, x*4,y*4)
		#If white pixel 
		elif (srcPxl == 255):
			addMatchPair (outfile1, x*4, y*4)
			addMatchPair (outfile2, x*4, y*4)

outfile1 =  outfile1.convert("RGBA")
outfile2 = outfile2.convert("RGBA")
outfile1.save('out1.png')
outfile2.save('out2.png')

#Test to make sure file cam be decrypted.
new_img = Image.blend(outfile1, outfile2, 0.4)
new_img.save("decryptedPswd.png","PNG")

exit (0)
