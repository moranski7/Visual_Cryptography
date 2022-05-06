#!/usr/bin/env python3
import mysql.connector
from pathlib import Path
import sys

def main ():
	mydb = mysql.connector.connect (
		host="localhost",
		user="Michael Oranski",
		password="Password@2",
		database='VoteDatabase',
		auth_plugin='mysql_native_password'
	)
	cursor = mydb.cursor()

	#check to make sure the command line arguements are okay
	if len(sys.argv) != 4:
		print ("Usage: ./storeImag.py userName electionName fileName", file=sys.stderr)
		exit (1)

	#create the query to get User Id
	sql = "SELECT VoterID FROM voters WHERE UserName = %s"
	val = (sys.argv[1], ) #comma needed to parse parameter.
	cursor. execute (sql, val)

	result = cursor. fetchall ()
	voterID = result[0][0]

	#create the query to get Election ID, start Date and end Date
	sql = "SELECT StartDate, EndDate, ElectID FROM elections WHERE Name = %s"
	val = (sys. argv[2], )
	cursor. execute (sql, val)

	result = cursor. fetchall ()
	startDate = result[0][0]
	endDate = result[0][1]
	electID = result[0][2]

	#get path of image.
	whereImgStored = str(Path().absolute()) + "/" + sys.argv[3]

	#Insert image location into table
	sql = "INSERT IGNORE INTO voterShares (ImgLoc, ImgName, ElectStart, ElectEnd, Elect_ID, Voter_ID) VALUES (%s, %s, %s, %s, %s, %s)"
	val = (whereImgStored, sys.argv[3], startDate, endDate, electID, voterID)

	#execute and commit insert
	cursor. execute (sql, val)
	mydb. commit ()
	print (cursor.rowcount) #Prints result number of successful insert to stdout.

if __name__ == '__main__':
	main ()
	sys.exit (0)
