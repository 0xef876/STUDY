n = int(input())
fact = 1
for i in range(2,n+1):
    fact *= i
    while True:
        if str(fact)[-1] == "0":
            fact //= 10
        else:
            break
    fact %= 10 ** 15
print(str(fact)[-5:])
