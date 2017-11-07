/* 
 * File:   dochange.c
 * Author: Kevin Lopez
 *
 * Created on October 4, 2016, 1:12 PM
 */

#include <stdio.h>
#include <stdlib.h>
//array of coin names to let us use a for loop for output
char names[5][16]={"Penny(ies)","Nickel(s)","Dime(s)","Quarter(s)","Dollar(s)"};
int dochange(int);
int change [ 4 ];

int main(int argc, char** argv) {
    
    int currentCents;
    int i;
    printf("Please enter the amount you would like changed: ")
    scanf("%d",&currentCents);
    if(currentCents<0){printf("Wrong amount!");}else{
    dochange(currentCents);
    for(i=4;i>=0;i--){
        printf("%d %s\n",change[i],names[i]);
    }
    //create an array
    //get the user input and send it to dochange
    return (EXIT_SUCCESS);
    }
}
int dochange(int i){
    //initialize the three variables i'm using to set values
    //this method is probably done in the worst way possible
    //but to be honest it works so i'm happy.
    double divider;
    int amountRemaining = i;
    int arrayValue;
    //get the number of dollars and add them to the array
    divider = i/100;
    arrayValue = divider;
    amountRemaining = amountRemaining-(arrayValue*100);
    change[4] = arrayValue;
    //now do the same for quarters
    divider = amountRemaining/25;
    arrayValue = divider;
    amountRemaining = amountRemaining-(arrayValue*25);
    change[3] = arrayValue;
    //next we go through the dimes
    divider = amountRemaining/10;
    arrayValue = divider;
    amountRemaining = amountRemaining-(arrayValue*10);
    change[2] = arrayValue;
    //next nickles
    divider = amountRemaining/5;
    arrayValue = divider;
    amountRemaining = amountRemaining-(arrayValue*5);
    change[1] = arrayValue;
    //finally the easy one, pennies
    change[0]=amountRemaining;
}

