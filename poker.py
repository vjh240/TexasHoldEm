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
    all_cards = hand | community_cards
    hands = combinations(all_cards, 5)
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
    if rank == 0:
        return high_card_tie(numbers_hand1,numbers_hand2)
    elif rank == 1:
        return one_pair_tie(numbers_hand1,numbers_hand2)
    elif rank == 2:
        return two_pair_tie(numbers_hand1,numbers_hand2)
    elif rank == 3:
        return three_of_a_kind_tie(numbers_hand1,numbers_hand2)
    elif rank == 4:
        return straight_tie(numbers_hand1,numbers_hand2)
    elif rank == 5:
        return high_card_tie(numbers_hand1,numbers_hand2)
    elif rank == 6:
        return full_house_tie(numbers_hand1,numbers_hand2)
    elif rank == 7:
        return four_of_a_kind_tie(numbers_hand1,numbers_hand2)
    elif rank == 8:
        return straight_tie(numbers_hand1,numbers_hand2)
    else:
        print ("ERROR")

def straight_tie(numbers_hand1,numbers_hand2):
    if numbers_hand1[4]>numbers_hand2[4]:
        return 1
    elif numbers_hand1[4]<numbers_hand2[4]:
        return 2
    else:
        return 3

def full_house_tie(numbers_hand1,numbers_hand2): #gotta add pair comparison
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

def four_of_a_kind_tie(numbers_hand1,numbers_hand2): #gotta add kickers
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

def three_of_a_kind_tie(numbers_hand1,numbers_hand2): #gotta add kickers
    frequency1 = [numbers_hand1.count(card) for card in numbers_hand1]
    frequency2 = [numbers_hand2.count(card) for card in numbers_hand2]
    triple1 = numbers_hand1[frequency1.index(3)]
    triple2 = numbers_hand2[frequency2.index(3)]
    if triple1 > triple2:
        return 1
    elif triple2 > triple1:
        return 2

def two_pair_tie(numbers_hand1,numbers_hand2):
    numbers_hand1.sort(reverse=True)
    numbers_hand2.sort(reverse=True)
    frequency1 = [numbers_hand1.count(card) for card in numbers_hand1]
    frequency2 = [numbers_hand2.count(card) for card in numbers_hand2]
    pair1_hand1 = numbers_hand1[frequency1.index(2)]
    pair1_hand2 = numbers_hand2[frequency2.index(2)]
    if pair1_hand1 > pair1_hand2:
        return 1
    elif pair1_hand2 > pair1_hand1:
        return 2
    look_for_next_pair1 = frequency1.index(2) + 2
    look_for_next_pair2 = frequency2.index(2) + 2
    pair2_hand1 = numbers_hand1[frequency1.index(2,look_for_next_pair1)]
    pair2_hand2 = numbers_hand2[frequency2.index(2,look_for_next_pair2)]
    if pair2_hand1 > pair2_hand2:
        return 1
    elif pair2_hand2 > pair2_hand1:
        return 2
    kicker_hand1 = numbers_hand1[frequency1.index(1)]
    kicker_hand2 = numbers_hand2[frequency2.index(1)]
    if kicker_hand1 > kicker_hand2:
        return 1
    elif kicker_hand2 > kicker_hand1:
        return 2
    return 3

def one_pair_tie(numbers_hand1,numbers_hand2):
    numbers_hand1.sort(reverse=True)
    numbers_hand2.sort(reverse=True)
    frequency1 = [numbers_hand1.count(card) for card in numbers_hand1]
    frequency2 = [numbers_hand2.count(card) for card in numbers_hand2]
    pair_hand1 = numbers_hand1[frequency1.index(2)]
    pair_hand2 = numbers_hand2[frequency2.index(2)]
    if pair_hand1 > pair_hand2:
        return 1
    elif pair_hand2 > pair_hand1:
        return 2
    kicker1_hand1 = numbers_hand1[frequency1.index(1)]
    kicker1_hand2 = numbers_hand2[frequency2.index(1)]
    if kicker1_hand1 > kicker1_hand2:
        return 1
    elif kicker1_hand2 > kicker1_hand1:
        return 2
    look_for_second_kicker1 = frequency1.index(1) + 1
    look_for_second_kicker2 = frequency2.index(1) + 1
    kicker2_hand1 = numbers_hand1[frequency1.index(1,look_for_second_kicker1)]
    kicker2_hand2 = numbers_hand2[frequency2.index(1,look_for_second_kicker2)]
    if kicker2_hand1 > kicker2_hand2:
        return 1
    elif kicker2_hand2 > kicker2_hand1:
        return 2
    look_for_third_kicker1 = frequency1.index(1,look_for_second_kicker1) + 1
    look_for_third_kicker2 = frequency2.index(1,look_for_second_kicker2) + 1
    kicker3_hand1 = numbers_hand1[frequency1.index(1, look_for_third_kicker1)]
    kicker3_hand2 = numbers_hand2[frequency2.index(1, look_for_third_kicker2)]
    if kicker3_hand1 > kicker3_hand2:
        return 1
    elif kicker3_hand2 > kicker3_hand1:
        return 2
    return 3

deck = FULL_DECK.copy()
hand, deck = deal_hand(deck)
community_cards, deck = deal_community_cards(deck)
rank_player_hand, player_hand = rank(hand,community_cards)
print("You were dealt a " + str(hand))
print(community_cards)
print("You have " + str(RANKED_HANDS[rank_player_hand]) + " with the cards " + str(player_hand))

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
        player_hand_vs_hidden_hand_result = tie_breaker(player_hand,hidden_hand,rank_player_hand)
        if player_hand_vs_hidden_hand_result == 1:
            win +=1
        elif player_hand_vs_hidden_hand_result == 2:
            loss += 1
        else:
            tie += 1
    else:
        win += 1

print("Outcome Probability:")
print("Win:  " + '{0:.4%}'.format(win/len(hidden_hands)))
print("Tie:  " + '{0:.4%}'.format(tie/len(hidden_hands)))
print("Loss: " + '{0:.4%}'.format(loss/len(hidden_hands)))


# a possible opportunity to remove iterations:
# if the players best hand is the river, they will tie with all other hand possibilities in which the river is their best hand