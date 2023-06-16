import sys
sys.setrecursionlimit(10**6)

n = int(input())
dic = {1:[]}

for i in range(n-1):
    a,b = map(int,input().split())

    if a not in dic:
        dic[a] = []
    if b not in dic:
        dic[b] = []

    if dic[a] == []:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if dic[b] == []:
        dic[b] = [a]
    else:
        dic[b].append(a)

visited = [False]*(n+1)
parent = [0]*(n+1)

def dfs(v):
    visited[v] = True
    for i in dic[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)


dfs(1)
for i in range(2,n+1):
    print(parent[i])