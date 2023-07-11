x=input("enter the string ")
a='aeiouAEIOU'
def change(x):
    
    for i in x:
        if i in a:
            x=x.replace(i,'-')
            return x
print(change(x))        