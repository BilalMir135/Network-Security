#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#(ax+b)%26
def encrypt(text, a, b):
    if(a>25 or a==13 or a%2==0):
        return 'Invalid value of a, a should be an odd num in range of 0-25'
    elif (b>25):
        return 'Invalid value of b, b should be in a range of 0-25'
    else:
        encryptedString = ''
        for word in text.split():
            for char in word.upper():
                 encryptedString += alphabets[(a*alphabets.find(char)+b)%26]
            encryptedString += ' '
        return encryptedString[:-1]

# ax%26=1
def a_Inverse(a):
    for x in range(1,26,2):
        if((a*x)%26==1):
            return x
        continue

# aInverse(x-b)%26
def decrypt(code,a,b):
    aInv = a_Inverse(a)
    decryptString = ''
    for word in code.split():
        for char in word.upper():
            decryptString += alphabets[(aInv*(alphabets.find(char)-b))%26]
        decryptString += ' '
    return decryptString[:-1]


code = encrypt('Hello World',15,20)
print(f'Encryption => Hello World => {code}')
print(f"Decryption => {code} => {decrypt(code,15,20)}")
print("----------------------------------------------------------------------------------\n")

#decrypting UVOHCBN NDU OYRU WGND IXXGVU OGBDUH NUODVGEQU without knowing keys
for a in range(1,26,2):
    if(a==13):
        continue
    for b in range(26):
        print(f"a = {a} , b = {b} => {decrypt('UVOHCBN NDU OYRU WGND IXXGVU OGBDUH NUODVGEQU',a,b)}")
    print('\n')
    