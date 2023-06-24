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
while True:
    print("select operation 1.push 2.pop 3.quit 4.top 5.display")
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
    else:
        print("enter the correct operation")
        