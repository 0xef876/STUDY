#10773
import sys
k = int(sys.stdin.readline())
data = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n != 0:
       data.append(n)
    else:
        data.pop()
print(sum(data))
