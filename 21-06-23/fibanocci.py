#CREATING NODE-DECLARATION AND DEFINITION
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):#iteration 1 happen
            temp=temp.next
        np.next=temp.next
        temp.next=np
    
    def display(self):
        if self.head==None:
            print('linked list is empty')
        else:
            temp=self.head#temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=' ')
                #temp.data means first node's data
                else:
                    temp=temp.next#establishing link
obj=singlelinkedlist()
#node creation- initialising
n=Node(10)#so n.data in node class will be 10
obj.head=n#assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
print()
obj.insert_position(3,1000)
obj.display