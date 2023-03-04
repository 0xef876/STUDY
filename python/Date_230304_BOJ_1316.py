n = int(input())
ans = n
for i in range(n):
  li = []
  s = input()
  state = 0
  for i in s:
    if s.count(i) > 1:
      index = -1
      data = []
      while True:
          index = s.find(i, index + 1)
          if index == -1:
              break
          data.append(index)
      li.append(data)
    for j in li:
      if j[-1] - j[0] != len(j)-1:
        state = 1
        break
  ans -= state
print(ans)
