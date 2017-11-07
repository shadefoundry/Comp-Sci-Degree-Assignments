//Implements Person.h
#include "stdafx.h"
#include"Person.h"
#include<iostream>

Person::Person() {
	firstName = "";
	lastName = "";
	nationality = "";
}

Person::Person(string f, string l, string n) {
	firstName = f;
	lastName = l;
	nationality = n;
}
