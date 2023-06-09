import sys
from collections import deque

visited = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = [i, j]
        elif graph[i][j] == 0:
            visited.append([i, j])

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs(start)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print(-1, end=' ')
        elif graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(graph[i][j]-2, end=' ')

    print()
