N = int(input())
arr = [k for k in range(1,N+1)]
if len(arr) == 1:
    s = str(arr.pop(0)) + ' '
    print(s)
else:
    s = str(arr.pop(0)) + ' '

    while len(arr) != 1:
        arr.append(arr[0])
        arr.pop(0)
        s += str(arr.pop(0)) +' '
    s += str(arr.pop(0))
    print(s)
