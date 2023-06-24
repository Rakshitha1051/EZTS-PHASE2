class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inOrder(root):
    current=root
    stack=[]
    done=0
    while True:
        #Reach the left most Node of the current
        if current is not None:
    #place pointer to a tree node on the stack
            stack.append(current)
            current=current.left
        elif(stack):
            current=stack.pop()
            print(current.data,end=" ")
            
            current=current.right
        else:
            break
    print()
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
inOrder(root)