n = int(input()) # n 입력
my_list = list(map(int,input().split())) # 데이터 입력받아 리스트화
max,min = my_list[0],my_list[0] # 최대 최소 리스트의 0번째 인덱스 값으로 설정
dic={} # 딕셔너리 생성
# max와 min의 인덱스 값들을 딕셔너리에 추가
dic['max_idx'] = 0
dic['min_idx'] = 0
res = [] # 결과 리스트 생성
# for문을 돌며 res 리스트에 수익 , 매도가, 매수가 append 해주며 idx까지 최신화
for i in range(1,n):
    if max < my_list[i]:
        max = my_list[i]
        dic['max_idx'] = i
    elif min > my_list[i]:
        res.append((max-min,max,min))
        min = my_list[i]
        dic['min_idx'] = i
        max = my_list[i]
        dic['max_idx'] = i
res.append((max-min,max,min))
res_sorted = sorted(res,key=lambda x:(-x[0],x[2])) # 기준을 수익과 매수가로잡고 정렬
if dic['max_idx'] <= dic['min_idx']: # 매수가의 인덱스값이 매도가의 인덱스값보다 작거나 같으면 에러
    print(0)
else:
    print(res_sorted[0][1] - res_sorted[0][2])
