from card import Card
from random import choice, random

"""
A generic version of a deck of cards, not specifically build for tomb of the four kings.
Contains a deck of cards, and a discard pile. Why the discard pile? so we can check which cards have been drawn or not.

"""
class Deck:

    def __init__(self, joker=False):
        self.deck = self.create_deck(joker=joker)
        self.shuffle()
        self.discard = []

    def __repr__(self):
        print("Deck: ")
        for card in self.deck:
            print(card)
        print("Discard: ")
        for card in self.discard:
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
    Reshuffles the discard pile back into the deck.
    """
    def reshuffle(self):
        self.deck += self.discard
        self.shuffle()
        self.discard = []

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
