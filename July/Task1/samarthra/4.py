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

print(octal(a))
