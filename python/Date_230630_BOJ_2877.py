n = int(input())

def solve(n):
    if n == 1:
        return 4
    elif n == 2:
        return 7
    else:
        if n % 2 != 0:
            return solve(n//2) * 10 + 4
        else:
            return solve(n//2 - 1) * 10 + 7

print(solve(n))