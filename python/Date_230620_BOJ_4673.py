data = []
for i in range(1,10000):
    for j in str(i):
        i += int(j)
    if i <= 10000:
        data.append(i)

for i in range(1,10000):
    if i not in data:
        print(i)    