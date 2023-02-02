# BOJ 1927

import sys,heapq
n=int(sys.stdin.readline().rstrip())
heap = []
for i in range(n):
    x=int(sys.stdin.readline().rstrip())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)
