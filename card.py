import random
import enum

# quick enum for card suites.
class Suites(enum.Enum):
    Joker = 0
    Spades = 1
    Diamonds = 2
    Clubs = 3
    Hearts = 4

class Card:

    """
    How cards are represented in this game
    Each card has a suite(these are the types), and a number(1-13)
    Default constructor will randomly create a card.
    """
    def __init__(self, suite=None, number=None):
        # convert suite to a proper enum if using str
        if type(suite) is str:
            suite = Suites[suite]
        # sanitize the inputs
        if suite not in Suites:
            raise ValueError(f"Suite can only be Diamonds, Hearts, Clubs, Spades, or Joker.\nPassed in {suite}")
        if number == 0 and suite != Suites.Joker:
            raise ValueError(f"Only the Joker may have the number 0 as it's value\nPassed in {suite}")
        if suite == Suites.Joker and number != 0:
            raise ValueError(f"The Joker may only have the number 0 as it's value\nPassed in {number}")
        elif number not in range(0, 14):
            raise ValueError(f"Number can only be 1 through 13\nPassed in {number}")

        if number is not None:
            self.number = number
        else:
            self.number = random.choice(range(1, 14))

        if suite is not None:
            self.suite = suite
        else:
            # excludes the joker from being a possible choice randomly generated card.
            # would be too much work to implement a proper joker implementation for too little payoff.
            self.suite = random.choice(list(Suites)[1:])

    def __repr__(self):
        if self.number not in [1,11,12,13]:
            return f"{self.number} of {self.suite.name}"
        elif self.number == 1:
            return f"Ace of {self.suite.name}"
        elif self.number == 11:
            return f"Jack of {self.suite.name}"
        elif self.number == 12:
            return f"Queen of {self.suite.name}"
        else:
            return f"King of {self.suite.name}"

    """
    One thing to note is that, while it would make sense to create a __lt__ or __gt__ for cards,
    we cannot do so accurately without knowing the rules of the game. As a quick example, in some games the ace trumps a king,
    but in others the king is the highest card you can obtain. Therefore, it makes sense to seperate comparisons of cards within
    code for those games only, and not here.
    """
    def __eq__(self, other):
        return self.suite == other.suite and self.number == other.number

    def __hash__(self):
        return hash((self.suite, self.number))
