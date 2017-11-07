//Actual program
//Coded by Kevin Lopez
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include"Person.h"
#include"Athlete.h"
#include<vector>
#include<string>
#include<sstream>

//create a vector of athletes to keep data in the memory
vector<Athlete> athletesVector;

//overload cout for printing objects from Athlete vector
std::ostream & operator<<(std::ostream & out, Athlete& a)
{
	out << a.getFirstName() << " " << a.getLastName() << " " << a.nationality << " " << a.jumpResult << "\n";
	return out;
}

void parseFile() {
		fstream athleteFile;
		athleteFile.open("jump.txt");

		/*If the file is open, as in the code found it we proceed*/
		if (athleteFile.is_open()) {
			cout << "The data is loaded successfully.\n";
			/*set of temp variables for reading from file*/
			string tmpFirstName, tmpLastName, tmpNationality, tmpJumpResult;
			Athlete tmpAthlete;

			while (!athleteFile.eof()) {
				/*read data from file using >> operator (yes it inherently does that)*/
				athleteFile >> tmpFirstName;
				athleteFile >> tmpLastName;
				athleteFile >> tmpNationality;
				athleteFile >> tmpJumpResult;

				/*convert tmpJumpResult from a string to a double*/
				//double tdblresult = stod(tmpJumpResult);
				double tdblresult;
				stringstream(tmpJumpResult) >> tdblresult;

				/*set the tmpAthlete values to the values read from the file*/
				tmpAthlete.setFirstName(tmpFirstName);
				tmpAthlete.setLastName(tmpLastName);
				tmpAthlete.setNationality(tmpNationality);
				tmpAthlete.setJumpResult(tdblresult);

				/*push values back so they stay in the record and don't get
				overwritten when we go to the next line*/
				athletesVector.push_back(tmpAthlete);
			}
		}
		/*Otherwise we shoot out an error.
		This should probably never happen*/
		else {
			cout << "Error: Something went wrong when opening the file!\nPlease restart the program";
		}
}

void displayRequestedDistance(double thr) {
	for (int i = 0; i < athletesVector.size(); i++) {
		/*loop through the vector and print any values
		that meet threshold*/
		if (athletesVector[i].jumpResult > thr) {
			cout << athletesVector[i];
		}
	}
}
/*verify that the value entered is a double.*/
bool checkIsDouble(string inputString, double &result) {
	/*This method is sourced from Aleksey Nikitenko from Stack Overflow:
	http://stackoverflow.com/questions/19349112/how-to-check-if-a-string-can-be-converted-to-double-in-c */
	char* end;
	result = strtod(inputString.c_str(), &end);
	if (end == inputString.c_str() || *end != '\0') return false;
	return true;
	delete(end);
}
/*get the user input and use the previous method
to make sure it's correct. If not we have a default*/
double getUserInput(){
	string in;
	double out;
	cout << "Enter jump result threshold: ";
	cin >> in;
	stringstream(in) >> out;
	/*Error checking
	(primitive but it works since we have no UI to speak of)*/
	if(checkIsDouble(in,out)==true){ return out; }
	else{
		cout << "You didn't enter a double, the default 8.0 will be used.\n";
		return 8.0;
	}
}

int main()
{
	parseFile();
	double d= getUserInput();
	displayRequestedDistance(d);
	system("pause");
	return 0;
}

