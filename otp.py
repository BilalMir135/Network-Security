import string
import random
import sys

abc = string.ascii_lowercase
one_time_pad = list(abc)

def encrypt(msg, key):
    ciphertext = ''
    for idx, char in enumerate(msg):
        charIdx = abc.index(char)
        keyIdx = one_time_pad.index(key[idx])

        cipher = (keyIdx + charIdx) % len(one_time_pad)
        ciphertext += abc[cipher]

    return ciphertext

def decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''

    charIdx = abc.index(ciphertext[0])
    keyIdx = one_time_pad.index(key[0])

    cipher = (charIdx - keyIdx) % len(one_time_pad)
    char = abc[cipher]

    return char + decrypt(ciphertext[1:], key[1:])


print(encrypt(msg, key))
print(decrypt(msg, key))