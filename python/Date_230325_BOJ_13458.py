import sys
N = int(sys.stdin.readline().rstrip())
student = list(map(int, sys.stdin.readline().rstrip().split()))
B,C = map(int, sys.stdin.readline().rstrip().split())

b = [0 for i in range(N)]
for i in range(len(student)):
    student[i] -= B
    b[i] += 1
    if student[i] > 0:
        if student[i] % C == 0:
            b[i] += student[i] // C
        else:
            b[i] += student[i] // C + 1
print(sum(b))
