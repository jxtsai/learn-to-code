# Top-down apprach to design BlackJack
### prototype version
Rules: 
  1.  A = 1 or 11, JQK = 10
  2.  closet to 21 as much as possible
  3.  21>= player or dealer
  4.  player busts or dealer bust    
  5.  dealer >= 17 (A == 11) or (A = 1)

expect outcome for this program => return the probability of dealer busts(dealer_bust(player, dealer))
player = sum([]) 
21>= dealer >=17 = sum([])
cards = [A, A, A, A, 2,2,2,2,3,3,3,3,3...... 10,10] (len(cards) == 52)
player= (random.choices(cards, k = 2)
dealer = (random.choices(cards, k = 2) 

def Check_ace(actor):
    return  "A" in actor

if Check_ace(dealer)  
(A)in the condition of True : (1) blackjack, (2) AA  busts (3) 9,8,7,6 A = 11 (4) 2~5, A = 1 (call another card)
(B) in the condition of False : (1) 20 >= dealer >= 17, 比大小 (2) dealer < 17( call another card) 

input ??  
