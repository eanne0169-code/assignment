

x=int(input("Enter your first number:"))
y=int(input("Enter your second number:"))
z=input("Enter a function(+,-,*,/):")

def add(x,y):
    print(x + y)    
    
def sub(x,y):
    print(x - y)
    
def mul(x,y):
    print(x * y)

def div(x,y):
    print(x / y)

if z == "+" :
    add(x,y)
    
elif z== "*":
    mul(x,y)
    
    
elif z== "-" :
    if x < y:
       print("Underfied")
    else:
     sub(x,y)

elif z== "/":
    if x < y:
        print("Underfied")
    else:
     div(x,y)        
     

    