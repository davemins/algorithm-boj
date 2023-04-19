"""개수 세기"""

N = int(input())

a = input().split()

list_a = list(map(int, a))

num = int(input())

print(list_a.count(num))