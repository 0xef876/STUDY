dic = {
    "c=":"č",
    "c-":"ć",
    "dz=":"dž",
    "d-":"đ",
    "lj":"lj",
    "nj":"nj",
    "s=":"š",
    "z=":"ž"
    }

n = input()
cnt = 0
def check():
    global cnt,n
    for i in dic.keys():
        if i in n:
            cnt += 1
            n = n.replace(i,'0',1)
            return check()
    return 1
while True:
    if check() == 1:
        break
print(len(n)+cnt - n.count('0'))
