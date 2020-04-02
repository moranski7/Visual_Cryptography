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

	tableOne = "CREATE TABLE IF NOT EXISTS voters"\
	"(UserName VARCHAR (255) UNIQUE NOT NULL,"\
	"FirstName VARCHAR (255) NOT NULL,"\
	"LastName VARCHAR (255) NOT NULL,"\
	"DOB DATE,"\
	"Age INT,"\
	"Gender VARCHAR (20),"\
	"VoterID INT AUTO_INCREMENT PRIMARY KEY)"

	tableTwo = "CREATE TABLE IF NOT EXISTS elections"\
	"(Name VARCHAR (550) UNIQUE NOT NULL,"\
	"StartDate DATE NOT NULL,"\
	"EndDate DATE NOT NULL,"\
	"Description TEXT(100000),"\
	"ElectID INT AUTO_INCREMENT PRIMARY KEY)"

	tableThree = "CREATE TABLE IF NOT EXISTS voterShares ("\
	"Img MEDIUMBLOB NOT NULL,"\
	"ElectStart DATE NOT NULL,"\
	"ElectEnd DATE NOT NULL,"\
	"Elect_ID INT NOT NULL,"\
	"Voter_ID INT NOT NULL,"\
	"FOREIGN KEY (Elect_ID) REFERENCES elections (ElectID),"\
	"FOREIGN KEY (Voter_ID) REFERENCES voters (VoterID))"

	cursor. execute (tableOne)
	cursor. execute (tableTwo)
	cursor. execute (tableThree)
	cursor. execute ("SHOW TABLES")

	print ("Tables created: ")
	for x in cursor:
		print (x)

#	cursor. execute ("DROP TABLE IF EXISTS voterShares")
#	cursor. execute ("DROP TABLE IF EXISTS voters")
#	cursor. execute ("DROP TABLE IF EXISTS elections")


if __name__ == '__main__':
	main ()
	exit (0)
