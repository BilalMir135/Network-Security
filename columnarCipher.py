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

#@DESC convert text key into number
#@EG hack => 3124
def convertKey(key):
    newKey = list(key.upper())
    count = 1
    for alphaChar in alphabets:
        for keyChar in key.upper():
            if keyChar == alphaChar:
                newKey[newKey.index(alphaChar)] = str(count)
                count +=1
    return ''.join(newKey)

#@DESC split text into key length chunks
#EG Hello my friend , 4 => ['Hell','o my',' frie', 'nd__']
def splitText(text,count):
    splittedText = [text[i:i+count] for i in range(0, len(text), count)]
    if len(splittedText[-1]) < count:
        splittedText[-1] += '_'*(count-len(splittedText[-1]))
    return splittedText

#@DESC create inital table with empty arrays
#EG 3124 => {3:[],1:[],2:[],4:[]}
def createInitialTable(key):
    table = {}
    for char in key:
        table[int(char)] = []
    return table

#@DESC create encrypting table
#EG Hello,12 => {1:{H,l,o},2:{e,l,_}}
def generateEncryptingTable(text,key):
    table = createInitialTable(key)
    splittedText = splitText(text,len(key))
    for splittedItem in splittedText:
        for splittedChar, keyChar in zip(splittedItem,key):
                table[int(keyChar)].append(splittedChar)
    sortedTable = {}
    for x in sorted(table.keys()):
        sortedTable[x] = table[x]
    return sortedTable

#@DESC create decrypting table
#EG Hloel_, 12, 3 => {1:{H,l,o},2:{e,l,_}}
def generateDecryptingTable(text,key,count):
    table = createInitialTable(key)
    splittedText = splitText(text,count)
    for splittedItem, keyChar in zip(splittedText,sorted(list(key))):
        for splittedChar in splittedItem:
            table[int(keyChar)].append(splittedChar)
    return table

def encrypt(text,key):
    encryptedString = ''
    newText = removeSpaces(text)
    newKey = convertKey(key)
    table = generateEncryptingTable(newText,newKey)
    for value in table.values():
        for char in value:
            encryptedString += char
    return encryptedString 


def decrypt(code,key):
    decryptedString = ''
    newCode = removeSpaces(code)
    newKey = convertKey(key)
    count = math.ceil(len(newCode)/len(key))
    table = generateDecryptingTable(newCode,newKey,count)
    for x in range(0,count):
        for value in table.values():
            if value[x] != '_':
                decryptedString += value[x]
    return decryptedString

#Task # 01
key = 'Hi'
text = 'Hello World'
code = encrypt(text,key)
print('----------------------Task # 01----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

#Task # 02
key = 'Mango'
text = 'Lets try columnar cipher to secure our the message'
code = encrypt(text,key)
print('----------------------Task # 02----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')
