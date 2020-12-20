#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text):
    encryptedString = ''
    for word in text.split():
        for char in word.upper():
            encryptedString += alphabets[(alphabets.find(char) + 13) % 26]
        encryptedString += ' '
    return encryptedString[:-1]

def decrypt(code):
    decryptString = ''
    for word in code.split():
        for char in word.upper():
            decryptString += alphabets[(alphabets.find(char) - 13) % 26]
        decryptString += ' '
    return decryptString[:-1]

code = encrypt('Hello World')
print(f'Encryption => Hello World => {code}')
print(f'Decryption => {code} => {decrypt(code)}')
