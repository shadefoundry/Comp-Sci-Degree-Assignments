//This file implemets Athlete.h
//Coded by Kevin Lopez
#include "stdafx.h"
#include<iostream>
#include"Person.h"
#include"Athlete.h"
Athlete::Athlete()
{
	firstName = "";
	lastName = "";
	nationality = "";
	jumpResult = 0.0;
}

Athlete::Athlete(string f, string l, string n, double j){
	firstName = f;
	lastName = l;
	nationality = n;
	jumpResult = j;
}
