#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

def matrix(x,y,initial,key):
    return [[initial for i in range(x)] for j in range(y)]

def initializeMatrix(key):
    result=list()
    for c in key:
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91):
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix=matrix(5,5,0,key) 
    for i in range(0,5): 
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    return my_matrix


def locindex(c,my_matrix):
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(text,key):  #Encryption
    msg=text
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    encryptedString = ''
    my_matrix = initializeMatrix(key.upper())
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i],my_matrix)
        loc1=list()
        loc1=locindex(msg[i+1],my_matrix)
        if loc[1]==loc1[1]:
            encryptedString += "{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]])
        elif loc[0]==loc1[0]:
            encryptedString += "{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5])
        else:
            encryptedString += "{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]])  
        i=i+2  
    return encryptedString      
                 
def decrypt(code,key):
    msg=code
    msg=msg.upper()
    msg=msg.replace(" ", "")
    i=0
    decryptedString = ''
    my_matrix = initializeMatrix(key.upper())
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i],my_matrix)
        loc1=list()
        loc1=locindex(msg[i+1],my_matrix)
        if loc[1]==loc1[1]:
            decryptedString += "{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]])
        elif loc[0]==loc1[0]:
            decryptedString += "{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5])
        else:
            decryptedString += "{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]])
        i=i+2  
    return decryptedString.replace('X','')      

#Task # 01
key = 'Hi'
text = 'Hello World'
code = encrypt(text,key)
print('----------------------Task # 01----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

#Task # 02
key = 'Success'
text = 'Paly fair is completely different way to encrypt the message'
code = encrypt(text,key)
print('----------------------Task # 02----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

