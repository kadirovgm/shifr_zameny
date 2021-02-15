import random


alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНПРСТУФЧЦЧШЩЪЫЬЭЮЯ '


def keygen(alphabet):
    with open('key.txt', mode='w', encoding="utf-8") as file:
        key = ''.join(random.sample(alphabet, len(alphabet)))
        file.write(key)
    return key


key = keygen(alphabet)


def encrypt(alphabet, key):
    k = key
    d = dict()
    res = ""
    for i in range(len(alphabet)):
        d[alphabet[i]] = k[i]
    with open('file.txt', encoding="utf-8") as f:
        read_data = f.read().strip()
        for i in range(len(read_data)-1):
            res += d[read_data[i]]
    with open('output_enc.txt', 'w', encoding="utf-8") as o:
        o.write(res)


def decrypt(key, alphabet):
    a = alphabet
    d = dict()
    res = ""
    for i in range(len(key)):
        d[key[i]] = a[i]
    with open('output_enc.txt', encoding="utf-8") as enc:
        read_data = enc.read().strip()
        for i in range(len(read_data)-1):
            res += d[read_data[i]]
    with open('output_dec.txt', 'w', encoding="utf-8") as o:
        o.write(res)


# next code is for menu
print(" -----------------------------")
print("| Type 'encrypt' or 'decrypt' |")
print("| Type 'back' for exit        |")
print(" -----------------------------")
temp = 0
while temp < 10:
    choise = input()
    if choise == 'encrypt':
        encrypt(alphabet, key)
        temp += 1
        print("File.txt encrypted! Check output_enc.txt")
    elif choise == 'decrypt':
        decrypt(key, alphabet)
        temp += 1
        print("output_enc.txt decrypted! Check output_dec.txt")
    elif choise == 'back':
        break
    else:
        print("Wrong, try again 'encrypt' or  'decrypt'")

