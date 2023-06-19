import sys
sys.setrecursionlimit(10**6)
n, m = map(int,input().split())

def backtracking(data,visited):
    if len(visited) == m:
        print(*visited)
        return
    for i in range(len(data)):
        if len(visited) > 0 and data[i] in visited:
            continue

        visited.append(data[i])
        backtracking(data,visited)
        visited.pop()

backtracking([i for i in range(1,n+1)],[])