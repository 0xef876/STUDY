#BOJ 11286

import sys,heapq

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
    val = int(sys.stdin.readline().rstrip())
    if val != 0:
        heapq.heappush(heap,(abs(val),val))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
