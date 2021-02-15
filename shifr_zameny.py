import random
from collections import Counter

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


########################################################## 1 METHOD
# decrypting teachers cryptographic text
# collection.Counter ()
# используя collection.Counter () для получения
# количество каждого элемента в строке
# with open('example.txt', encoding="utf-8") as ex:
#     read_ex = ex.read().strip()
#     result = Counter(read_ex)
######################################################### 2 METHOD
# используя dict.get () для подсчета
# каждого элемента в строке
result = {}
with open('example.txt', encoding="utf-8") as ex:
    read_ex = ex.read().strip()
    for keys in read_ex:
        result[keys] = result.get(keys, 0) + 1

sorted_result = {}
sorted_keys = sorted(result, key=result.get, reverse=True)
for w in sorted_keys:
    sorted_result[w] = result[w]
#########################################################

fr_dict = {' ': 0.175, 'о': 0.089, 'е': 0.072, 'а': 0.062, 'и': 0.062, 'т': 0.053, 'н': 0.053, 'с': 0.045,
           'р': 0.040, 'в': 0.038, 'л': 0.035, 'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023, 'у': 0.021,
           'я': 0.018, 'ы': 0.016, 'з': 0.016, 'ь': 0.014, 'ъ': 0.014, 'б': 0.014, 'г': 0.013, 'ч': 0.012,
           'й': 0.010, 'х': 0.009, 'ж': 0.007, 'ю': 0.006, 'ш': 0.006, 'ц': 0.004, 'щ': 0.003, 'э': 0.003,
           'ф': 0.002}

########################################################
# print("Count of all characters in example.txt is:\n" + str(result))
print("The result of freq analys: " + str(sorted_result))  # Counted
print("Reference freq analys of Russian alphabeth:" + str(fr_dict))  # reference
spis = ''.join(fr_dict.keys())
print("The reference like list:" + str(spis))
######################################################## encryption attempt
def decrypt_p(result, fr_dict):
    fr = fr_dict
    d = dict()
    res = ""
    for i in range(len(result)):
        d[result[i]] = fr[i]
    with open('example.txt', encoding="utf-8") as enc:
        read_data = enc.read().strip()
        for i in range(len(read_data) - 1):
            res += d[read_data[i]]
    with open('output_example_dec.txt', 'w', encoding="utf-8") as o:
        o.write(res)
#######################################################

res_join = ''.join(sorted_result.keys())
fr_dict_join = ''.join(fr_dict.keys())
decrypt_p(res_join, fr_dict_join)

