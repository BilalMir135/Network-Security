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
    keyCount = 0
    plainTextCount = 0
    for char in text:
        if keyCount < len(key):
            newText += key[keyCount]
            keyCount += 1
        else:
            newText += text[plainTextCount]
            plainTextCount +=1
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
    keyCount = 0
    plainTextcount = 0
    currentKey = key[0].upper()
    for cipherChar in newText:
        result = (alphabets.find(cipherChar) - alphabets.find(currentKey) + 26) % 26
        decryptedString += alphabets[result]
        keyCount += 1
        if keyCount < len(key):
            currentKey = key[keyCount].upper()
        else:
            currentKey = decryptedString[plainTextcount]
            plainTextcount += 1
    return decryptedString

#Task # 01
key = 'Hi'
code = encrypt('Hello World',key)
print('----------------------Task # 01----------------------')
print(f'Encryption => Hello World => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

#Task # 02
key = 'work'
code = 'Pvrdl zo xskm xo vm'
print('----------------------Task # 02----------------------')
print(f'Decryption => {code} => {decrypt(code, key)}\n')