a,b,c = map(int, input().split())
data = {i : [] for i in range(1,a+1)}
for i in range(b):
    d,e = map(int, input().split())
    data[d].append(e)
    data[e].append(d)


for i in data:
    data[i].sort()


def bfs(graph,s):
    v = []
    q = [s]
    while q:
        node = q.pop(0)
        if node not in v:
            v.append(node)
            q.extend(graph[node])

    return v    
def dfs(graph,s):
    v = []
    q = [s]
    while q:
        node = q.pop()
        if node not in v:
            v.append(node)
            q.extend(sorted(graph[node],reverse=True))

    return v


print(*dfs(data,c))
print(*bfs(data,c))