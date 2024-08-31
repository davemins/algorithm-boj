"""과제 안 내신 분..?"""

num_list = [0 for i in range(30)]

for i in range(1, 31):
    num_list[i-1] = i

for i in range(28):
    n = int(input())
    num_list.remove(n)

for j in num_list:
    print(j, end='\n')