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
        suites_excluded: list of suites that should not appear when the deck is created.
    """
    def __init__(self, shuffled=True, num_jokers=0, n=1, suites_excluded=None):
        self.deck = self.create_deck(num_jokers=num_jokers, n=n, suites_excluded=suites_excluded)
        if shuffled:
            self.shuffle()
        self.discard = []
        self.deck_size = len(self.deck)

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
    Returns a list of n * 52 + num_jokers unshuffled cards.
    jokers are all added at the end of each deck.
    
    inputs:
    num_jokers: determines the number of jokers added into the deck.
    n: determines how many decks are created.
    suites_excluded: used to remove certain suites from being added into the deck, passed in as a list or else fails.
    """
    @staticmethod
    def create_deck(num_jokers=0, n=1, suites_excluded=None):
        deck = []
        suites = list(Suites)[1:]
        if suites_excluded is not None:
            # check to make sure suites_excluded is a list
            if type(suites_excluded) is not list:
                raise ValueError(f"Expected {list} for suites_excluded, got {type(suites_excluded)} instead")
            for item in suites_excluded:
                if item not in Suites:
                    raise ValueError(f"Cannot pass in {item} as a suite!")
                suites.remove(item)

        for i in range(n):
            for suite in suites:
                for number in range(1, 14):
                    deck.append(Card(suite=suite, number=number))

        for i in range(num_jokers):
            deck.append(Card(suite="Joker", number=0))
        return deck

    """
    Returns the card on top of the deck, if n=1, or 
    """
    def draw(self, n=1):
        # cant draw negative cards
        if n < 1:
            raise ValueError("Cant draw less than 1 card!")
        # We could make it so that if there are no cards left in the deck, we shuffle the discard back
        # into the deck and continue drawing, but we would still need to check if the player is trying to draw
        # more cards than exist in the deck + discard.

        # If, in the future, we wanted to institute a hand limit, this would not be the place to modify.
        if n > len(self.deck):
            raise ValueError("For now, cannot draw more cards than exist in the deck!")
        if n is 1:
            return self.deck.pop(0)
        return [self.deck.pop(0) for i in range(n)]


    """
    Takes a card and adds it into the discard pile.
    """
    def discard(self, card):
        # make sure we dont try to add random data types to the discard pile.
        # One thing we could do is make sure we aren't adding a card that wasn't already in
        # the deck, but I dont believe that's nessesary, as many games have mechanics that will
        # give you cards that you didnt have before.
        assert isinstance(card, Card)
        self.discard.append(card)
        return

    """
    Takes a list of cards and adds it into the discard pile.
    """
    def discard_multiple(self, cards):
        # make sure we dont try to add random data types to the discard pile.
        for card in cards:
            assert isinstance(card, Card)
        self.discard += cards
        return

