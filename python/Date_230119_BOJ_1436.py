#1436
import sys

n = int(sys.stdin.readline())
ans = 0
count = 665
while True:
    count += 1
    if '666' in str(count):
        ans += 1
        if ans == n:
            print(count)
            break
