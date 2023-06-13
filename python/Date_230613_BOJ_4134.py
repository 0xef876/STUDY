n = int(input())
for i in range(n):
    # a보다 큰 소수 출력하기 최대한 빠르게
    a = int(input())
    if a == 1 or a == 0:
        print(2)
        continue
    for j in range(a, 2*a):
        for k in range(2, int(j**0.5)+1):
            if j % k == 0:
                break
        else:
            print(j)
            break
