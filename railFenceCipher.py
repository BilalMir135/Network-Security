#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

def createRail(text,key):
    rail = [['\n' for i in range(len(text))] for j in range(key)] 
    return rail
        

def encrypt(text, key): 
	rail = createRail(text,key)
	dir_down = False
	row, col = 0, 0	
	for i in range(len(text)): 
		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
		rail[row][col] = text[i] 
		col += 1
		if dir_down: 
			row += 1
		else: 
			row -= 1
	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return("" . join(result)) 

def decrypt(code, key): 
	rail = createRail(code,key)
	dir_down = None
	row, col = 0, 0
	for i in range(len(code)): 
		if row == 0: 
			dir_down = True
		if row == key - 1: 
			dir_down = False
		
		rail[row][col] = '*'
		col += 1
		if dir_down: 
			row += 1
		else: 
			row -= 1			
	index = 0
	for i in range(key): 
		for j in range(len(code)): 
			if ((rail[i][j] == '*') and
			(index < len(code))): 
				rail[i][j] = code[index] 
				index += 1		
	result = [] 
	row, col = 0, 0
	for i in range(len(code)): 
		if row == 0: 
			dir_down = True
		if row == key-1: 
			dir_down = False
		if (rail[row][col] != '*'): 
			result.append(rail[row][col]) 
			col += 1
		if dir_down: 
			row += 1
		else: 
			row -= 1
	return("".join(result)) 

#Task # 01
key = 3
text = 'Hello World'
code = encrypt(text,key)
print('----------------------Task # 01----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')

#Task # 02
key = 5
text = 'We have studied the three different techniques of transposition ciphers'
code = encrypt(text,key)
print('----------------------Task # 02----------------------')
print(f'Encryption => {text} => {code}')
print(f'Decryption => {code} => {decrypt(code, key)}\n')