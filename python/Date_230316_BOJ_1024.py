N, L = map(int, input().split())

for length in range(L, 101):
    if length % 2 == 0:
        if N % length == length // 2:
            start = N // length - length // 2 +1
            if start < 0:
                continue
            end = start + length
            result = [str(i) for i in range(start, end)]
            print(" ".join(result))
            break
    else:
        if N % length == 0:
            start = N // length - (length - 1) // 2
            if start < 0:
                continue
            end = start + length - 1
            result = [str(i) for i in range(start, end+1)]
            print(" ".join(result))
            break
else:
    print("-1")
