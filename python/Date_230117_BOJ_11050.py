## 11050

def solution(n,k):
    if k == 0 or n == k:
        return 1
    return solution(n-1,k) + solution(n-1,k-1)

a, b = map(int,input().split())

print(solution(a,b))