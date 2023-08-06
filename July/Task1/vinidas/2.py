
x=input("enter the string ")
def vow(char):
    for i in range(len(char)): 
        if char[i] in r'[aeiouAEIOU]': 
            char.replace(char[i],'-')
    return print("new string = ",char)
vow(x)