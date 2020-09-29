from card import Card
from random import choice, random

class Deck:

    def __init__(self, joker=False):
        self.deck = self.create_deck(joker=joker)
        self.shuffle()

        self.discard = []

    def __repr__(self):
        for card in self.deck:
            print(card)
    """
    Given a list of cards, returns a random ordering of those cards
    note that this DOES empty the list containing the old deck, so usage should look like
    deck = Card.shuffle(deck)
    """
    @staticmethod
    def shuffle(deck):
        # using list comprehension,
        return [deck.pop(random.randint(0, len(deck) - 1)) for i in range(len(deck))]

    """non-static version of shuffle."""
    def shuffle(self):
        # using list comprehension,
        return [self.deck.pop(random.randint(0, len(self.deck) - 1)) for i in range(len(self.deck))]
    """
    Returns a deck of 52 unshuffled cards.
    setting joker to true adds a joker to the end
    """


    @staticmethod
    def create_deck(joker=False):
        deck = []
        for suite in ["Spades", "Diamonds", "Clubs", "Hearts"]:
            for number in range(1, 14):
                deck.append(Card(suite=suite, number=number))
        if joker:
            deck.append(Card(suite="Joker", number=0))
        # Right here would be where you would shuffle the deck if we wanted that option.
        return deck