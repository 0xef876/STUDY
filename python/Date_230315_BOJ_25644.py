n = int(input()) # n 입력
my_list = list(map(int,input().split())) # 데이터 입력받아 리스트화
M,m = my_list[0],my_list[0] # 최대 최소 리스트의 0번째 인덱스 값으로 설정
# max와 min의 인덱스 값들을 딕셔너리에 추가
res = [ 0 ] # 결과 리스트 생성
# for문을 돌며 res 리스트에 수익 , 매도가, 매수가 append 해주며 idx까지 최신화
for i in range(1,n):
    if M < my_list[i]:
        M = my_list[i]
    elif m > my_list[i]:
        res.append(M-m)
        m = my_list[i]
        M = my_list[i]
res.append(M-m)

print(max(res))
