

a=list(input("enter the list "))
def duplicate(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    print(x)  
duplicate(a)          