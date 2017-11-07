// Lopez_Assignment_3.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <string>
#include "Lopez_Assignment_3.h"
using namespace std;


class Customer {
public:
	/*Define 3 arrays for documenting information of calls.
	They're each the max number of calls + 1 so they don't break.
	This is so I don't need to deal with the abomination that is vectors.*/
	string calledNumbers[101];
	string callDate[101];
	int callTimes[101];
	string name;
	double balance;
	double bill;
	double monthlyFee = 10.00;
	double perCall = 0.5;
	int numCalls = 0;
	int callMinutes = 0;
	string planType;
	double perMin = 0.1;
	int savings;
	/*adds a new call,
	increasing call minutes by time and numCalls by 1
	also adds call time, date and number to seperate arrays*/
	void addCall(int time, string date, string number,int i) {
		callMinutes += time;
		numCalls+=1;
		calledNumbers[i] = number;
		callDate[i] = date;
		callTimes[i] = time;
	}
	//calculate the cost of the bill
	double computeBill() {
		bill = monthlyFee + (perCall * numCalls);
		return bill;
	}

};

class PremiumCustomer :public Customer {
public:
	double perMin = 0.1;
	double perCall = 0.05;
	int savings;
	double monthlyFee = 20.0;
	//compute the premium bill (which somehow seems worse to me)
	double computeBill() {
		bill = monthlyFee + (perCall*numCalls) + (perMin*callMinutes);
		return bill;
	}
};
/*define all the lists that we generate customers from later
These are generated outside the main loop so we can access them in other methods.*/
Customer list[6];
string names[6] = { "Peter Parker","Steve Rogers","Tony Stark",
"Bruce Wayne","Bruce Banner","Clark Kent" };
string numbers[6] = { "(151) 170-6646","(492) 826-1287","(865) 944-0285",
"(438) 390-0987","(195) 683-6371","(636) 763-5130" };
string date_times[6] = { "2016-12-13","2016-12-15","2016-12-20",
"2016-12-21","2016-12-27","2016-12-29" };

/*Calculates % savings from premium plan compared to regular plan.*/
int computeSavings(int callMins, int numCalls) {
	double basicPrice;
	double premiumPrice;
	int percentSavings;
	basicPrice = 10 + (0.5*numCalls);
	premiumPrice = 20 + (0.05*numCalls) + (0.1*callMins);
	percentSavings = (basicPrice / premiumPrice) * 100;
	return percentSavings;
}

/*Prints the call time, date and which number it was to.*/
void printBill() {
	/*Print the bill of whatever customer the for loop decides.
	outputs customer name, plan type, each call, it's time and date, and the number called*/
	int i,j;
	for (i = 0; i < 6; i++) {
		cout << list[i].name << "\n";
		for (j = 0; j < list[i].numCalls; j++) {
			//print all the calls for each user
			cout << list[i].planType
				<< "||Call # " << j
				<< "||Number Called: " << list[i].calledNumbers[j]
				<< "||" << list[i].callDate[j]
				<< "||" << list[i].callTimes[j];
			/*If the user is premium, print their savings.
			Otherwise we just go to another line*/
			if (list[i].planType == "Premium") {
				cout << "||Savings vs Basic Call: " << computeSavings(list[i].callMinutes, list[i].numCalls) << "%\n";
			}
			else { cout << "\n"; }
		}
	}
	
}

int main(int argc, char** argv) {
	int i,j,k,l,m;

	/*for loop that randomly generates the customer values because I don't
	care enough to manually define them myself. It also does all the tests
	and things because again, I can't be asked.*/
	for (i = 0; i < 6; i++) {
		/*randomly decide what type of customer we're creating
		0 is basic, 1 is premium.*/
		j = rand() % 2;
		//if j is 0 it's a regular customer
		if (j == 0) {
			Customer c;
			/*select the customer name from the predefined table
			and randomly generate a balance between 0 and 100*/
			c.name = names[i];
			c.balance = rand() % 100;
			c.planType = "Basic";
			list[i] = c;
		}
		//otherwise it's premium and we create one of those
		else {
			PremiumCustomer pc;
			pc.name = names[i];
			pc.balance = rand() % 100;
			pc.planType = "Premium";
			list[i] = pc;
		}
	}

	/*Goes through each member to handle adding calls.*/
	for (i = 0; i < 6; i++) {
		/*Generate a random number to signify how many calls the user made
		this month. I'm working with 1 to 100. The way we go with it is a bit
		of a workaround since it manually sets the minimum instead of doing it
		with an equation but this way is easier so I can't be tossed to do it
		the other way.*/
		l = (rand() % 90)+10;
		/*nested for loop adds the random number of calls, 1 to 10,
		each with random number of minutes between 4 and 240 (4 hours)*/
		for (k = 0; k < l; k++) {
			//random number for number of minutes, 4 to 240
			j = rand() % 237+4;
			//random number for call number
			m = rand() % 6;
			list[i].addCall(j,date_times[m],numbers[m],k);
		}
	}
	
	printBill();
	/*input doesn't matter here
	it just exists for debugging in Visual Studio*/
	cin >> i;
	return EXIT_SUCCESS;
}

