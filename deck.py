from card import *

def create_deck(max_value=14):
    deck = []
    suits = ["s", "h", "d", "c"] # spades, hearts, diamonds, clubs
    for suit in suits:
        for value in range (1, max_value):
            deck.append(Card(value, suit))
    return deck

perfect_deck = create_deck()

def print_deck(deck):
    for card in deck:
        print(card)

def faro_shuffle(deck): # assume deck is 52 cards, use 2 piles
    left_deck = []
    right_deck = []
    for c in range(0, 26):
        left_deck.append(deck[c])
        right_deck.append(deck[c + 26])
    shuffled_deck = []
    for c in range(0, 26):
        shuffled_deck.append(left_deck[c])
        shuffled_deck.append(right_deck[c])
    return shuffled_deck

def faro_shuffle(deck, num_piles):
    assert len(deck) % num_piles == 0 # deck is divisible evenly into piles

    # split into piles 
    pile_size = len(deck) // num_piles
    piles = []
    for i in range(num_piles):
        piles.append(deck[i * pile_size:(i + 1) * pile_size])

    new_shuffled_deck = []

    # interleave piles
    for i in range(pile_size):
        for pile in piles:
            new_shuffled_deck.append(pile[i])
    return new_shuffled_deck
