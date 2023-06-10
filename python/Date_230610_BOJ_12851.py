from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = []
def bfs(N,K):
    queue = deque([])  # bfs 탐색을 위한 덱 선언
    min_cnt = 100001
    answer = 0
    # 큐에는 현재 위치와 현재 위치까지 오는데 걸린 시간을 저장한다.
    queue.append((N,0))
    # 방문 여부를 저장하는 리스트
    visited = [True] * 100001
    # 방문 여부를 저장하는 리스트에 현재 위치를 방문했다고 표시한다.
    # 큐가 빌 때까지 반복한다.
    while queue:
        # 현재 위치와 현재 위치까지 오는데 걸린 시간을 가져온다.
        x,time = queue.popleft()
        # 현재 위치가 목표 위치와 같다면 현재 위치까지 오는데 걸린 시간을 반환한다.
        if x == K:
            min_cnt = min(min_cnt, time)
            if time == min_cnt:
                answer += 1
            elif time > min_cnt:
                return [min_cnt, answer]

        visited[x] = False
        move = [-1,1,x]
        for i in move:
            new_x = x + i
            if 0<=new_x<=100000 and visited[new_x]:
                queue.append((new_x,time+1))
    return [min_cnt, answer]

print(*bfs(N,K),sep='\n')