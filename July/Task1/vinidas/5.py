c = ord('A')
row = int(input("enter numbe of row :"))

for i in range(row):
     for j in range(i):
        print(chr(c+i-1),end =' ')
     print()  

c = 0 
for i in range(row):
    for j in range(i):
        c +=1
        print(c,end =' ')
    print()


c = ord('A')
for i in range(row):
    for j in range(i):
        print(chr(c),end = ' ')
        c+=1
    
    print()

for i in range(row,1):
    for j in range(i): 
        print('*',end = ' ')
    print()