/*
	Reference: 
	C++ program to generate random password 
	https://www.includehelp.com/cpp-programs/generate-random-password.aspx
	Hritik Raj
	June 21, 2018 
*/
import std.stdio;
import std.string;
import std.conv;
import std.random;
import core.stdc.stdlib;

/*
	checks the arguements passed to the program.

	Param:
		args  	- args passed to program
		length 	- Pass by reference. Contains length of the password generated.
	Return:
		N/A
*/
void checkArg (string[] args, ref int length);

/*
	Generates a password of specified length.

	Param:
		length 	- Determines the length of the password.

	Return:
		A password containing 3 of the 4 class characteristics.
*/
string genPswd (int length);

void main (string[] args) {

	int length = 0;
	checkArg (args, length);	// Validates the command line arguments and gets length.
	string pswd = genPswd (length); // Generate a password of 
	
	//Store in file.
	File fl = File ("p5wd.txt", "w");
	fl.writeln (pswd);
	fl.close();

	exit (0);
}

void checkArg (string[] args, ref int length) {
	
	// If no command line argument provided, default to password length of 7.
	if (args.length == 1)
		length = 7;
	// If argument provided, check to see if it is a number and within range.
	else if (args.length == 2) {
		if (isNumeric(args[1])){
			length = to!int(args[1]); // converts argument to an integer.
			if (length < 6) {
				stderr.writeln ("Length must be greater or equal to 6 characters long.");
				exit (1);
			}
			else if (length > 50) {
				stderr.writeln ("Length can't exceed 50 characters in length.");
				exit(1);
			}
		}
		else {
			stderr.writeln ("Argument must be number.");
			exit (1);
		}
	}
	//User provided too many command line arguments.
	else {
		stderr.writeln ("Usage: ./createPswd [optional] #");
		exit (1);
	}
}

/*
	Generate a random number based on a specified range.
*/
auto getKey (int range) {
	auto rand = Random(unpredictableSeed);		// Get random generator with a new seed after each run.
	auto key = uniform (0, range, rand);  // generates a uniformly-distributed integer in the range of [1, 100]
	return (key % range);
}

string genPswd (int length) {
	int count = 0;
	string pswd = "";
	// Three of four possible password characteristic class: Upper, Lower, number
	string lowerAlpha = "abcdefghijklmnopqrstuvwxyz";
	string upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string numeric = "0123456789";

	while (count < length) {
		auto pswdCharClass = getKey (3);	// Choose a password characteristic class at random

		switch (pswdCharClass) {

			case 0	:	int select = getKey (26); // select from lower class
						pswd = pswd ~ lowerAlpha[select.. (select+1)]; //slice from lower string and add to password.
						break;
			case 1	:	int select = getKey (26); // select from upper
						pswd = pswd ~ upperAlpha[select.. (select+1)]; //slice from lower string and add to password.
						break;
			case 2	:	int select = getKey (10); // select from number
						pswd = pswd ~ numeric[select.. (select+1)]; //slice from lower string and add to password.
						break;
			default :
		}

		count++;
	}

	return pswd;
}
