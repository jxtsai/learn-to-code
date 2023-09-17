'''
### deck of card, player hand, dealer hand

deck = []
playerhand = []
dealerhand = []


### dealCard(turn)



### caculating cards


### win or lose ?



### game loop


'''
import random

deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        "J","Q","K","A","J","Q","K","A", "J","Q","K","A", "J","Q","K","A",  ]
playerhand = []
dealerhand = []

def dealCard(turn):
    pick = random.choice(deck)
    turn.append(pick)
    deck.remove(pick)

def caculate(hand):
    '''
    function parameter is a list of cardhand
    '''
    if 
