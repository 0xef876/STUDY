import sys

def dfs(graph, start, visited):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(graph, v, visited)

n, m = map(int, sys.stdin.readline().split())

# 인접 리스트 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
