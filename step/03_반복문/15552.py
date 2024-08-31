"""빠른 A+B""" 

import sys

T = int(sys.stdin.readline())
list = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for i in range(T):
    print(list[i])