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
    print('')

for i in range(row):
     print(" "*i+"* "*(row-i))

for i in range(3):
    print(" "*(3-i)+"* "*i)
for i in range(3,0,-1):
    print(" "*(3-i)+"* "*i)
print()
for i in range(4,0,-1):
    print(" "*(i)+"*"*(5-i))
print()
for i in range(4):
    for j in range(1,5-i):
        print(j,end =' ')
    print()