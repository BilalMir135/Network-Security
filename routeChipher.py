#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

import math

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def removeSpaces (text):
    newStr = ''
    for word in text.split():
        newStr += word
    return newStr


#@DESC split text into key length chunks
#EG Hello my friend , 4 => ['Hell','o my',' frie', 'nd__']
def splitText(text,count):
    splittedText = [text[i:i+count] for i in range(0, len(text), count)]
    if len(splittedText[-1]) < count:
        splittedText[-1] += '_'*(count-len(splittedText[-1]))
    return splittedText


#@DESC create encrypting table
#EG Hello,12 => {1:{H,l,o},2:{e,l,_}}
def generateEncryptingTable(text,key):
    table = []
    newText = removeSpaces(text)
    count = math.ceil(len(newText)/key)
    splittedText = splitText(newText,count)
    for splittedItem in splittedText:
        table.append(list(splittedItem))
    return [table, count]

#@DESC create decrypting table
#EG Hloel_, 12, 3 => {1:{H,l,o},2:{e,l,_}}
def generateDecryptingTable(text,key):
    table = [[] for x in range(0,key)]
    newText = removeSpaces(text)
    count = math.ceil(len(newText)/key)
    splittedText = splitText(text,key)
    for splittedItem in splittedText:
        keyCount = 0
        for splittedChar in splittedItem:
            table[keyCount].append(splittedChar)
            keyCount += 1
    return [table, count]

def simpleRuleEncrypt(text,key):
    encryptedString = ''
    table, count = generateEncryptingTable(text,key)
    for x in range(0,count):      
        for row in table:
            encryptedString += row[x]
    return encryptedString

def simpleRuleDecrypt(code, key):
    decryptedString = ''
    table, count = generateDecryptingTable(code,key)
    for row in table:
        for item in row:
            if item != '_':
                decryptedString += item
    return decryptedString

def oddColumnFirstRuleEncrypt(text,key):
    encryptedString = ''
    table, count = generateEncryptingTable(text,key)
    for x in range(1,count,2):      
        for row in table:
            encryptedString += row[x]
    for x in range(0,count,2):
        for row in table:
            encryptedString += row[x]
    return encryptedString

def oddColumnFirstRuleDecrypt(code,key):
    decryptedString = ''
    table, count = generateDecryptingTable(code,key)
    for row in table:
        evenIndex = round(count/2)
        oddIndex = 0
        for x in range(0,count):
            if evenIndex < count:
                if row[evenIndex] != '_':
                        decryptedString += row[evenIndex]
                evenIndex += 1
            if oddIndex < round(count/2):
                if row[oddIndex] != '_':
                        decryptedString += row[oddIndex]
                oddIndex += 1
    return decryptedString

#Task # 01
key = 2
text = 'WE ARE STUDYING AND TRYING TO UNDERSTAND TRANSPOSITION CIPHERS'
code = simpleRuleEncrypt(text,key)
print('----------------------Task # 01----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {simpleRuleDecrypt(code,key)}\n')

#Task # 02
key = 4
text = 'Lets try another route to secure our the message using tanspoiton cipher'
code = oddColumnFirstRuleEncrypt(text,key)
print('----------------------Task # 02----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {oddColumnFirstRuleDecrypt(code, key)}\n')