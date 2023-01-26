# BOJ 1764
import sys
a,b = map(int,sys.stdin.readline().split())
dic = {}

for i in range(a):
	name = sys.stdin.readline().strip()
	try :
		if dic[name]:
			dic[name] += 1
	except:
		dic[name] = 1
for j in range(b):
	name = sys.stdin.readline().strip()
	try :
		if dic[name]:
			dic[name] += 1
	except:
		dic[name] = 1
print(list(dic.values()).count(2))
dic = dict(sorted(dic.items()))

for i in dic.keys():
	if dic[i] == 2:
		print(i)

