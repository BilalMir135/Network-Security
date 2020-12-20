#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt_decrypt(text):
    encryptedString = ''
    for word in text.split():
        for char in word.upper():
            encryptedString += alphabets[alphabets[::-1].find(char)]
        encryptedString += ' '
    return encryptedString[:-1]

code = encrypt_decrypt('Hello World')
print(f'Encryption => Hello World => {code}')
print(f"Decryption => {code} => {encrypt_decrypt(code)}")