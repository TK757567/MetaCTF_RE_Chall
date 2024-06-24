import base64

flag=input("enter the sauce: ")

enc=''

for i in flag:
    first=ord(i) ^ 0x1337
    second = first + 65
    enc+=chr(second) 

enc=base64.b64encode(bytes(enc, 'utf-8'))

print(enc.decode('utf-8'))

