s = input()
t = input()

while len(s) < len(t):
    if t[-1] == 'A': # 맨뒤가 A
        t = t[:-1] # 맨뒤를 제거
    else:
        t = t[:-1] # 맨뒤를 제거
        t = t[::-1] # 뒤집기
if s == t:
    print(1)
else:
    print(0)