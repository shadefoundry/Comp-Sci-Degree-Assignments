#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* card structure definition */
struct card {
    const char *face; /* define pointer face */
    const char *suit; /* define pointer suit */
}; /* end structure card */

typedef struct card Card; /* new type name for struct card */

/* prototypes */
void fill_deck(Card * const _deck, const char*_face[],
        const char*_suit[]);
void shuffle_deck(Card * const _deck);
void print_deck(const Card * const _deck);

int main(void) {
    //create an array of card objects
    Card deck[52];

    //create two pointer arrays of the numbers and suits so we can generate the deck later
    const char *face[] = {"2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"};
    const char *suit[] = {"Clubs", "Diamonds", "Hearts", "Spades"};

    //define an instance of random
    srand(time(NULL));

    fill_deck(deck, face, suit);
    print_deck(deck);
    shuffle_deck(deck);
    //I know it's not asked for but this divider makes reading the output far easier.
    printf("\n==========================================================================================\n\n");
    print_deck(deck);

    return 0;

}

void fill_deck(Card * const _deck, const char*_face[], const char*_suit[]) {
    int i;
    //generate the deck
    for (i = 0; i <= 51; i++) {
        _deck[i].face = _face[i % 13];
        _deck[i].suit = _suit[i / 13];
    }
}

void shuffle_deck(Card * const _deck) {
    int i, j;
    //temporary card to use for randomization
    Card temp;

    for (i = 0; i <= 51; i++) {
        j = rand() % 52;
        temp = _deck[i];
        _deck[i] = _deck[j];
        _deck[j] = temp;
    }
}

void print_deck(const Card * const _deck) {
    int i;

    for (i = 0; i <= 51; i++) {
        //fancy printf to divide the output into 4 columns
        printf("%5s of %-8s%c", _deck[i].face, _deck[i].suit, (i + 1) % 4 ? '\t' : '\n');
    }
}