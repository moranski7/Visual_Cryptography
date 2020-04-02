#!/usr/bin/env python3
import mysql.connector

def main ():
	mydb = mysql.connector.connect (
			host="localhost",
			user="Michael Oranski",
			password="Password@2",
			database='VoteDatabase',
			auth_plugin='mysql_native_password'
		)
	cursor = mydb.cursor()

	cursor. execute ("DROP TABLE IF EXISTS voterShares");
	cursor. execute ("DROP TABLE IF EXISTS voters");
	cursor. execute ("DROP TABLE IF EXISTS elections");
	

if __name__ == '__main__':
	main()
	exit (0)
