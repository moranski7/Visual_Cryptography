#!/bin/sh

# A bash test file using ImageMagick to convert a text to an image file.
# To use must install using command: sudo apt install imagemagick-6.q16
# 
# This program takes in one text file as an arguement.
# The text file must contain at least one string consisting of 6 characters.
# 
# When completed succcessfully, it should return a zero.
# If an error occurs, it should return a nonnegative integer.
#

# user calls program without parameter
if [ $# -eq 0 ]
	then
		echo "Usage: convertBash.sh [FILE]"
		echo "Convert string from file to image."
		exit 1
fi

#Check to see if file exist
if [ ! -f $1 ]; then
	echo "File not found!"
	exit 1
fi

#Check to see if file is empty
if [ ! -s $1 ]; then
	echo "File is empty!"
	exit 1
fi

#read single line from file.
read -r line < "$1"

#converts the text to image.
convert -size 380x70 xc:white -pointsize 50\
		-fill black -stroke black -draw "text 10,55 '$line'" \
		test.bmp

exit 0
