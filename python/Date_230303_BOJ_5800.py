import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    k = data[0]
    new_data = data[1:]
    M = max(new_data)
    m = min(new_data)
    new_data.sort(reverse=True)
    gap = abs(new_data[0] - new_data[1])
    for j in range(1,len(new_data) - 1):
        if gap < abs(new_data[j] - new_data[j+1]):
            gap = abs(new_data[j] - new_data[j+1])
    print("Class",i+1)
    print(f"Max {M}, Min {m}, Largest gap {gap}")
