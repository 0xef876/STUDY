N,K = map(int,input().split())
# 최소 시간을 구하는 문제이므로 bfs를 사용한다.
# bfs는 최단거리를 구하는 알고리즘이다.
# 최단거리를 구하는 알고리즘은 bfs, 다익스트라, 플로이드 와샬 알고리즘이 있다.
# bfs는 가중치가 없는 그래프에서 최단거리를 구하는 알고리즘이다.
# 다익스트라는 가중치가 있는 그래프에서 최단거리를 구하는 알고리즘이다.
# 플로이드 와샬은 모든 정점에서 모든 정점으로의 최단거리를 구하는 알고리즘이다.

# bfs는 큐를 사용한다.
# 큐에는 현재 위치와 현재 위치까지 오는데 걸린 시간을 저장한다.


def bfs(N,K):
    # 큐에는 현재 위치와 현재 위치까지 오는데 걸린 시간을 저장한다.
    queue = [(N,0)]
    # 방문 여부를 저장하는 리스트
    visited = [False] * 100001
    # 방문 여부를 저장하는 리스트에 현재 위치를 방문했다고 표시한다.
    visited[N] = True
    # 큐가 빌 때까지 반복한다.
    while queue:
        # 현재 위치와 현재 위치까지 오는데 걸린 시간을 가져온다.
        x,time = queue.pop(0)
        # 현재 위치가 목표 위치와 같다면 현재 위치까지 오는데 걸린 시간을 반환한다.
        if x == K:
            return time
        # 현재 위치가 목표 위치와 같지 않다면
        # 현재 위치에서 갈 수 있는 위치를 확인한다.
        for i in (x-1,x+1,x*2):
            # 갈 수 있는 위치가 0보다 크고 100000보다 작고
            # 방문한 적이 없다면
            if 0<=i<=100000 and not visited[i]:
                # 큐에 현재 위치를 방문했다고 표시한다.
                visited[i] = True
                # 큐에 현재 위치와 현재 위치까지 오는데 걸린 시간+1을 저장한다.
                if i == x*2:
                    queue.insert(0,(i,time))
                else:
                    queue.append((i,time+1))

# bfs를 호출하고 반환된 값을 출력한다.
print(bfs(N,K))
