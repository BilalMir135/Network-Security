#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def removeSpaces (text):
    newStr = ''
    for word in text.split():
        newStr += word
    return newStr

def convertTextIntoKey (text, key):
    newText = ''
    count = 0
    for char in text:
        if count < len(key):
            newText += key[count]
        else:
            count = 0
            newText += key[count]
        count += 1
    return newText

def encrypt(text,key):
    encryptedString = ''
    newText = removeSpaces(text.upper())
    convertedText = convertTextIntoKey(newText,key.upper())
    for plainChar, keyChar in zip(newText,convertedText):
        encryptedString += alphabets[(alphabets.find(plainChar) + alphabets.find(keyChar)) % 26]
    return encryptedString

def decrypt(code,key):
    decryptedString = ''
    newText = removeSpaces(code.upper())
    convertedText = convertTextIntoKey(code,key.upper())
    for encryptedChar, keyChar in zip(newText,convertedText):
        decryptedString += alphabets[(alphabets.find(encryptedChar) - alphabets.find(keyChar)) % 26]
    return decryptedString

#Task # 01
key = 'Hi'
code = encrypt('Hello World',key)
print('----------------------Task # 01----------------------')
print(f'Encryption => Hello World => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

#Task # 02
key = 'TRYHARD'
code = 'OZELNVUXTGWHVUBJLVTYDKURVDVFKPNA'
print('----------------------Task # 02----------------------')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

#Task # 03
key = 'Practice'
code = 'XCECKVJSLKOUHTXIIYEXBOGRTIEEBXJIG'
print('----------------------Task # 03----------------------')
print(f'Decryption => {code} => {decrypt(code, key)}\n')