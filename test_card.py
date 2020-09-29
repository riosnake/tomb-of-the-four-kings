from card import Card
from deck import Deck
from random import seed
import unittest


class TestCard(unittest.TestCase):
    # Note that I've manually tested create_deck, and can affirm that it does generate a 52 card deck

    # Shuffle Tests
    # All cards made it into the shuffled deck
    def test_shuffle_1(self):
        seed(12)
        deck = Deck.shuffle(Card.create_deck())
        new_deck = Card.create_deck()
        for card in deck:
            assert card in new_deck, f"{card} not found in {new_deck}"

    # different ordering from a brand new deck
    # Though this is very unlikely, it is actually mathmatically possible that you shuffle a deck
    # and get the same deck again, but that's so unlikely we can ignore it
    def test_shuffle_2(self):
        seed(12)
        deck = Deck.shuffle(Card.create_deck())
        new_deck = Card.create_deck()

        is_different = False
        for i in range(len(deck)):
            if deck[i] != new_deck[i]:
                is_different = True
                break
        self.assertEqual(is_different, True, "Cards not in a different ordering from before")


if __name__ == "__main__":
    unittest.main()

