import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

if data[n-1][n-1] == 1:
    print(0)
    exit()

def dfs(x, y, d):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return
    if d == 0 or d == 2:
        if x+1 < n and data[y][x+1] == 0:
            dfs(x+1, y, 0) # 가로
    if d == 1 or d == 2:
        if y+1 < n and data[y+1][x] == 0:
            dfs(x, y+1, 1) # 세로
    if x+1 < n and y+1 < n and data[y][x+1] == 0 and data[y+1][x] == 0 and data[y+1][x+1] == 0:
        dfs(x+1, y+1, 2) # 대각선

dfs(1, 0, 0)
print(answer)
