#!/usr/bin/python3
#Red: https://stackoverflow.com/questions/13070038/attachment-image-to-send-by-mail-using-python  (author: user1292828)
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def main():
	print ("Entering main function...")
	# set up the SMTP server
	smtp = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
	smtp.ehlo()
	smtp.login("xxxx@xxxx.com", "password") #censoring email and password for privacy
	
	print ("Generating email header...")
	imgData = open("out2.png", 'rb').read()
	msg = MIMEMultipart()
	msg['Subject'] = 'Program Test'
	msg['From'] = 'xxxx@xxx.com'
	msg['To'] = 'xxx@xxxx.com'
	
	print ("Generating body and attachment")
	text = MIMEText("test")
	msg.attach(text)
	image = MIMEImage(imgData, name=os.path.basename("out2.png"))
	msg.attach(image)

	smtp.sendmail("xxxx@xxxx.com", "xxx@xxx.com", msg.as_string()) #censoring email and password for privacy
	smtp.quit()
	print ("Exiting main function...")

if __name__ == '__main__':
	print("Start of program...")
	main()
	exit (0)
