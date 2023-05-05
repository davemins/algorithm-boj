"""바구니 순서 바꾸기"""

# N, M = map(int, input().split())

# bag = [0 for i in range(N)]
# new_bag = []

# for i in range(N):
#     bag[i] = i + 1

# new_bag = [0 for i in range(N)]

# for j in range(M):
#     new_bag = [0 for i in range(N)]
#     begin, end, mid = map(int, input().split())
#     mark = mid
#     mark2 = begin
#     for n in range(begin -1, mid - 1):
#         new_bag[n] = bag[mark - 1]
#         mark += 1
#         if mark == end + 1:
#             break
#     for m in range(mid - 1, end):
#         new_bag[m] = bag[mark2 - 1]
#         mark2 += 1
#         if mark2 > mid:
#             break
#     for l in range(begin - 1, end):
#         bag[l] = new_bag[l]

# for k in bag:
#     print(k, end=' ')

import sys

n,m=map(int,sys.stdin.readline().split())
tmp=[i+1 for i in range (n)]

for _ in range(m):
    begin,end,mid=map(int,sys.stdin.readline().split())
    tmp[begin-1:end]=tmp[mid-1:end]+tmp[begin-1:mid-1]

print(*tmp)
