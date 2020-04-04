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

	#Check to make sure the command line arguments are correct
	if len (sys.argv) != 3:
		print ("Usage: ./login.py userName password", file=sys.stderr)
		sys.exit (1)

	#Create a query to see if the two values exist in the table.
	sql = "SELECT * FROM voters WHERE UserName = %s AND Password = %s"
	val = (sys.argv[1], sys.argv[2],) #comma needed to parse parameter.
	cursor. execute (sql, val)
	result = cursor. fetchall ()

	#print the result.
	if len(result) == 1:
		print (0)
	else
		print (-1)

if __name__ == '__main__':
	main ()
	sys.exit (0)
