a,b = map(int,input().split())


def f(n):
    count = 0

    k = 0
    while 2**k <= n:
        # 0011: p = 4
        p = 2**(k+1)
        p_count = (n+1)//p

        # (완성된 패턴의 갯수) * (패턴의 길이의 절반 = 한 패턴에서 1은 절반이 나오기 때문)
        count += p_count * (p//2)

        # 완성되지 않은 곳의 길이... 0011001에서 left는 3이다.
        left = (n+1) % p
        # 001에서, 00의 길이는 p/2
        count += max(0, left - p//2)

        k += 1

    return count
print(f(b)-f(a-1))