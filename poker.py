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
    if rank == 4:
        return straight_tie(numbers_hand1,numbers_hand2)
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
    #     high_card_tie(numbers_hand1,numbers_hand2)
    # elif rank == 6:
    #     full_house_tie(numbers_hand1,numbers_hand2)
    # elif rank == 7:
    #     four_of_a_kind_tie(numbers_hand1,numbers_hand2)
    # elif rank == 8:
    #     straight_tie(numbers_hand1,numbers_hand2)
    # else:
    #     print("Something went wrong")

def straight_tie(numbers_hand1,numbers_hand2):
    if numbers_hand1[4]>numbers_hand2[4]:
        return 1
    elif numbers_hand1[4]<numbers_hand2[4]:
        return 2
    else:
        return 3

def full_house_tie(numbers_hand1,numbers_hand2):
    frequency_high1 = numbers_hand1.count(numbers_hand1[4])
    if frequency_high1 == 3:
        triple1 = numbers_hand1[4]
    else:
        triple1 = numbers_hand1[0]
    frequency_high2 = numbers_hand2.count(numbers_hand1[4])
    if frequency_high2 == 3:
        triple2 = numbers_hand2[4]
    else:
        triple2 = numbers_hand2[0]
    if triple1 > triple2:
        return 1
    else:
        return 2

def four_of_a_kind_tie(numbers_hand1,numbers_hand2):
    frequency_high1 = numbers_hand1.count(numbers_hand1[4])
    if frequency_high1 == 4:
        quad1 = numbers_hand1[4]
    else:
        quad1 = numbers_hand1[0]
    frequency_high2 = numbers_hand2.count(numbers_hand1[4])
    if frequency_high2 == 4:
        quad2 = numbers_hand2[4]
    else:
        quad2 = numbers_hand2[0]
    if quad1 > quad2:
        return 1
    else:
        return 2

def high_card_tie(numbers_hand1,numbers_hand2):
    numbers_hand1.sort(reverse=True)
    numbers_hand2.sort(reverse=True)
    for x in range(5):
        if numbers_hand1[x]>numbers_hand2[x]:
            return 1
        elif numbers_hand2[x]>numbers_hand1[x]:
            return 2
    return 3

deck = FULL_DECK.copy()
hand, deck = deal_hand(deck)
community_cards, deck = deal_community_cards(deck)
rank_player_hand, player_hand = rank(hand,community_cards)
print("You were dealt a " + str(hand))
print(community_cards)
print("You have " + str(RANKED_HANDS[rank_player_hand]))
print("best hand = " + str(player_hand))

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


# a possible opportunity to remove iterations:
# if the players best hand is the river, they will tie with all other hand possibilities in which the river is their best hand