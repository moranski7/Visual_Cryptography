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


	#Check to make sure the commandline arguments are okay.
	if len(sys.argv) != 8:
		print ("Usage: ./addUser.py userName password firstName LastName DOB age gender", file=sys.stderr)
		sys.exit (1)

	#Create the query and escape values to prevent sql injection
	sql = "INSERT IGNORE INTO voters (UserName, Password, FirstName, LastName, DOB, Age, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
	val = (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

	#execute and commit insert
	cursor. execute (sql, val)
	mydb. commit ()
	print (cursor.rowcount) #Prints result number of successful insert to stdout.

if __name__ == '__main__':
	main ()
	sys.exit (0)
