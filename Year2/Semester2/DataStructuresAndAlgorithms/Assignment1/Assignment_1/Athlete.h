//Athlete header file with unimplemented data
//Coded by Kevin Lopez
#include "stdafx.h"
#ifndef ATHLETE_H
#define ATHLETE_H
#include<iostream>
#include"Person.h"

using namespace std;
class Athlete : public Person{
public:
	double jumpResult;
	Athlete();
	Athlete(string f, string l, string n, double j);
	/*getters and setters for jumpResult*/
	void setJumpResult(double r) { jumpResult = r; }
	double getJumpResult() { return jumpResult; }
};
std::ostream& operator<<(std::ostream& out, const Athlete& a);
#endif // !ATHLETE_H