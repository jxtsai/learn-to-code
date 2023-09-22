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

def reset(p):
    '''
    重洗牌歸零
    參數為遊戲者之列表 : playerhand or dealerhand
    
    '''
    pass
    

def dealCard(turn):
    '''
    參數為玩家, 發"一張"牌
    '''
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
    
def caculate(hand):
    '''
    function parameter is a list of cards
    計算手上的牌總和
    '''
    faces = ["J","Q","K", "A"]
    total = 0
    for c in hand:
        if c in faces and c == "A":
            if total <= 10:
                total = total + 11
            else:
                total = total + 1
                
        elif c in faces:
            total = total + 10
        else :
            total = total + c
    return total    
    
 
def winner():
    '''
    判別本場遊戲的獲勝者
    '''
    
    if caculate(playerhand) < 17:
        player = input("Play this game, please type 'p'. To quit this game, type 'q' ! ")
        return 
    elif caculate(playerhand) >= caculate(dealerhand):
        return "You win!"
    else:
        return "You lost!"



def unveil():
    pass
    
def game():
    print("Welcome Black-Jack ! Exit this game, type 'q'. ")
    
    for i in range(2):
        dealCard(playerhand)
        dealCard(dealerhand)
    
    print(f" Your cards: {playerhand}, for {caculate(playerhand)}") 
    print(f" Dealer : {dealerhand[0]}.")
    play = input("Hit ('h') to add card,  Stand ('s') or Quit ('q')" ) 
     
    if play == 's':
        while caculate(dealerhand) < 17:
            dealCard(dealerhand)
    elif play == 'h':
            dealCard(playerhand)
            if caculate(playerhand) < 17:
                play = input("Hit ('h') to add card or Stand ('s')? " )   
        
    print(f" Your cards: {playerhand}, for {caculate(playerhand)}")     
    print(f" Dealer : {dealerhand}.") 
    
    
game()
    
 
