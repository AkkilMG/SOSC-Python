string = input("enter string: ").strip('')
rev = string[::-1]
if string == rev:
    print("it is a palindrome") 
else:
    print("it is not a palindrome")
