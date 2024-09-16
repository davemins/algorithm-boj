'''
# 문제 이해


# 발상


# 복잡도


'''
computer = int(input())  # 컴퓨터 수
link = int(input())  # 연결된 링크 수

# 각 컴퓨터에 연결된 컴퓨터 정보를 저장할 리스트
computers = [[] for _ in range(computer)]

# 연결 정보 입력받기
for _ in range(link):
    a, b = map(int, input().split())
    computers[a - 1].append(b - 1)
    computers[b - 1].append(a - 1)  # 양방향 연결

# DFS 함수
def dfs(computers, visited, x):
    visited[x] = True
    count = 1  # 현재 컴퓨터도 감염되므로 count = 1로 시작
    for neighbor in computers[x]:
        if not visited[neighbor]:
            count += dfs(computers, visited, neighbor)
    return count

# 방문 여부 체크 리스트
visited = [False] * computer

# 1번 컴퓨터(0번 인덱스)에서 시작
result = dfs(computers, visited, 0) - 1  # 1번 컴퓨터는 제외하고 세기 위해 -1

print(result)
'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
구현하는데 시간이 너무 오래 걸린다.
'''