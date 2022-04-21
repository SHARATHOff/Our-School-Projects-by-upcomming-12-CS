import turtle
turtle.Turtle()
def A(a,b):
    print(a+b)
def B():
    global a
    a += 10
    print(a)
def C(a = 10,b=20,c=30):
    print(a+b+c)
def D():
    a = 10
    for i in range(1,a):
        print("*"*i,end='')
        print('**'*i,"*",end='')
        print()
    for j in range(a,-1,-1):
        print("*"*i,end='')
        print('**'*j,"*",end='')
        print()
def circle():
    while True:
        a = 1
        turtle.left(a)
        turtle.forward(a)
        a+=1
def box():
    turtle.speed(1000)    
    while True:
        turtle.speed(1000)
        a = 100
        turtle.bgcolor('black')
        turtle.forward(a)
        turtle.color('red')
        turtle.left(a)
        turtle.forward(a)
        turtle.left(a)
        turtle.forward(a)
        turtle.left(a)
        turtle.forward(a)
        
circle()
