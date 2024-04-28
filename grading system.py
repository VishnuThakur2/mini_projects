#grading system 
name=input("enter the name of student ")
v1=int(input("enter the first subject marks "))
v2=int(input("enter the second subject marks "))
v3=int(input("enter the marks of third subject "))
v4=int(input("enter the marks of forth subject "))
v5=int(input("enter the marks of fifth subject "))
t=v1+v2+v3+v4+v5
percentage=t/5
print("your percentage is:",percentage)
if(v1>100 or v2>100 or v3>100 or v4>100 or v5>100 or v1<0 or v2<0 or v3<0 or v4<0 or v5<0):
    print("enter the wrong marks criteria")
elif(percentage==100):
    print("grade==O")
elif(percentage>=90):
    print("grade==A+")
elif(percentage>=80):
    print("grade==B+")
elif(percentage>=70):
    print("grade==B")
elif(percentage>=60):
    print("grade==C")
elif(percentage>=50):
    print("grade==D")
else:
    print("the student is fail")

