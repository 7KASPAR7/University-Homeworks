from unittest import TestCase, main
from hangman_logic import gues

word1 = ['_', '_', '_', '_', '_', '_']
word2 = ['_', 'Г', '_', 'А', '_', 'А']
used = ['Г', 'У', 'А', 'И']


class Tests(TestCase):
    def test_valid_values(self):
        self.assertEqual(gues('и', 5, 'ПИКНИК', word1, [], 0, 0), (5, 2))
        self.assertEqual(gues('О', 3, 'ОГРАДА', word2, used, 0, 3), (3, 4))


main()
