#!/usr/bin/env python3
import mysql.connector
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

	#check to make sure the commandline arguments are okay
	if len(sys.argv) != 3:
		print ("Usage: ./getUserInfo.py userName electionName", file=sys.stderr)
		exit (1)

	#create the query and escape the value to prevent sql injection
	sql = "SELECT VoterID FROM voters WHERE UserName = %s"
	val = (sys.argv[1], )		#comma is needed to parse the parameter. No comma results in "ValueError: Could not process parameters" error.
	cursor.execute (sql, val)

	result = cursor. fetchall ()
	firstHalf = result[0][0]
	
	#create the query and escape the value to prevent sql injection
	sql = "SELECT ElectID FROM elections WHERE Name = %s"
	val = (sys.argv[2], )		#comma is needed to parse the parameter. No comma results in "ValueError: Could not process parameters" error.
	cursor.execute (sql, val)

	result = cursor. fetchall ()
	secondHalf = result[0][0]
	fileName = str(firstHalf) + str(secondHalf) + ".txt"
	file = open (fileName, "w")
	file.close()

if __name__ == '__main__':
	main ()
	sys.exit (0)
