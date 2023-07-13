n, k = map(int,input().split())
queue = [i for i in range(1,n+1)]

result = []
count = 0

for i in range(n):
    count += k-1
    if count >= len(queue):
        count = count%len(queue) # 나머지 연산자를 이용해 queue의 길이보다 큰 수가 나오는 경우를 대비
    result.append(str(queue.pop(count)))
print("<", ", ".join(result), ">", sep = '')