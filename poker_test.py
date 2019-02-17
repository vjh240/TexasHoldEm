from poker import hand_strength, straight_tie, full_house_tie, four_of_a_kind_tie, high_card_tie, three_of_a_kind_tie, two_pair_tie, one_pair_tie
import unittest
from unittest import TestCase

class TestHandStrength(TestCase):
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

class TestTieBreakers(TestCase):
    def test_straight_tie_breaker1(self):
        numbers_hand1 = [3,4,5,6,7]
        numbers_hand2 = [2,3,4,5,6]
        result = straight_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_straight_tie_breaker2(self):
        numbers_hand1 = [2,3,4,5,6]
        numbers_hand2 = [3,4,5,6,7]
        result = straight_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,2)

    def test_straight_tie_breaker3(self):
        numbers_hand1 = [2,3,4,5,6]
        numbers_hand2 = [2,3,4,5,6]
        result = straight_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,3)

    def test_full_house_tie_breaker1(self):
        numbers_hand1 = [3,3,3,7,7]
        numbers_hand2 = [2,2,2,5,5]
        result = full_house_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_full_house_tie_breaker2(self):
        numbers_hand1 = [2,2,2,8,8]
        numbers_hand2 = [6,6,6,3,3]
        result = full_house_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,2)

    def test_four_of_a_kind_tie_breaker1(self):
        numbers_hand1 = [3,3,3,3,7]
        numbers_hand2 = [2,2,2,2,5]
        result = four_of_a_kind_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_four_of_a_kind_tie_breaker2(self):
        numbers_hand1 = [2,2,2,2,8]
        numbers_hand2 = [6,6,6,6,3]
        result = four_of_a_kind_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,2)

    def test_high_card_tie_breaker1(self): #player 1 has better high card
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [2,4,6,8,10]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_high_card_tie_breaker2(self): #player 1 has better second highest card
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [2,4,6,8,11]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_high_card_tie_breaker3(self): #player 1 has better third highest card
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [2,4,6,9,11]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_high_card_tie_breaker4(self): #player 1 has better fourth highest card
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [2,4,7,9,11]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_high_card_tie_breaker5(self): #player 1 has better fifth highest card
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [2,5,7,9,11]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,1)

    def test_high_card_tie_breaker6(self): #player 2 has better high card
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [4,6,8,10,12]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,2)

    def test_high_card_tie_breaker7(self): #tie
        numbers_hand1 = [3,5,7,9,11]
        numbers_hand2 = [3,5,7,9,11]
        result = high_card_tie(numbers_hand1,numbers_hand2)
        self.assertEqual(result,3)

    def test_three_of_a_kind_tie_breaker1(self):
        numbers_hand1 = [3, 3, 3, 6, 7]
        numbers_hand2 = [2, 2, 2, 4, 5]
        result = three_of_a_kind_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_three_of_a_kind_tie_breaker2(self):
        numbers_hand1 = [2, 2, 2, 7, 8]
        numbers_hand2 = [6, 6, 6, 4, 3]
        result = three_of_a_kind_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_two_pair_tie_breaker1(self): #player 1 high pair wins
        numbers_hand1 = [2, 3, 3, 7, 7]
        numbers_hand2 = [2, 4, 4, 6, 6]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_two_pair_tie_breaker2(self): #player 1 low pair wins
        numbers_hand1 = [2, 6, 6, 7, 7]
        numbers_hand2 = [2, 5, 5, 7, 7]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_two_pair_tie_breaker3(self): #player 1 kicker wins
        numbers_hand1 = [3, 6, 6, 7, 7]
        numbers_hand2 = [2, 6, 6, 7, 7]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_two_pair_tie_breaker4(self): #player 2 high pair wins
        numbers_hand1 = [2, 3, 3, 7, 7]
        numbers_hand2 = [2, 4, 4, 8, 8]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_two_pair_tie_breaker5(self): #player 2 low pair wins
        numbers_hand1 = [2, 4, 4, 8, 8]
        numbers_hand2 = [3, 6, 6, 8, 8]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_two_pair_tie_breaker6(self): #player 2 kicker
        numbers_hand1 = [2, 5, 5, 7, 7]
        numbers_hand2 = [4, 5, 5, 7, 7]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_two_pair_tie_breaker7(self): #tie
        numbers_hand1 = [3, 6, 6, 8, 8]
        numbers_hand2 = [3, 6, 6, 8, 8]
        result = two_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 3)

    def test_one_pair_tie_breaker1(self): #player 1 pair wins
        numbers_hand1 = [3, 5, 6, 8, 8]
        numbers_hand2 = [3, 5, 6, 7, 7]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_one_pair_tie_breaker2(self): #player 1 kicker wins
        numbers_hand1 = [3, 5, 7, 8, 8]
        numbers_hand2 = [3, 5, 6, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_one_pair_tie_breaker3(self): #player 1 kicker2 wins
        numbers_hand1 = [3, 6, 7, 8, 8]
        numbers_hand2 = [3, 5, 7, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_one_pair_tie_breaker4(self): #player 1 kicker 3 wins
        numbers_hand1 = [3, 5, 6, 8, 8]
        numbers_hand2 = [2, 5, 6, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 1)

    def test_one_pair_tie_breaker5(self): #player 2 pair wins
        numbers_hand1 = [3, 5, 6, 8, 8]
        numbers_hand2 = [3, 5, 6, 9, 9]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_one_pair_tie_breaker6(self): #player 2 kicker wins
        numbers_hand1 = [3, 5, 6, 8, 8]
        numbers_hand2 = [3, 5, 7, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_one_pair_tie_breaker7(self): #player 2 kicker2 wins
        numbers_hand1 = [3, 4, 7, 8, 8]
        numbers_hand2 = [3, 5, 7, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_one_pair_tie_breaker8(self): #player 2 kicker 3 wins
        numbers_hand1 = [3, 5, 6, 8, 8]
        numbers_hand2 = [4, 5, 6, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 2)

    def test_one_pair_tie_breaker8(self): #tie
        numbers_hand1 = [4, 5, 6, 8, 8]
        numbers_hand2 = [4, 5, 6, 8, 8]
        result = one_pair_tie(numbers_hand1, numbers_hand2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()