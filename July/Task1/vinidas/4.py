dec = int(input("enter decimal number: "))
def oct(num):
    rem = 0 
    i = 1
    while (num != 0):
        rem = rem+ (num%8)*i
        num = num//8
        i = i*10
    return rem
def bi(num):
    rem = 0 
    i = 1
    while (num != 0):
        rem = rem+ (num%2)*i
        num = num//2
        i = i*10
    return rem
print("octal = ",oct(dec))
print("binary = ",bi(dec))