
# coding: utf-8

############ **************** POKER MADE SIMPLE **************** ############

"""This program is a simplified version of a Poker game to be played between two opponents.
Each person is granted two random cards from a standard card deck of 52 cards.

A 'flop' of 3 cards, face up, is presented that is shared between the two players. The two 
players have the option of creating a combination from two cards that are given to them and
the three shared cards. The one with higher ranking combo wins the game."""

import random as rd

class Card:
    """Contains individual cards"""
    
    def __init__(self, value = None, suit = None):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit)

class Deck:
    """Contains complete playing deck
       52 Cards (4 suits, 13 ranks, Ace High Only)"""
    
    cards = []
    cut_deck = []
    suits = ['Hearts','Spades','Clubs','Diamonds']
    
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for value in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
                self.cards.append(Card(value, suit))
            
    def shuffle(self):
        """Returns deck of cards after randomised shuffling"""            
        return rd.shuffle(self.cards)
        
    def cut(self): 
        """Returns shuffled deck split at index 26 and then cards given to players from 
        second half of the deck - index 26 onwards"""   
        self.cut_deck = self.cards[26:]
        return self.cut_deck
        
class Player:
    """Contains Player objects with dealt cards and complete hand"""

    player_dealt = [] # the 2 cards that are dealt from cut deck
    player_hand = [] # the complete hand, 2 cards + 3 flop cards
    
    def __init__(self, deck, index):
        """Two cards are given to Player along with flop"""
        
        self.player_dealt = []
        self.player_dealt = deck.cut()[index[0]:index[1]]
        self.player_hand = self.player_dealt + deck.cut()[0:3]

def hands(player_object):
    """This will check player hands against rankings"""    
    
    p_values = [] # the values will be separated from player hand
    p_suits = [] # the suits will be separated from player hand
    
    for card in player_object.player_hand:
        p_values.append(card.value)
        p_suits.append(card.suit)
            
    def ranks(pv,ps):
        
        def royal(pv,ps):
            """Returns 10 if player hand is royal flush
            False if not"""
            count = 0
            for value in pv:
                if value >= 10:
                    count += 1
            if count == 5 and len(set(ps)) == 1:
                return 10
            return False
        
        def sflush(pv,ps):
            """Returns 9 if player hand is straight flush
            False if not"""
            count = 0
            sorted_pv = sorted(pv)
            if len(set(ps)) == 1: # all cards have same suits
                for i in range(len(pv)-1):
                    if sorted_pv[i+1] - sorted_pv[i] == 1: # all cards are sequential
                        count += 1
                if count == 4:
                    return 9
            return False
            
        def four(pv, ps):
            """Returns 8 if player has four of a kind
            False if not"""
            count = {}
            
            for value in pv:
                if value not in count:
                    count[value] = 1
                else:
                    count[value] += 1
                    
            if 4 in count.values(): # if any value is appearing 4 times
                return 8
            return False
        
        def fullhouse(pv, ps):
            """Returns 7 if player has full house
            False if not"""
            count = {}
            for value in pv:
                if value not in count:
                    count[value] = 1
                else: 
                    count[value] += 1
                    
            if len(count.values()) == 2: 
                return 7
            return False
        
        def flush(pv, ps):
            """Returns 6 if player hand is flush
            False if not"""
            if len(set(ps)) == 1:
                return 6
            return False
        
        def straight(pv,ps):
            """Returns 5 if player has straight
            False if not"""
            count = 0
            sorted_pv = sorted(pv)
            if len(set(ps)) > 1:
                for i in range(len(pv)-1):
                    if sorted_pv[i+1] - sorted_pv[i] == 1:
                        count += 1
            if count == 4:
                return 5
            return False
        
        def three(pv,ps):
            """Returns 4 if player has three of a kind
            False if not"""
            count = {}
            for value in pv:
                if value not in count:
                    count[value] = 1
                else:
                    count[value] += 1
                    
            if 3 in count.values():
                return 4
            return False
        
        def twopair(pv, ps):
            """Returns 3 if player has a two pair
            False if not"""
            count = {}
            for value in pv:
                if value not in count:
                    count[value] = 1
                else:
                    count[value] += 1
            if list(count.values()).count(2) == 2:
                return 3
            return False
        
        def pair(pv, ps):
            """Returns 2 if player has a pair
            False if not"""
            count = {}
            for value in pv:
                if value not in count:
                    count[value] = 1
                else:
                    count[value] += 1
            if list(count.values()).count(2) == 1:
                return 2
            return False
        
        rankings = [royal, sflush, four, fullhouse, flush, straight, three, twopair, pair]
        
        for x in rankings:
            if x(pv,ps) is not False:
                return (x(pv,ps))
        else:
            return 1
        
    Player_rank = ranks(p_values, p_suits)
    return Player_rank


def unequal_comparison(p1_rank, p2_rank):
    """This returns who has higher ranked hand for unequal cases"""
    
    display = {10: "Royal flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Fullhouse", 6: "Flush", 5: "Straight", 4: "Three of a kind", 3: "Two Pair", 2: "One Pair", 1: "High Card"}
    
    print("Player 1 has {}".format(display[p1_rank]))
    print("Player 2 has {}".format(display[p2_rank]))
    
    if p1_rank > p2_rank:
        print("Player 1 wins the hand.")
        return 1
    else:
        print("Player 2 wins the hand.")
        return 2

def equal_comparison(p1_rank, p2_rank, Player1_object, Player2_object):
    
    P1_High = high_check(Player1_object)
    P2_High = high_check(Player2_object)
    
    if p1_rank == 1:
        print("Both players have high card.")
        if P1_High > P2_High:
            print("Player 1 has higher card with value: ", P1_High)
            return 1, None
        elif P2_High > P1_High:
            print("Player 2 has higher card with value:", P2_High)
            return 2, None
        else:
            print("Both players have same highest ranked card", P1_High)
            return 0, None
            
    elif p1_rank == 2:
        print("Both players have a one pair.")
        
        P1_High = onepair_check(Player1_object)
        P2_High = onepair_check(Player2_object)
        
        if P1_High > P2_High:
            print("Player 1 has higher one pair with value:", P1_High)
            return 1, None
        elif P2_High > P1_High:
            print("Player 2 has higher one pair with value:", P2_High)
            return 2, None
        else:
            print("Both players have same high value pair: ", P1_High) 
            return 0, None

    elif p1_rank == 3:
        print("Both players have a two pair.")
        
        P1_High = twopair_check(Player1_object)
        P2_High = twopair_check(Player2_object)
        
        if P1_High > P2_High:
            print("Player 1 has higher two pair with value:", P1_High)
            return 1, None
        elif P2_High > P1_High:
            print("Player 2 has higher two pair with value:", P2_High)
            return 2, None
        else:
            print("Both players have same highest value two pair: ", P1_High)
            return 0, None
            
    elif p1_rank == 4:
        print("Both players have three of a kind.")
        
        P1_High = three_check(Player1_object)
        P2_High = three_check(Player2_object)
        
        if P1_High > P2_High:
            print("Player 1 has higher three of a kind with value:", P1_High)
            return 1, None
        elif P2_High > P1_High:
            print("Player 2 has higher three of a kind with value:", P2_High)
            return 2, None
        else:
            print("Both players have same three of a kind with high", P1_High)
            return 0, None
        
    elif p1_rank == 8:
        print("Both players have four of a kind.")
        
        P1_High = four_check(Player1_object)
        P2_High = four_check(Player2_object)
        
        if P1_High > P2_High:
            print("Player 1 has higher four of a kind:", P1_High)
            return 1, None
        elif P2_High > P1_High:
            print("Player 2 has higher four of a kind:", P2_High)
            return 2, None
        else:
            print("Both players have same four of a kind", P1_High)
            return 0, None
    else:
        return "Both have same high rank combo which can't be compared by high card-low card", "Hand is tied"
            
def high_check(Player_object):
    high_value = []
    for card in Player_object.player_hand:
        high_value.append(card.value)
    return max(high_value)

def onepair_check(Player_object):
    d = {}
    for card in Player_object.player_hand:
        if card.value not in d:
            d[card.value] = 1
        else:
            d[card.value] += 1
    for k,v in d.items():
        if v == 2:
            return k
        
def twopair_check(Player_object):
    d = {}
    keys = []
    
    for card in Player_object.player_hand:
        if card.value not in d:
            d[card.value] = 1
        else:
            d[card.value] += 1
            
    for k,v in d.items():
        if v == 2:
            keys.append(k)
    return max(keys)

def three_check(Player_object):
    d = {}
    
    for card in Player_object.player_hand:
        if card.value not in d:
            d[card.value] = 1
        else:
            d[card.value] += 1
            
    for k,v in d.items():
        if v == 3:
            return k
        
def four_check(Player_object):
    d = {}
    for card in Player_object.player_hand:
        if card.value not in d:
            d[card.value] = 1
        else:
            d[card.value] += 1
    for k,v in d.items():
        if v == 4:
            return k

play = input("WELCOME TO POKER MADE SIMPLE.\nTwo Players are involved in this game, "
             "dealt 2 distinct cards and 3 common cards.\nPress 'Y' to Play: ")

p1bet_amount = 0 # amount won by player 1
p2bet_amount = 0 # amount won by player 2

p1wins = 0 # tallying player 1 wins
p2wins = 0 # tallying player 2 wins

index_1 = [3,5] # random indexes for player 1 cards
index_2 = [13,15] # random indexes for player 2 cards

while play == 'Y' or play == 'y':

    try:
        bet = int(input("Enter bet money: $"))
    except:
        print("Please enter a number as bet money")
        continue
    
    a = Deck()
    a.shuffle() # shuffling the deck every hand
    a.cut() # cutting the deck every hand
    p1 = Player(a, index_1) # creating player 1 object
    p2 = Player(a, index_2) # creating player 2 object
    
    print("\nPlayer 1, your hand is", p1.player_hand[0:2], "+ flop: ", p1.player_hand[2:])
    print("Player 2, your hand is: ", p2.player_hand[0:2], "+ flop: ", p2.player_hand[2:], '\n')
    
    P1_rank = hands(p1)
    P2_rank = hands(p2)
    
    if P1_rank != P2_rank:
        x = unequal_comparison(P1_rank, P2_rank)
        if x == 1:
            print("${} goes to Player 1".format(bet))
            p1wins += 1
            p1bet_amount += bet
        elif x == 2:
            print("${} goes to Player 2".format(bet))
            p2wins += 1
            p2bet_amount += bet
        else:
            pass
        
    elif P1_rank == P2_rank:
        a, b = equal_comparison(P1_rank, P2_rank, p1, p2)
        if a == 1:
            print("${} goes to Player 1".format(bet))
            p1wins += 1
            p1bet_amount += bet
        elif a == 2:
            print("${} goes to Player 2".format(bet))
            p2wins += 1
            p2bet_amount += bet
        else:
            pass
        
    play = input("\nPress 'Y' to continue playing OR enter any other key to quit: ")

print("\nExiting game.\nPlayer 1 won {} hands.\nPlayer 2 won {} hands.\nPlayer 1 won ${}.\nPlayer 2 won ${}."        .format(p1wins, p2wins, p1bet_amount, p2bet_amount))

