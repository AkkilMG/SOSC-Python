a = int(input("Enter a decimal number "))
def octal(a):
    result = 0
    multiplier = 1

    while a != 0:
        digit = a % 8
        result += digit * multiplier
        multiplier *= 10
        a //= 8

    return result

def binary(a):
    m=1
    r=0
    while a!=0:
        d=a%2
        r+=d*m
        m*=10
        a//=2
    return r    
print("the octal value of the given number is ",octal(a))
print("the binary value of the given number is ",binary(a))