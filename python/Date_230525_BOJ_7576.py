from collections import deque
M, N = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

day = 0
q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    y, x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue

        if graph[ny][nx] != 0:
            continue

        # 이동 조건
        if graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            q.append((ny, nx))


def check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:

                return -1  # 0값이 있다면 -1

    return max(map(max, graph)) - 1  # graph에서 최대값을 추출

print(check())
