# BOJ 11866 
n,k = map(int,input().split())
li = [i for i in range(1,n+1)]
idx = 0
s = "<"
for _ in range(n):
    idx += k-1
    if idx >= len(li):
        idx = idx%len(li)
    s += str(li.pop(idx))
    s += ", "
print(s[:-2]+">")