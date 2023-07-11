c = ord('A') - 1 

for i in range(1, 5):
    for j in range(1, i + 1):
        c = c + 1
        print(chr(c), end=' ')
    print()

c=0
for i in range(1,5):
    for j in range(1,i+1):
        
        c+=1
        print(c," ",end='')    
    print()    


c = ord('A') - 1 
for i in range(1,6):
    for j in range(1,i+1):
        
        c+=1
        print(chr(c)," ",end='')    
    print()    


    


for i in range(5):
    print(" "*i+"* "*(4-i+1))


for i in range(3):
    print(" "*(2-i+1)+"* "*i)
for i in range(3):
    print(" "*i+"* "*(2-i+1))



for i in range(5):
    print(" "*(4-i+1)+"*"*i)


for i in range(0,4):
    for j in range(4-i):
        print(j+1,end=" ")
    print()        