import random
import unittest

class Card:
    """
    How cards are represented in this game
    Each card has a suite(these are the types), and a number(1-13)
    Default constructor will randomly create a card.
    """
    def __init__(self, suite=None, number=None):
        # sanitize the inputs

        if suite not in ["Diamonds", "Hearts", "Clubs", "Spades", "Joker"]:
            raise ValueError(f"Suite can only be Diamonds, Hearts, Jacks, Spades, or Joker.\nPassed in {suite}")
        if number == 0 and suite != "Joker":
            raise ValueError(f"The Joker may only have the number 0 as it's value\nPassed in {number}")
        elif number not in range(1, 14):
            raise ValueError(f"Number can only be 1 through 13\nPassed in {number}")

        if number is not None:
            self.number = number
        else:
            self.number = random.choice(range(1, 14))

        if suite is not None:
            self.suite = suite
        else:
            self.suite = random.choice(["Diamonds", "Hearts", "Jacks", "Spades"])

    def __repr__(self):
        if self.number not in [1,11,12,13]:
            return f"{self.number} of {self.suite}"
        elif self.number == 1:
            return f"Ace of {self.suite}"
        elif self.number == 11:
            return f"Jack of {self.suite}"
        elif self.number == 12:
            return f"Queen of {self.suite}"
        else:
            return f"King of {self.suite}"

    def __eq__(self, other):
        return self.suite == other.suite and self.number == other.number





