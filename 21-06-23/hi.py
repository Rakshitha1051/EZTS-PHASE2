class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def deleting_firstnode(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deleting_lasttnode(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def deleting_atposition(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
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
obj.display()
print("deleting at beginning")
obj.deleting_firstnode()
print("")
obj.display()
print("deleting at the end")
obj.deleting_lasttnode()
print("")
obj.display()
print("deleting at specified position")
obj.deleting_atposition()
print("")