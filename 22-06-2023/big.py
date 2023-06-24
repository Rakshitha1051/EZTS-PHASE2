def big(x,y):
    big=x if  x>y else y
    print("the biggest value",big)
x=int(input("enter x value"))
y=int(input("enter y value"))
big(x,y)
print("task has completed")
''' '''
def prime():
    x=int(input("enter a positive number"))
    if x>1:
        for i in range(2,x):   
           if x%i==0:
            print(x,"is not a prime")
            break
        else:
            print(x,"is a prime")
prime()
print("task has completed")
''' ''' 
def rel():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    return (a>b),(a<b),(a!=0),(a==b)
p,q,r,s=rel()
print(p)
print(q)
print(r)
print(s)
print("task has completed")
''' '''
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
s=int(input("enter a number"))
 fact(s)
''' '''
def big(a):
    if a>0:
        print(a,"is a positive")
    else:
        print(a,"is not a positive")
x=int(input("enter x value"))
big(x)
''' '''
def even():
    n=int(input("enter a value"))
    if n%2==0:
        return"even"
    else:
        return "odd"
r=even()
print(r)
''' '''
