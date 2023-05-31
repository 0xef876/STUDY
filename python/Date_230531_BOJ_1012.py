import sys
sys.setrecursionlimit(10000)
T = int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        arr[y][x]=1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    def dfs(x,y):
        arr[y][x]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<M and 0<=ny<N and arr[ny][nx]==1:
                dfs(nx,ny)
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                dfs(j,i)
                cnt+=1
    print(cnt)
