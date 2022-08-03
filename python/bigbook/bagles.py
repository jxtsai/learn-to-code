    import random

def threes():
    # a function to return 3 non-repeated digits
    numbers= []
    for i in range(10):
        numbers.append(str(i))
    t = True
    while t:
       n3 = random.choices( numbers, k=3)
       if n3[0] != n3[1] and n3[0] !=n3[2] and n3[1] != n3[2]:
           t = False 
    return n3        

answer = threes()

guess = 10
def begals():
    return user[0] not in answer and user[1] not in answer and user[2] not in answer
     
print("I have thought up a number. \n")
print("You have 10 guesses to get it.\n")
print(f"Guess #{guess}: ")

while guess >= 1:
    checkuser = False
    while not checkuser :
        user = list(input(">"))
        if len(user) == 3:
            checkuser = True
        else:
            print("3 non repeated number")
            
    if answer == user:
        print("You get it!")
        break
    elif begals(): 
        print("Bagels")     
    else :     
       for i in range(len(user)):
           if user[i] == answer[i]:
               print("Fermin")     
           elif user[i] in answer:
               print("Pico")
    guess = guess - 1   
    print(f"You have {guess} change to try")
