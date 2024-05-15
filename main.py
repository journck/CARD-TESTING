# std imports
import sys
import math
import time
import timeit
import colorsys
import contextlib

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

def main():
    workingDeck = create_unshuffled_deck()
    lines_from_deck(workingDeck)


    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()
        while term.inkey() not in (u'q', u'Q'):
            # print(term.home + term.clear)
            workingDeck = faro_shuffle(workingDeck)
            lines_from_deck(workingDeck)

    main()

if __name__ == "__main__":
    main()