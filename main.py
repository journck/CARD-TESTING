# std imports
import sys
import math
import time
import timeit
import colorsys
import contextlib
import random

# local
from blessed import Terminal
from card import Card
from deck import *

term = Terminal()

def line_from_card(card):
    valueString = card.get_value_string()
    match card.suit:
        case "s":
            print(term.black_on_lightgray(term.center(valueString)))
        case "h":
            print(term.black_on_red(term.center(valueString)))
        case "d":
            print(term.black_on_mistyrose(term.center(valueString)))
        case "c":
            print(term.white_on_black(term.center(valueString)))
        
def lines_from_deck(deck):
    print(term.home)
    for card in deck:
        line_from_card(card)

def test_equivalence(perfect_deck, questioning_deck):
    assert len(perfect_deck) == len(questioning_deck)
    for i in range(len(perfect_deck)):
        card1 = perfect_deck[i]
        card2 = questioning_deck[i]
        if card1.value != card2.value or card1.suit != card2.suit:
            return False
    return True
    
def main():
    num_shuffles = 0
    auto_play = False
    shouldExit = False
    print(term.clear + term.home)
    startingDeck = create_deck()
    workingDeck = startingDeck.copy()
    lines_from_deck(workingDeck)
    


    with term.cbreak(), term.hidden_cursor():
        ind = term.inkey()
        if (ind == ' '):
            auto_play = True
        while (auto_play or term.inkey() != u'q'):
            shouldExit = False
            print(ind)
            print(term.clear + term.home)
            workingDeck = faro_shuffle(workingDeck,2)
            num_shuffles += 1
            lines_from_deck(workingDeck)
            if test_equivalence(startingDeck, workingDeck):
                print(term.center("") + term.black_on_green(term.center("THE DECK IS SORTED | SHUFFLES: " + str(num_shuffles))))
                num_shuffles = 0
                term.inkey()
            else:
                print(term.center("") + term.black_on_red(term.center("THE DECK IS NOT SORTED | SHUFFLES: " + str(num_shuffles))))
            if auto_play:
                time.sleep(0.1)


    main()

if __name__ == "__main__":
    main()