A , B = map(int,input().split())

cnt = 0
while True:
	if A == B:
		print(cnt+1) 
		break
	elif A > B:
		print(-1)
		break
	if B % 10 == 1:
		B //= 10
	
	elif B % 2 == 0:
		B //= 2
	else:
		print(-1)
		break
	cnt += 1
