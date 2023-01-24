# 17219
import sys
a,b = map(int,sys.stdin.readline().split())
dic = {}
for _ in range(a):
    Id,password = map(str,sys.stdin.readline().split())
    dic[Id] = password

for _ in range(b):
    print(dic[input()])
