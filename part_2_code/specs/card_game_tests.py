import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.game = CardGame()
        self.card_1 = Card('clubs', 3)
        self.card_2 = Card('Diamonds', 1)
        self.card_3 = Card('Hearts', 3)
        self.card_4 = Card ('Hearts', 10)
        self.cards = [self.card_1, self.card_2, self.card_3, self.card_4]

    def test_check_for_ace_with_ace(self):
        actual = self.game.check_for_ace(self.card_2)
        self.assertEqual(True, actual)

    def test_check_for_ace_without_ace(self):
        actual = self.game.check_for_ace(self.card_1)
        self.assertEqual(False, actual)

    def test_highest_card(self):
        actual = self.game.highest_card(self.card_3, self.card_4)
        self.assertEqual(self.card_4, actual)

    def test_cards_total(self):
        actual = self.game.cards_total(self.cards)
        self.assertEqual('You have a total of 17', actual)