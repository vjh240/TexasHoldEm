import random
from itertools import combinations
import time

FULL_DECK = set(["2h","3h","4h","5h","6h","7h","8h","9h","10h","11h","12h","13h","14h","2c","3c","4c","5c","6c","7c","8c","9c","10c","11c","12c","13c","14c","2s","3s","4s","5s","6s","7s","8s","9s","10s","11s","12s","13s","14s","2d","3d","4d","5d","6d","7d","8d","9d","10d","11d","12d","13d","14d"])
RANKED_HANDS = ["a High Card","One Pair","Two Pair","Three of a Kind","a Straight","a Flush","a Full House","Four of a Kind","a Straight Flush"]

def deal_hand(deck):
  hand = set(random.sample(deck,2))
  deck = deck - hand
  return hand, deck

def deal_community_cards(deck):
    community_cards = set(random.sample(deck,5))
    deck = deck - community_cards
    return community_cards, deck

def hand_strength(hand):
    has_ace = False
    suits = [s[-1:] for s in hand]
    numbers = [int(n[:len(n)-1]) for n in hand]
    numbers.sort()
    num_of_aces = numbers.count(14)
    all_one_suit = len(set(suits)) == 1
    if num_of_aces >= 1:
        has_ace = True
    if all_one_suit:
        #you do not need to check for full house or four of a kind since we know all the cards are one suit (all numbers must be different)
        is_straight = int(numbers[4]) - int(numbers[0]) == 4
        if is_straight:
            return 8 #straight flush
        else:
            if has_ace:
                numbers[numbers.index(14)] = 1
                numbers.sort()
                is_straight = int(numbers[4]) - int(numbers[0]) == 4
                if is_straight:
                    return 8 #straight flush
                else:
                    return 5 #flush
            return 5 #flush
    x = len(set(numbers))
    if x == 4:
        return 1 #One Pair
    elif x == 3:
        number_frequencies = [numbers.count(c) for c in numbers]
        if number_frequencies.count(3): #if a frequency of 3 is found then the hand is a three of a kind
            return 3 #Three of a Kind
        return 2 #Two Pair
    elif x == 2:
        if numbers.count(numbers[0]) == 1 or numbers.count(numbers[0]) == 4:
            return 7 #four of a kind
        return 6  # Full house
    else:
        is_straight = int(numbers[4]) - int(numbers[0]) == 4
        if is_straight:
            return 4  # straight flush
        if has_ace:
            numbers[numbers.index(14)] = 1
            numbers.sort()
            is_straight = int(numbers[4]) - int(numbers[0]) == 4
            if is_straight:
                return 4  # straight
            else:
                return 0  # high card
        return 0 #high card
    return -1 #something went wrong if we got to this point

def rank(hand,community_cards):
    all_seven_cards = hand | community_cards
    hands = combinations(all_seven_cards, 5)
    max_rank = -1
    for h in hands:
        result = hand_strength(h)
        if result > max_rank:
            max_rank = result
            max_hand = h
        elif result == max_rank:
            best_hand = tie_breaker(h,max_hand,max_rank)
            if best_hand == 1:
                max_hand = h

    return max_rank, max_hand

def tie_breaker(hand1,hand2,rank):
    numbers_hand1 = [int(n[:len(n) - 1]) for n in hand1]
    numbers_hand1.sort()
    numbers_hand2 = [int(n[:len(n) - 1]) for n in hand2]
    numbers_hand2.sort()
    return 1
    # print(numbers_hand1)
    # print(numbers_hand2)
    # print(rank)
    # if rank == 0:
    #     high_card_tie(numbers_hand1,numbers_hand2)
    # elif rank == 1:
    #     one_pair_tie(numbers_hand1,numbers_hand2)
    # elif rank == 2:
    #     two_pair(numbers_hand1,numbers_hand2)
    # elif rank == 3:
    #     three_of_a_kind_tie(numbers_hand1,numbers_hand2)
    # elif rank == 4:
    #     straight_tie(numbers_hand1,numbers_hand2)
    # elif rank == 5:
    #     flush_tie(numbers_hand1,numbers_hand2)
    # elif rank == 6:
    #     full_house_tie(numbers_hand1,numbers_hand2)
    # elif rank == 7:
    #     four_of_a_kind_tie(numbers_hand1,numbers_hand2)
    # elif rank == 8:
    #     straight_tie(numbers_hand1,numbers_hand2)
    # else:
    #     print("Something went wrong")

# def straight_tie(numbers_hand1,numbers_hand2):
#     if numbers_hand1[4]>numbers_hand2[4]:
#         return 1
#     elif numbers_hand1[4]<numbers_hand2[4]:
#         return 2
#     else:
#         return 3

def unit_test_hands():
    # high card
    test_hand = ["2c", "4c", "6d", "8d", "10s"]
    if hand_strength(test_hand) != 0:
        print("High Card broken")

    # one pair
    test_hand = ["2c", "4c", "4c", "5d", "6c"]
    if hand_strength(test_hand) != 1:
        print("One Pair broken")

    # two pair
    test_hand = ["2c", "2d", "4c", "4d", "6c"]
    if hand_strength(test_hand) != 2:
        print("Two Pair broken")

    # three of a kind
    test_hand = ["2c", "4c", "4c", "4d", "6c"]
    if hand_strength(test_hand) != 3:
        print("Three of a Kind broken")

    # straight  a-5
    test_hand = ["14d", "2c", "3c", "4c", "5c"]
    if hand_strength(test_hand) != 4:
        print("Straight A-5 broken")

    # straight  10-a
    test_hand = ["14d", "10c", "11c", "12c", "13c"]
    if hand_strength(test_hand) != 4:
        print("Straight 10-A broken")

    # flush
    test_hand = ["2c", "10c", "11c", "12c", "13c"]
    if hand_strength(test_hand) != 5:
        print("Flush broken")

    # full house
    test_hand = ["14d", "14c", "14s", "12c", "12d"]
    if hand_strength(test_hand) != 6:
        print("Fullhouse broken")

    # four of a kind
    test_hand = ["14d", "14c", "14s", "14h", "13c"]
    if hand_strength(test_hand) != 7:
        print("Four of a Kind broken")

    # straight flush a-5
    test_hand = ["14c", "2c", "3c", "4c", "5c"]
    if hand_strength(test_hand) != 8:
        print("Straight Flush broken")

    # straight flush 10-a
    test_hand = ["14c", "10c", "11c", "12c", "13c"]
    if hand_strength(test_hand) != 8:
        print("Royal Flush broken")

deck = FULL_DECK.copy()
hand, deck = deal_hand(deck)
community_cards, deck = deal_community_cards(deck)
rank_player_hand, player_hand = rank(hand,community_cards)
print("You were dealt a " + str(hand))
print(community_cards)
print("You have " + str(RANKED_HANDS[rank_player_hand]))
print(player_hand)
hidden_hands = set(combinations(deck,2))
win = 0
loss = 0
tie = 0
for h in hidden_hands:
    h = set(h)
    rank_hidden_hand,hidden_hand = rank(h,community_cards)
    if rank_hidden_hand > rank_player_hand:
        loss += 1
    elif rank_hidden_hand == rank_player_hand:
        tie += 1
    else:
        win += 1

print("Wins: " + str(win))
print("Ties: " + str(tie))
print("Losses: " + str(loss))

unit_test_hands()


# a possible opportunity to remove iterations:
# if the players best hand is the river, they will tie with all other hand possiblilities in which the river is their best hand