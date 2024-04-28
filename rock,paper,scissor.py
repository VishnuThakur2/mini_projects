#rock paper scissor
import random as r
v=r.choice(['rock','scissor','paper'])
y=input("choice only one 'rock,paper,scissor':")
if(y=='rock'):
    if(v=='rock'):
        print("match draw")
    elif(v=='paper'):
        print("computer wins")
    elif(v=='scisor'):
        print("you win")
if(y=='scissor'):
    if(v=='scisor'):
        print("match draw")
    elif(v=='rock'):
        print("computer wins")
    elif(v=='paper'):
        print("you wins")
if(y=='paper'):
    if(v=='paper'):
        print("match draw")
    elif(v=='rock'):
        print("we loose")
    elif(v=='scissor'):
        print("we win")
    else:
        print("nobody wins")
    