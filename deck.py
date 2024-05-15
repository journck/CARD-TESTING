from card import Card

def create_unshuffled_deck():
    deck = []
    suits = ["s", "h", "d", "c"] # spades, hearts, diamonds, clubs
    for suit in suits:
        for value in range (1, 14):
            deck.append(Card(value, suit))
    return deck

perfect_deck = create_unshuffled_deck()

def print_deck(deck):
    for card in deck:
        print(card)

def faro_shuffle(deck):
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