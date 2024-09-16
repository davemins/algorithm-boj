'''
# 문제 이해


# 발상


# 복잡도


'''
computer = int(input())
link = int(input())

information = []
computers = [[] for i in range(computer)]

for i in range(link):
    information.append(list(map(int, input().split())))

for j in information:
    computers[j[0] - 1].append(j)

def dfs(data, x, y, count):
    if data[x]:
        nx, ny = data[x].pop()
        count += 1
        count += dfs(data, nx, ny, count)
    return count

count = 0

count += dfs(computers, 0, 0, count)

result = count
print(count)
'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
구현하는데 시간이 너무 오래 걸린다.
'''