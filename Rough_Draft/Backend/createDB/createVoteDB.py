#!/usr/bin/env python3
import mysql.connector

mydb = mysql.connector.connect (
		host="localhost",
		user="Michael Oranski",
		password="Password@2",
		auth_plugin='mysql_native_password'
	)

mycursor = mydb.cursor()
mycursor.execute ("CREATE DATABASE IF NOT EXISTS VoteDatabase")

mycursor.execute ("SHOW DATABASES")

for x in mycursor:
	print (x)

exit (0)