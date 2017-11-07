/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.c
 * Author: link491
 *
 * Created on October 28, 2016, 11:05 AM
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student {
    int comp, math, phys;
    int total;
    int id;
};

int main() {
    int i;
    struct student record[3];
    int x = 0;
    int y = 1;
    int z = 2;
    int a;
    for (i = 0; i < 3; i++) {
        //Note: I couldn't get strings working and I was sick of getting
        //aggravated so I decided to go with assigning the student an ID instead
        printf("Enter Student ID>");
        scanf("%i", &record[i].id);
        printf("Enter student %d marks for comp>", i + 1);
        scanf("%i", &record[i].comp);
        printf("Enter student %d marks for math>", i + 1);
        scanf("%i", &record[i].math);
        printf("Enter student %d marks for phys>", i + 1);
        scanf("%i", &record[i].phys);
        record[i].total = record[i].comp + record[i].math + record[i].phys;
    }

    //long string of if statements working with dummy variables to determine
    //order of students
    //1 switch 2
    if (record[0].total < record[1].total) {
        a = x;
        x = y;
        y = a;
    }
    //1 switch 3
    if (record[0].total < record[2].total) {
        a = x;
        x = z;
        z = a;
    }
    //2 switch 3
    if (record[1].total < record[2].total) {
        a = y;
        y = z;
        z = a;
    }

    //finally we print out the output
    printf("==================================\n");
    printf("Rank  Comp  Phys  Math  Total  ID\n   1    %i    %i    %i    %i   %i\n   2    %i    %i    %i    %i   %i\n   3    %i    %i    %i    %i   %i"
            , record[x].comp, record[x].phys, record[x].math, record[x].total, record[x].id
            , record[y].comp, record[y].phys, record[y].math, record[y].total, record[y].id
            , record[z].comp, record[z].phys, record[z].math, record[z].total, record[z].id);
    //printf("\n%i %i %i",record[x].total,record[y].total,record[z].total);
    return 0;
}

