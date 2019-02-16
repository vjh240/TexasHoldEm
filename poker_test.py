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

    def test_hand_strength_with_two_pair(self):
        hand = ["2c", "2d", "4c", "4d", "6c"]
        self.assertEqual(hand_strength(hand), 2)

    def test_hand_strength_with_three_of_a_kind(self):
        hand = ["2c", "4c", "4c", "4d", "6c"]
        self.assertEqual(hand_strength(hand), 3)

    def test_hand_strength_with_straight_ace_to_5(self):
        hand = ["14d", "2c", "3c", "4c", "5c"]
        self.assertEqual(hand_strength(hand), 4)

    def test_hand_strength_with_straight_10_to_ace(self):
        hand = ["14d", "10c", "11c", "12c", "13c"]
        self.assertEqual(hand_strength(hand), 4)

    def test_hand_strength_with_flush(self):
        hand = ["2c", "10c", "11c", "12c", "13c"]
        self.assertEqual(hand_strength(hand), 5)

    def test_hand_strength_with_full_house(self):
        hand = ["14d", "14c", "14s", "12c", "12d"]
        self.assertEqual(hand_strength(hand), 6)

    def test_hand_strength_with_four_of_a_kind(self):
        hand = ["14d", "14c", "14s", "14h", "13c"]
        self.assertEqual(hand_strength(hand), 7)

    def test_hand_strength_with_straight_flush_ace_to_5(self):
        hand = ["14c", "2c", "3c", "4c", "5c"]
        self.assertEqual(hand_strength(hand), 8)

    def test_hand_strength_with_straight_flush_10_to_ace(self):
        hand = ["14c", "10c", "11c", "12c", "13c"]
        self.assertEqual(hand_strength(hand), 8)


if __name__ == '__main__':
    unittest.main()