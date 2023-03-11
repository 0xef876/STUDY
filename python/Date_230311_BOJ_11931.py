a = int(input())
data = []
for i in range(a):
    n = int(input())
    data.append(n)
data.sort(reverse = True)
for i in data:
    print(i)
