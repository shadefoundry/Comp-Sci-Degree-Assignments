/* 
 * File:   fibonacci.c
 * Author: Kevin Lopez
 *
 * Created on October 4, 2016, 12:08 PM
 */

#include <stdio.h>
#include <stdlib.h>
//define the fibonacci method that we'll use later
int fibonacci(int);
//main program

int main(int argc, char** argv) {
    //declare variables that we use.
    /*
     n is the number entered as well as the number of terms
     i is the value that we actually use to calculate
     c is our counting variable
     */
    unsigned long n, i = 0, c;
    //basic setup
    printf("Please enter the integer number n: ");
    scanf("%lu", &n);
    if (n < 0) {
        printf("Wrong input!");
    } else {
        printf("Fibonacci number F_%lu is: ", n);
        //for loop that recursively calls the fibonacci function
        for (c = 1; c <= n; c++) {
            //call the function
            fibonacci(i);
            i++;
        }
        //after the for loop is done this prints the final value
        printf("%d", fibonacci(i));
        return 0;
    }

}
//actual method that calculates the fibonacci sequence

int fibonacci(int n) {
    //the actual calculation
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return ( fibonacci(n - 1) + fibonacci(n - 2));
}
