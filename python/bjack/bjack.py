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
    card = random.choice(deck)
    print(card)
    turn.append(card)
    deck.remove(card)
    
def caculate(hand):
    '''
    function parameter is a list of cards
    '''
    faces = ["J","Q","K"]
    total = 0
    for c in hand:
        if c in faces:
            total = total + 10
        else :
            total = total + c
        # elif c == "A" and total <= 17:
        #    total = total + 11
    if total > 21:
       play = "q"
       return "Busts!"
    else:
        return total
 
def winner():
    if caculate(playerhand) >= caculate(dealerhand):
        return "You win!"
    else:
        return "You lost!"

play = input("Add card, please type 'a', to quit this game, type 'q' !")

while play != "q":
    #print(playerhand)
    #print(dealerhand)
    dealCard(playerhand)
    dealCard(dealerhand)
    print(playerhand, dealerhand)
    print(f"player hand are : {caculate(playerhand)}")
    print(f"dealer's hand are : {caculate(dealerhand)}")
    print(winner())
    break
    
