import random

cards =[11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]


class Player():
    # 二張卡
    def __init__(self):
        self.scores = 12
    def deal(self):
        self.card = random.choice(cards)
        cards.pop(self.card)
        print(self.card)
        return self.card
    def stand(self):    
        pass
    def total(self):
        self.scores = self.scores + self.deal()
        return self.scores
    

player1 = Player()
host = Player()



print(player1.total())
print(len(cards))