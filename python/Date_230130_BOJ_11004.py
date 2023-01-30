#BOJ 11004
import sys
a,b = map(int,sys.stdin.readline().split());
data = list(map(int,sys.stdin.readline().split()))
data.sort()
print(data[b-1])
