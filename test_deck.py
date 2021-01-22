from card import Card, Suites
from deck import Deck
from random import seed
from collections import Counter
import unittest

# a standard 52 card deck without a joker.
correct_deck = [Card("Spades", 1), Card("Spades", 2), Card("Spades", 3), Card("Spades", 4),
                Card("Spades", 5), Card("Spades", 6), Card("Spades", 7), Card("Spades", 8),
                Card("Spades", 9), Card("Spades", 10), Card("Spades", 11), Card("Spades", 12), Card("Spades", 13),
                Card("Diamonds", 1), Card("Diamonds", 2), Card("Diamonds", 3), Card("Diamonds", 4),
                Card("Diamonds", 5), Card("Diamonds", 6), Card("Diamonds", 7), Card("Diamonds", 8),
                Card("Diamonds", 9), Card("Diamonds", 10), Card("Diamonds", 11), Card("Diamonds", 12), Card("Diamonds", 13),
                Card("Clubs", 1), Card("Clubs", 2), Card("Clubs", 3), Card("Clubs", 4),
                Card("Clubs", 5), Card("Clubs", 6), Card("Clubs", 7), Card("Clubs", 8),
                Card("Clubs", 9), Card("Clubs", 10), Card("Clubs", 11), Card("Clubs", 12), Card("Clubs", 13),
                Card("Hearts", 1), Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4),
                Card("Hearts", 5), Card("Hearts", 6), Card("Hearts", 7), Card("Hearts", 8),
                Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Hearts", 12), Card("Hearts", 13)]

class TestDeck(unittest.TestCase):

    # Deck Creation Tests
    # Test creation of standard unshuffled deck
    def test_create_1(self):
        deck = Deck(shuffled=False)
        self.assertSequenceEqual(deck, correct_deck, "created deck and unmodified deck were not equal")

    # test creation of standard shuffled deck
    def test_create_2(self):
        deck = Deck(shuffled=True)
        for card in correct_deck:
            self.assertIn(card, deck, f"{card} was not found in the deck")

    # test creation of shuffled deck with a joker
    def test_create_3(self):
        deck = Deck(num_jokers=1)
        for card in correct_deck:
            self.assertIn(card, deck, f"{card} was not found in the deck")
        self.assertIn(Card("Joker", 0), deck)

    # test num_jokers properly works
    def test_create_4(self):
        deck = Deck(num_jokers=2000)
        count = Counter(deck)
        num_of_jokers = count.get(Card("Joker", 0))
        self.assertEqual(num_of_jokers, 2000, f"Expected 2000 jokers in deck, got {num_of_jokers} instead.")

    # test creation of two unshuffled decks.
    def test_create_5(self):
        deck = Deck(n=2, shuffled=False)
        for i in range(len(deck)):
            self.assertEqual(deck[i], correct_deck[i%52], f"Expected {correct_deck[i%52]}, got {deck[i]} instead")

    # stress test creation of 200 unshuffled decks
    def test_create_6(self):
        deck = Deck(n=200, shuffled=False)
        for i in range(len(deck)):
            self.assertEqual(deck[i], correct_deck[i % 52], f"Expected {correct_deck[i%52]}, got {deck[i]} instead")

    # test creation of 2 shuffled decks
    def test_create_7(self):
        deck = Deck(n=2)
        card_count = Counter(deck)
        for card in correct_deck:
            self.assertIn(card, deck, f"Expected to find {card} in deck, found no such card")
        for card, count in card_count.items():
            self.assertEqual(count, 2, f"Expected to find 2 of {card}, found {count} instead")

    # stress test creation of 2000 shuffled decks
    def test_create_8(self):
        deck = Deck(n=2000)
        card_count = Counter(deck)
        for card in correct_deck:
            self.assertIn(card, deck, f"Expected to find {card} in deck, found no such card")
        for card, count in card_count.items():
            assert count == 2000, f"Expected to find 2000 of {card}, found {count} instead"

    # stress test creation of 1000 d=shuffled decks with jokers in them
    def test_create_9(self):
        deck = Deck(n=1000, num_jokers=3000)
        card_count = Counter(deck)
        for card in correct_deck:
            self.assertIn(card, deck, f"Expected to find {card} in deck, found no such card")
        for card, count in card_count.items():
            if card.suite == Suites.Joker:
                self.assertEqual(count, 3000, f"Expected to find 3000 of Joker, found {count} instead.")
            else:
                self.assertEqual(count, 1000, f"Expected to find 1000 of {card}, found {count} instead")

    # tests that excluding a suite works.
    def test_create_10(self):
        deck = Deck(suites_excluded=[Suites.Hearts])
        for card in deck:
            self.assertNotEqual(card.suite, Suites.Hearts, f"Expected all cards of type heart to be excluded, found {card} instead.")

    # tests that excluding multiple suites works
    def test_create_11(self):
        deck = Deck(suites_excluded=[Suites.Hearts, Suites.Spades])
        for card in deck:
            self.assertNotEqual(card.suite, Suites.Hearts, f"Expected all cards of type hearts to be excluded, found {card} instead")
            self.assertNotEqual(card.suite, Suites.Spades, f"Expected all cards of type spades to be excluded, found {card} instead")

    # tests that passing in a wrong argument properly crashes
    def test_create_12(self):
        with self.assertRaises(ValueError):
            deck = Deck(suites_excluded="Hearts")
            deck = Deck(suites_excluded={"Hearts"})
            deck = Deck(suites_excluded=["Hearts"])

    # tests excluding suites from a deck with multiple cards.
    def test_create_13(self):
        deck = Deck(n=4, suites_excluded=[Suites.Hearts])
        for card in deck:
            self.assertNotEqual(card.suite, Suites.Hearts, f"Expected all cards of type hearts to be excluded, found {card} instead")

    # tests that drawing a card gives you a card to work with.
    def test_draw_1(self):
        deck = Deck()
        card_drawn = deck.draw()
        self.assertIsInstance(card_drawn, Card, f"deck.draw() did not return a card")

    # tests that drawing a card gives you the first card in the deck.
    def test_draw_2(self):
        deck = Deck()
        first_card = deck[0]
        card_drawn = deck.draw()
        self.assertEqual(first_card, card_drawn, f"{card_drawn} and {first_card} are not the same")

    # tests that drawing a card removes that card from the deck.
    def test_draw_3(self):
        deck = Deck()
        card_drawn = deck.draw()
        self.assertNotIn(card_drawn, deck, f"found {card_drawn} in deck when drawn from the deck")

    # tests that drawing a card does not change the ordering of the deck.
    def test_draw_4(self):
        deck = Deck()
        card_drawn = deck.draw()

    # tests that calling draw on an empty deck will reshuffle the discard pile back into the deck.
    # def test_draw_5(self):



if __name__ == "__main__":
    unittest.main()

