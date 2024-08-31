"""바구니 순서 바꾸기"""

n, m=map(int, input().split())
tmp = [i+1 for i in range (n)]

for _ in range(m):
    begin, end, mid = map(int, input().split())
    tmp[begin - 1 : end] = tmp[mid - 1 : end] + tmp[begin - 1 : mid - 1]

print(*tmp)