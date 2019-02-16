from poker import hand_strength
import unittest
from unittest import TestCase

class TestPoker(TestCase):
    def test_hand_strength_with_high_card(self):
        hand = ["2c", "4c", "6d", "8d", "10s"]
        self.assertEqual(hand_strength(hand), 0)

    def test_hand_strength_with_one_pair(self):
        hand = ["2c", "4c", "4c", "5d", "6c"]
        self.assertEqual(hand_strength(hand), 1)


if __name__ == '__main__':
    unittest.main()