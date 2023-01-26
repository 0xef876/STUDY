# BOJ 1620
import sys
a,b = map(int,sys.stdin.readline().split())
dic = {}
dic2 = {}
for i in range(a):
    poketmon = sys.stdin.readline().strip()
    dic[poketmon] = str(i+1)
    dic2[str(i+1)] = poketmon
for _ in range(b):
    temp = sys.stdin.readline().strip()
    if temp.isalpha():
        print(dic[temp])
    else:
        print(dic2[temp])
