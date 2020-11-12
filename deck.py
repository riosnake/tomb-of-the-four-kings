from card import Card, Suites
import random

"""
A generic version of a deck of cards, not specifically built for tomb of the four kings.
Contains a deck of cards, and a discard pile so we can check which cards have been drawn or not.

usage of len, iter, and getitem are to go over the cards in the current facedown deck, not all cards present in the deck class.
to go through all cards within the deck class, use varName.allCards()
"""
class Deck:

    """
    Sets up the deck of cards
    Parameters:
        shuffled: sets whether the deck should start out shuffled or not
        num_jokers: sets how many jokers should appear in the deck
        n: determines how many decks of 52 cards are created and used
    """
    def __init__(self, shuffled=True, num_jokers=0, n=1):
        self.deck = self.create_deck(num_jokers=num_jokers, n=n)
        if shuffled:
            self.shuffle()
        self.hand = []
        self.discard = []

    def __repr__(self):
        print("Deck: ")
        for card in self.deck:
            print(card)
        print("Discard: ")
        for card in self.discard:
            print(card)

    def __iter__(self):
        return iter(self.deck)

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, item):
        return self.deck[item]


    """
    Shuffles the current deck.
    """
    def shuffle(self):
        self.deck = [self.deck.pop(random.randint(0, len(self.deck) - 1)) for i in range(len(self.deck))]

    """
    Reshuffles the discard pile back into the deck.
    """
    def reshuffle(self):
        self.deck += self.discard
        self.shuffle()
        self.discard = []

    """
    Returns a deck of n * 52 + num_jokers unshuffled cards.
    jokers are all added at the end of each deck.
    """
    @staticmethod
    def create_deck(num_jokers=0, n=1):
        deck = []
        for i in range(n):
            for suite in list(Suites)[1:]:
                for number in range(1, 14):
                    deck.append(Card(suite=suite, number=number))

        for i in range(num_jokers):
            deck.append(Card(suite="Joker", number=0))
        return deck

    """
    Returns the first card in the deck, and adds it to the end of the discard pile
    """
    def draw(self):
        card = self.deck.pop(0)
        self.discard.append(card)
        return card

    """
    Returns a list of x cards drawn from the top of the deck.
    """
    def draw_multiple(self, num_of_cards_to_draw):
        cards = [self.deck.pop(0) for i in range(num_of_cards_to_draw)]
        self.discard += cards
        return cards
