import math
def sum():
    x1=int(input("enter value of x: "))
    y1=int(input("enter value of y: "))
    sum =x1+y1
    return sum
def sub():
    x1=int(input("enter value of x: "))
    y1=int(input("enter value of y: "))
    sub =x1-y1
    return sub
def mul():
    x1=int(input("enter value of x: "))
    y1=int(input("enter value of y: "))
    mul =x1*y1
    return mul
def div():
    x1=int(input("enter value of x: "))
    y1=int(input("enter value of y: "))
    div =x1/y1
    return div
def sqrt():
    x1=int(input("enter value of x: "))
    sqrt =math.sqrt(x1)
    return sqrt
def pow():
    x1=int(input("enter value of x: "))
    y1=int(input("enter value of y: "))
    pow =x1**y1
    return pow
def log():
    x1=int(input("enter value of x: "))
    log =math.log(x1)
    return log
def sin():
    x1=int(input("enter the value of x: "))
    sin =math.sin(x1)
    return sin
def cos():
    x1=int(input("enter the value x: "))
    cos =math.cos(x11)
    return cos
def tan():
    x1=int(input("enter the value x: "))
    tan =math.tan(x1)
    return tan
def exp():
    x1=int(input("enter the value x: "))
    exp =math.exp(x1)
    return exp
def fact():
    x1=int(input("enter the value x: "))
    fact =math.factorial(x1)
    return fact
def mod():
    x1=int(input("enter the value x: "))
    y1=int(input("enter the value y: "))
    mod =x1%y1
    return mod
def sqr():
    x1=int(input("enter the value x: "))
    sqr =x1**2
    return sqr
def cube():
    x1=int(input("enter the value x: "))
    cube =x1**3
    return cube
while True:
    choice=int(input("enter your choice 1->sum 2->sub 3->div 4->mul 5->sqrt 6->pow 7->pow 8->log 9->sin 10->cos 11->tan 12->exp 13->fact 14->mod 15->sqr 16->cube 17->exit:"))
    if choice==1:
       print(sum())
    elif choice==2:
       print(sub())
    elif choice==3:
        print(div())
    elif choice==4:
        print(mul())
    elif choice==5:
        print(sqrt())
    elif choice==6:
        print(pow())
    elif choice==7:
        print(log())
    elif choice==8:
        print(sin())
    elif choice==9:
        print(cos())
    elif choice==10:
        print(tan())
    elif choice==11:
        print(exp())
    elif choice==12:
        print(fact())
    elif choice==13:
        print(mod())
    elif choice==14:
        print(sqr())
    elif choice==15:
        print(cube())
    elif choice==16:
        break
    else:
        print("Invalid choice")