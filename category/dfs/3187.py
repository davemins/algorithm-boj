'''
# 문제 이해
양치기 소년 버전의 dfs

# 발상
탐색에 대한 부분이다.

# 복잡도
데이터가 n개일 대 O(n)의 시간복잡도를 가진다.

'''
r, c = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(input()))  # 입력을 list로 변환

def dfs(x, y, result):
    if x < 0 or x >= r or y < 0 or y >= c:  # 경계를 벗어났는지 체크
        return result
    if graph[x][y] != '#':  # 아직 방문하지 않은 곳이면
        if graph[x][y] == 'k':  # 양일 경우
            result[0] += 1
        if graph[x][y] == 'v':  # 늑대일 경우
            result[1] += 1
        graph[x][y] = '#'  # 방문한 곳은 벽으로 처리
        # 상하좌우로 DFS 탐색
        dfs(x - 1, y, result)
        dfs(x + 1, y, result)
        dfs(x, y - 1, result)
        dfs(x, y + 1, result)
    return result

result = [0, 0]  # 전체 양과 늑대 수
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':  # 방문하지 않은 지역이라면 DFS 탐색 시작
            start = [0, 0]  # 현재 영역의 양과 늑대 수
            start = dfs(i, j, start)
            # 양이 더 많으면 늑대를 잡아먹음
            if start[0] > start[1]:
                result[0] += start[0]
            else:
                result[1] += start[1]

# 최종 결과 출력
print(str(result[0]) + ' ' + str(result[1]))

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
일단 dfs를 푸는 기본적으로 공식이 되는 코드를 외워두자.
그리고 문자열 입력에 대한 문법도 많이 부족하다.
위의 것만 훈련하면 잘 풀어낼 수 있을 것 같다.

근데 이거 보니까 bfs로 풀어야 풀린다..
둘 다 연습하자.
'''