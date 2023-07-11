def encode(string,k):
    newstring =""
    for i in string: 
        val =ord(i)
        for j in range(k):
             val+=1
             if(val >122):
                val = 97
             elif(val>90 and val<97):
                 val =75
        newstring += chr(val)
    print("The encoded message is "+newstring)

def decode(string,k):
    newstring =""
    for i in string: 
        val =ord(i)
        for j in range(k):
             val-=1
             if(val <65):
                val = 90
             elif(val>90 and val<97):
                 val =122
        newstring += chr(val)
     
    print("The decoded message is "+newstring)
print("Type of encode to encrypt and decode to decrypt:")
type = input()
print("type message: ")
stri = input()
print("enter the number of shifts: ")
off  = int(input())
if(type == "encode"):
    encode(stri,off)   
elif(type == 'decode'):
    decode(stri,off)
else:
    print('error input ') 