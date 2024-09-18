'''
# 문제 이해
그 자리의 값만큼 이동할 수 있는 문제

# 발상
탐색에 대한 부분이다.

# 복잡도
데이터가 n개일 대 O(n)의 시간복잡도를 가진다.

'''
from collections import deque

n = int(input())  # 게임 구역의 크기 입력

# 게임판 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 여부를 저장하는 리스트
visited = [[False] * n for _ in range(n)]

# 이동 가능한 방향 (오른쪽, 아래)
dx = [0, 1]
dy = [1, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 이동할 수 있는 칸 수
        distance = graph[x][y]

        # 도착지점에 도착하면 'HaruHaru' 출력하고 함수 종료
        if distance == -1:
            print("HaruHaru")
            return

        # 두 가지 방향으로 이동 (오른쪽, 아래)
        for i in range(2):
            nx = x + dx[i] * distance
            ny = y + dy[i] * distance

            # 범위 내에 있고, 아직 방문하지 않은 곳이면 큐에 추가
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    # 만약 도착지점에 도달하지 못했다면 'Hing' 출력
    print("Hing")


# BFS를 시작하는 지점은 (0, 0)
bfs(0, 0)

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
원리는 이해했으니 벼락치기 하듯이 dfs, bfs를 일단 암기하자.
구현을 못하면 아무리 발상이 있어도 소용없다.

그리고 문제를 잘 읽어보자..
두 가지 방향으로만 이동할 수 있는 것인지 몰랐다.
'''