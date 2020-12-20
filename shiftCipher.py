#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text,key):
    encryptedString = ''
    for word in text.split():
        for char in word.upper():
            encryptedString += alphabets[(alphabets.find(char) + key) % 26]
        encryptedString += ' '
    return encryptedString[:-1]

def decrypt(code, key):
    decryptString = ''
    for word in code.split():
        for char in word.upper():
            decryptString += alphabets[(alphabets.find(char) - key) % 26]
        decryptString += ' '
    return decryptString[:-1]

code = encrypt('Hello World',45)
print(f'Encryption => Hello World => {code}')
print(f'Decryption => {code} => {decrypt(code, 45)}')

#decrypting Zlkdoxqrixqflk vlr plisba qeb pefcq zfmebo without knowing key
for key in range(26):
    print(f"Key = {key} {decrypt('Zlkdoxqrixqflk vlr plisba qeb pefcq zfmebo',key)}")

#from my program 23 is the possible decrypt key