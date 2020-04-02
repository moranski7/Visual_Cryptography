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

	#check to make sure the commandline arguments are okay.
	if (len (sys.argv) < 4) or (len(sys.argv) > 5):
		print ("Usage: ./AddElections.py Name StartDate EndDate (Optional)Description", file=sys.stderr)
		exit (1)

	#create the query and escape values to prevent sql injection
	sql = "INSERT IGNORE INTO elections (Name, StartDate, EndDate, Description) VALUE (%s, %s, %s, %s)"
	if (len(sys.argv) == 3):
		val = (sys.argv[1], sys.argv[2], sys.argv[3], NULL)
	else:
		val = (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

	#execute and commit insert
	cursor. execute (sql, val)
	mydb. commit()
	print (cursor. rowcount) #Prints the number of successful insert to stdout

	#For debugging purpose. Please comment out when done.
	#cursor. execute ("SELECT * FROM elections")
	#myresult = cursor. fetchall()
	#for x in myresult:
	#	print (x)

if __name__ == '__main__':
	main ()
	sys.exit (0)
