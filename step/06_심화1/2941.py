"""크로아티아 알파벳"""

alphabet = input()
unique_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = len(alphabet)


for i in unique_alphabet:
    num = alphabet.count(i)
    count -= num

print(count)