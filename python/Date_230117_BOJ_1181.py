# BOJ 1181
def solution():
    li = set()
    N = int(input())
    for i in range(N):
        s = input()
        li.add(s)
    ans = sorted(li,key=lambda x : (len(x),x))

    return ans

for i in solution():
    print(i)