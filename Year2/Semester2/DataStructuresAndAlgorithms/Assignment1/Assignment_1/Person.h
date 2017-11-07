#include "stdafx.h"
#ifndef PERSON_H
//Contains unimplemented information for Person
#define PERSON_H
#include<iostream>
#include<string>

using namespace std;
class Person {
public:
	string firstName, lastName, nationality;
	/*Constructors*/
	Person();
	Person(string f, string l, string n);
	/*Getters and setters*/
	string getFirstName() { return firstName; }
	void setFirstName(string fn) { firstName = fn; }
	string getLastName() { return lastName; }
	void setLastName(string ln) { lastName = ln; }
	string getNationality() { return nationality; }
	void setNationality(string n) { nationality = n; }
};
#endif // !PERSON_H
