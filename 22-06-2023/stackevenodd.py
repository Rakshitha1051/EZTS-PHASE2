stack=[]
def push():
    element=int(input("enter the element you want to push:"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
def top():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("the peek element is:",stack[-1])
def display():
    if len(stack)==0:
        print("stack is empty")
        return
    print("the stack is:",stack)
def evenodd():
    print("even elements")
    for i in stack:
        if i%2==0:
            print(i,end=" ")
    print("odd elements")
    print()
    for i in stack:
        if i%2==1:
            print(i,end=" ")
    print()
while True:
    print("select operation 1.push 2.pop 3.quit 4.top 5.display 6.evenodd" )
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    elif choice==4:
        top()
    elif choice==5:
        display()
    elif choice==6:
        evenodd()
    else:
        print("enter the correct operation")
        
