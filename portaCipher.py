#Group Members
#Bilal Mir B17158013
#Waliullah B17158055

alphabets = {
    "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
    "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
}

def create_table(key):
    return [alphabets[char] for char in key.upper()]

def get_position(table, char):
    if char in table[0]:
        row = 0
    else:
        row = 1 if char in table[1] else -1
    return (None, None) if row == -1 else (row, table[row].index(char))

def get_opponent(table, char):
    row, col = get_position(table, char.upper())
    if row == 1:
        return table[0][col]
    else:
        return table[1][col] if row == 0 else char

def encrypt_decrypt(text, key):
    cipher = ""
    count = 0
    table = create_table(key)
    for char in text.upper():
        cipher += get_opponent(table[count], char)
        count = (count + 1) % len(table)
    return cipher

#Task # 01
key = 'Hi'
code = encrypt_decrypt('Hello World',key)
print('----------------------Task # 01----------------------')
print(f'Encryption => Hello World => {code}')
print(f'Decryption => {code} => {encrypt_decrypt(code, key)}\n')