#roll the  dice
import random as r
i=1
v1=v2=0
while(i<7):
    c=r.randint(1,6)
    y=int(input("enter the number between 1to 6: "))
    choice=input("if you quite type'stop' otherwise type 'no' : ")
    v1+=c
    v2+=y
    if(choice=='stop'):
        break
    elif(choice=='no'):
        continue
    else:
        print("wrong choice")
        break
        
print("\n")
print("your score is:",v2)
print("the computer score is:",v1)
print("\n")
if(v1>v2):
    print("computer won with score of:",v1)
else:
    print("you won with the score of:",v2)
