#!/usr/bin/env python3
#Reference:
# https://stackoverflow.com/questions/37201250/sending-email-via-gmail-python
# Author: apadana
# Date: May 17, 2016
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import oauth2client
from oauth2client import client, tools, file
from apiclient import errors, discovery
import httplib2
import base64
import sys
import os

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'

def get_credentials():
    home_dir = os.path.expanduser('~') #>> C:\Users\Me
    credential_dir = os.path.join(home_dir, '.credentials')  # >>C:\Users\Me\.credentials   (it's a folder)
    
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir) #create folder if doesnt exist
    credential_path = os.path.join(credential_dir, 'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path) #Store the credential
    credentials = store.get()
    
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)  # Create a flow object. (it assists with OAuth 2.0 steps to get user authorization + credentials)
        flow.user_agent = APPLICATION_NAME

        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    
    return credentials

def createMessageWithAttachment(sender, to, subject, msgHtml, msgPlain, attachmentFile):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      msgHtml: Html message to be sent
      msgPlain: Alternative plain text message for older email clients          
      attachmentFile: The path to the file to be attached.

    Returns:
      An object containing a base64url encoded email object.
    """

    #create the message container using a dictionary { to, from, subject }
    message = MIMEMultipart('mixed')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject


    messageA = MIMEMultipart('alternative')
    messageR = MIMEMultipart('related')

    #Add text to email body.
    messageR.attach(MIMEText(msgHtml, 'html'))
    messageA.attach(MIMEText(msgPlain, 'plain'))
    messageA.attach(messageR)

    message.attach(messageA)

    # Try to guess what kind of file is being attached.
    content_type, encoding = mimetypes.guess_type(attachmentFile)
    main_type, sub_type = content_type.split('/', 1)
 
    #how the file should be read and stored. Should Only be dealing with image.
    if main_type == 'image':
        fp = open(attachmentFile, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    else: #If it reaches here, then there is something wrong with file checking part.
        print ("ERROR: FILE NOT AN IMAGE!")
        exit (1)

    #Encode the attachment, add a header and attach it to the message
    filename = os.path.basename(attachmentFile)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    #encode the message (the message should be in bytes)
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def SendMessageInternal(service, user_id, message):
    """Sends the email while checking for any error"""
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return "Error"
    return "OK"

def SendMessage(sender, to, subject, msgHtml, msgPlain, attachFile):
	"""Get the credentials, create the email and send it. """
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http()) # Create an httplib2.Http object to handle our HTTP requests, and authorize it using credentials.authorize()
	service = discovery.build('gmail', 'v1', http=http)
	message1 = createMessageWithAttachment(sender, to, subject, msgHtml, msgPlain, attachFile)
	result = SendMessageInternal(service, "me", message1) #Sends email and checks for errors

	return result

def main ():
	if (len(sys.argv) < 3):
		print ("Not enough arguments!")
		print ("Usage: ./sendImage.py imageFile target_email")
		exit (1)

	elif (len (sys.argv) > 3):
		print ("Too many arguments!")
		print ("Usage: ./sendImage.py imageFile target_email")
		exit (1)

	#Make sure first argument is a picture file.
	if (not (sys.argv[1].lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')))):
		print ("First command line argument must be a png, jpg, jpeg, or bmp file.")
		exit (1)

	#Email contents
	to = sys.argv[2]
	sender = "Michael.Oranski@gmail.com"
	subject = "Sending Share Test"
	msgHtml = "Hi<br/>Here is the share for the pswd."
	msgPlain = "Hi\nHere is the share for the pswd."
	attachFile = sys.argv[1]

	SendMessage(sender, to, subject, msgHtml, msgPlain, attachFile)


if __name__ == '__main__':
    main()
    exit (0)
