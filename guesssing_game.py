#guessing number game
import random as r

b=int(input("enter the number "))
c=r.randrange(1,b)
d=int(input("enter the number "))
while(True):
    if(d==0):
        print("game over,player quite the game.")
        break
    elif(d==c):
        print("congratulation you are right. the random number was:",c)
        break
    elif(d<c):
        d=int(input("you are near to correct it play some more time"))
    elif(d>c):
        d=int(input("your guessing is around to corect.please play more time"))
    else:
        d=int(input("try again"))
        